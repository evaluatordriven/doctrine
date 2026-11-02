#!/usr/bin/env python3
"""Validate a scored E-DI evaluator record against schemas/evaluator-record.schema.json.

A pass is not C8. This checker does not apply the pass rule, does not compare the
record to a packet, and does not decide a terminal state.

saw_gt is a named defect, not a failed file: the checker prints `defect: saw_gt`
and exits 0.

C35 (v1.21.0): the instrument's dimension list is the job's vocabulary, so a filed pass may not score a
dimension the record does not declare (`evidence not attributable`, an ERROR), and a declared dimension
no filed pass observed rests on ZERO passes, which is also an ERROR -- zero is not one, and rule 10's
single-pass label is unchanged for exactly one. The instrument-to-record link is NOT checked: nothing
here requires the instrument to be machine-readable, and the clause names that as a duty on the author.

C34 (v1.20.0): the record names its passes and every named pass is filed BESIDE the record, so this
checker resolves each `passes[].artifact` against the record's own directory and loads it. A named
pass that is not filed is an ERROR -- the reported fact is `evidence not filed`, which is what the
job's own declaration already records, not a defect in a reading already taken. A dimension observed
by a single pass prints `note: single-pass` and exits 0: Instrument rule 10 labels a one-run reading,
it does not ban it. What is NOT checked, and is an audit item instead: whether a channel is a model
channel (this corpus defines no channel vocabulary and does not invent one), and whether the
instrument required more passes than were filed (nothing in the record declares the instrument's N). The Orchestrator exits needs_owner. The Orchestrator stamps
instrument_in_force before this checker runs. The Evaluator does not emit the hashes.

Like the packet gate, the stdlib structural check always runs and the Draft 2020-12 pass
runs only when jsonschema is installed -- a declaration this file did not carry before
proposal 0049. The verdict names the level that produced it: `OK (schema-verified)` or
`OK (structural only)`.

Usage:  python3 tools/validate_evaluator_record.py <record.json>
Exit 0 = shape ok (defects may be named on stdout); 1 = errors; 2 = usage/IO.
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path

CORPUS = Path(__file__).resolve().parents[1]
SCHEMA = CORPUS / "schemas" / "evaluator-record.schema.json"
PASS_SCHEMA = CORPUS / "schemas" / "pass.schema.json"
CLASSES = {
    "artifact_missed_standard",
    "standard_moved",
    "dimension_unauthorized",
    "frame_at_fault",
}
VERDICTS = {"accept", "regenerate", "needs_owner", "reject"}
ACCESS = {"none", "blind_to_gt", "saw_gt"}
HARDNESS = {"INVARIANT", "DOCUMENT", "PRIOR"}
SHA = re.compile(r"^[a-f0-9]{64}$")
PASS_KINDS = {"scored", "confirmation"}
PASS_STATUSES = {"filed", "void"}
PASS_KEYS = {
    "pass_id", "kind", "status", "void_cause", "channel",
    "provider", "model", "family", "rubric_sha256", "code_sha256",
    "run_ref", "scores", "instance_extensions",
}
ROOT_KEYS = {
    "job_id", "iteration", "passes", "dimensions", "pass_rule", "violations", "verdict",
    "ground_truth_ref", "ground_truth_version", "ground_truth_hardness",
    "mandate_ref", "instrument_in_force", "evaluator_identity",
    "channel_blind", "ratified", "instance_extensions",
}
REQUIRED = [
    "passes",
    "dimensions", "pass_rule", "violations", "verdict",
    "ground_truth_ref", "ground_truth_version", "ground_truth_hardness",
    "mandate_ref", "instrument_in_force", "evaluator_identity",
    "channel_blind", "ratified",
]


def _blank(v) -> bool:
    return v is None or (isinstance(v, str) and not v.strip()) or v in ({}, [])


def structural(rec: dict) -> tuple[list[str], list[str]]:
    errs: list[str] = []
    defects: list[str] = []
    if not isinstance(rec, dict):
        return ["record is not an object"], []
    for k in rec:
        if k not in ROOT_KEYS:
            errs.append(f"unlabelled extra key: {k}")
    for k in REQUIRED:
        if k not in rec:
            errs.append(f"missing required: {k}")
    dims = rec.get("dimensions")
    if not isinstance(dims, list) or not dims:
        errs.append("dimensions must be a non-empty array")
    else:
        for i, d in enumerate(dims):
            if not isinstance(d, dict):
                errs.append(f"dimensions[{i}] is not an object")
                continue
            for extra in d:
                if extra not in {
                    "name", "score", "scale", "anchor_note",
                    "observation", "observation_channel", "ground_truth_access",
                }:
                    errs.append(f"dimensions[{i}] unlabelled extra key: {extra}")
            for k in ("name", "score", "observation", "observation_channel", "ground_truth_access"):
                if k not in d:
                    errs.append(f"dimensions[{i}] missing {k}")
            if "observation" not in d or _blank(d.get("observation")):
                errs.append(f"dimensions[{i}] observation empty")
            if d.get("ground_truth_access") not in ACCESS and "ground_truth_access" in d:
                errs.append(f"dimensions[{i}] ground_truth_access not in enum")
            if d.get("ground_truth_access") == "saw_gt":
                defects.append("saw_gt")
            if "score" in d and not isinstance(d.get("score"), (int, float)):
                errs.append(f"dimensions[{i}] score is not a number")
    pr = rec.get("pass_rule")
    if isinstance(pr, dict):
        for k in ("accept", "dimension_floor", "reject", "cap"):
            if k not in pr:
                errs.append(f"pass_rule missing {k}")
            elif not isinstance(pr.get(k), (int, float)):
                errs.append(f"pass_rule.{k} is not a number")
        for extra in pr:
            if extra not in {"accept", "dimension_floor", "reject", "cap"}:
                errs.append(f"pass_rule unlabelled extra key: {extra}")
    elif "pass_rule" in rec:
        errs.append("pass_rule is not an object")
    viol = rec.get("violations")
    if isinstance(viol, list):
        for i, v in enumerate(viol):
            if not isinstance(v, dict):
                errs.append(f"violations[{i}] is not an object")
                continue
            for k in ("id", "class", "observation"):
                if k not in v or _blank(v.get(k)):
                    errs.append(f"violations[{i}] missing {k}")
            if v.get("class") not in CLASSES and "class" in v:
                errs.append(f"violations[{i}] class not in the four locators")
    elif "violations" in rec:
        errs.append("violations is not an array")
    if rec.get("verdict") not in VERDICTS and "verdict" in rec:
        errs.append("verdict not in enum")
    if rec.get("ground_truth_hardness") not in HARDNESS and "ground_truth_hardness" in rec:
        errs.append("ground_truth_hardness not in enum")
    for k in ("ground_truth_ref", "ground_truth_version", "evaluator_identity"):
        if k in rec and _blank(rec.get(k)):
            errs.append(f"{k} empty")
    mandate = rec.get("mandate_ref")
    if "mandate_ref" in rec:
        if not isinstance(mandate, dict):
            errs.append("mandate_ref is not an object {doc, version}")
        else:
            for k in ("doc", "version"):
                if k not in mandate or _blank(mandate.get(k)):
                    errs.append(f"mandate_ref.{k} empty")
    inst = rec.get("instrument_in_force")
    if "instrument_in_force" in rec:
        if not isinstance(inst, dict):
            errs.append("instrument_in_force is not an object")
        else:
            if _blank(inst.get("version")):
                errs.append("instrument_in_force.version empty")
            for k in ("rubric_sha256", "code_sha256"):
                if not isinstance(inst.get(k), str) or not SHA.match(inst.get(k, "")):
                    errs.append(f"instrument_in_force.{k} is not a sha256")
    if "channel_blind" in rec and not isinstance(rec.get("channel_blind"), bool):
        errs.append("channel_blind is not a boolean")
    if "ratified" in rec and not isinstance(rec.get("ratified"), bool):
        errs.append("ratified is not a boolean")
    exts = rec.get("instance_extensions")
    if exts is not None:
        if not isinstance(exts, list):
            errs.append("instance_extensions is not an array")
        else:
            for i, item in enumerate(exts):
                if not isinstance(item, dict):
                    errs.append(f"instance_extensions[{i}] is not an object")
                    continue
                if item.get("label") != "instance-specific":
                    errs.append(f"instance_extensions[{i}] label is not instance-specific")
                if _blank(item.get("name")):
                    errs.append(f"instance_extensions[{i}] name empty")
    passes = rec.get("passes")
    if not isinstance(passes, list) or not passes:
        errs.append("passes must be a non-empty array (a job that ran one pass files one pass)")
    else:
        for i, p in enumerate(passes):
            if not isinstance(p, dict):
                errs.append(f"passes[{i}] is not an object")
                continue
            for extra in p:
                if extra not in {"pass_id", "kind", "status", "artifact"}:
                    errs.append(f"passes[{i}] unlabelled extra key: {extra}")
            for k in ("pass_id", "kind", "status", "artifact"):
                if k not in p or _blank(p.get(k)):
                    errs.append(f"passes[{i}] missing {k}")
            if p.get("kind") not in PASS_KINDS and "kind" in p:
                errs.append(f"passes[{i}] kind not in {sorted(PASS_KINDS)}")
            if p.get("status") not in PASS_STATUSES and "status" in p:
                errs.append(f"passes[{i}] status not in {sorted(PASS_STATUSES)}")
    # one name, even if several dimensions saw ground truth
    if defects:
        defects = ["saw_gt"]
    return errs, defects


def structural_pass(p: dict) -> list[str]:
    """The stdlib shape check for one filed pass. Mirrors schemas/pass.schema.json.

    Always runs; the Draft 2020-12 pass is added by the caller when jsonschema is importable.
    """
    errs: list[str] = []
    if not isinstance(p, dict):
        return ["pass is not an object"]
    for k in p:
        if k not in PASS_KEYS:
            errs.append(f"unlabelled extra key: {k}")
    for k in ("pass_id", "kind", "status", "channel", "rubric_sha256", "code_sha256", "run_ref"):
        if k not in p or _blank(p.get(k)):
            errs.append(f"missing {k}")
    if p.get("kind") not in PASS_KINDS and "kind" in p:
        errs.append(f"kind not in {sorted(PASS_KINDS)}")
    if p.get("status") not in PASS_STATUSES and "status" in p:
        errs.append(f"status not in {sorted(PASS_STATUSES)}")
    for k in ("rubric_sha256", "code_sha256"):
        if isinstance(p.get(k), str) and not SHA.match(p.get(k, "")):
            errs.append(f"{k} is not a sha256")
    if p.get("status") == "void":
        if _blank(p.get("void_cause")):
            errs.append("void pass carries no void_cause")
        if "scores" in p:
            errs.append("void pass carries scores: an attempt that observed nothing is void, not filed-with-empty-scores")
    else:
        scores = p.get("scores")
        if not isinstance(scores, list) or not scores:
            errs.append("filed pass carries no scores")
        else:
            for i, s in enumerate(scores):
                if not isinstance(s, dict):
                    errs.append(f"scores[{i}] is not an object")
                    continue
                for extra in s:
                    if extra not in {"dimension", "score", "observation"}:
                        errs.append(f"scores[{i}] unlabelled extra key: {extra}")
                for k in ("dimension", "score"):
                    if k not in s or _blank(s.get(k)):
                        errs.append(f"scores[{i}] missing {k}")
                if "score" in s and not isinstance(s.get("score"), (int, float)):
                    errs.append(f"scores[{i}] score is not a number")
    return errs


def check_filed(rec: dict, record_dir: Path) -> tuple[list[str], list[str], list[str]]:
    """Resolve every named pass against the record's own directory (C34).

    Returns (errors, defects, notes). A named pass that is not filed is an ERROR. A single-pass
    dimension is a NOTE. A filed pass that is itself malformed is an ERROR, because the record
    rests on it.
    """
    errs: list[str] = []
    notes: list[str] = []
    passes = rec.get("passes")
    if not isinstance(passes, list):
        return errs, [], notes
    seen: dict[str, int] = {}
    dim_passes: dict[str, int] = {}
    attributable: dict[str, list[str]] = {}
    for i, p in enumerate(passes):
        if not isinstance(p, dict):
            continue
        pass_id = p.get("pass_id")
        artifact = p.get("artifact")
        if _blank(pass_id) or _blank(artifact):
            continue
        seen[str(pass_id)] = seen.get(str(pass_id), 0) + 1
        target = (record_dir / str(artifact)).resolve()
        if not target.is_file():
            errs.append(f"passes[{i}] not filed: {artifact} (evidence not filed)")
            continue
        try:
            filed = json.loads(target.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as e:
            errs.append(f"passes[{i}] filed but unreadable: {artifact}: {e}")
            continue
        for e in structural_pass(filed):
            errs.append(f"passes[{i}] ({artifact}): {e}")
        try:
            from jsonschema import Draft202012Validator
            pv = Draft202012Validator(json.loads(PASS_SCHEMA.read_text(encoding="utf-8")))
            for e in sorted(pv.iter_errors(filed), key=lambda e: list(e.path)):
                loc = "/".join(str(x) for x in e.path) or "(root)"
                errs.append(f"passes[{i}] ({artifact}): {loc}: {e.message}")
        except ImportError:
            pass
        for k in ("pass_id", "kind", "status"):
            if k in p and k in filed and p.get(k) != filed.get(k):
                errs.append(f"passes[{i}] {k} disagrees with the filed pass: record says {p.get(k)!r}, file says {filed.get(k)!r}")
        if isinstance(filed, dict) and isinstance(filed.get("scores"), list):
            for s in filed["scores"]:
                if isinstance(s, dict) and not _blank(s.get("dimension")):
                    d = str(s["dimension"])
                    dim_passes[d] = dim_passes.get(d, 0) + 1
                    attributable.setdefault(d, []).append(str(artifact))
    for pid, n in seen.items():
        if n > 1:
            errs.append(f"pass_id repeated across entries: {pid} ({n}x) -- a pass is one run, named once")
    dims = rec.get("dimensions")
    declared = {str(d["name"]) for d in dims
                if isinstance(d, dict) and not _blank(d.get("name"))} if isinstance(dims, list) else set()
    # C35 -- one dimension, one name. A score that attributes to nothing is an error, never a label:
    # counting by string equality silently reads it as observing nothing, so the dimension reads zero
    # passes and the record passes.
    for _dim in sorted(dim_passes):
        if _dim not in declared:
            errs.append(f"evidence not attributable: {attributable[_dim][0]} scores dimension {_dim!r}, which the record does not declare")
    if isinstance(dims, list):
        for d in dims:
            if not isinstance(d, dict) or _blank(d.get("name")):
                continue
            name = str(d["name"])
            n = dim_passes.get(name, 0)
            if n == 0:
                errs.append(f"evidence not attributable: dimension {name!r} rests on zero filed passes -- zero is not one")
            elif n == 1:
                notes.append(f"single-pass: dimension {name!r} rests on 1 pass -- Instrument rule 10, labelled and not a non-conformance")
    # C36 -- an iteration names what it sends back, and a below-floor dimension is a violation that names it.
    viols = rec.get("violations") if isinstance(rec.get("violations"), list) else []
    verdict = rec.get("verdict")
    if verdict == "regenerate" and not viols:
        errs.append("iteration names nothing it sends back: verdict 'regenerate' with no violation -- "
                    "an iteration tasked with nothing is not an iteration")
    named = [v.get("dimension") for v in viols if isinstance(v, dict) and not _blank(v.get("dimension"))]
    for _d in named:
        if str(_d) not in declared:
            errs.append(f"evidence not attributable: a violation names dimension {_d!r}, which the record does not declare")
    pr = rec.get("pass_rule") if isinstance(rec.get("pass_rule"), dict) else {}
    floor = pr.get("dimension_floor", rec.get("dimension_floor"))
    if isinstance(dims, list) and isinstance(floor, (int, float)):
        for d in dims:
            if not isinstance(d, dict) or _blank(d.get("name")):
                continue
            nm, sc = str(d["name"]), d.get("score")
            if isinstance(sc, (int, float)) and sc < floor and nm not in named:
                errs.append(f"below-floor dimension {nm!r} ({sc} < {floor}) carries no violation naming it -- "
                            f"the shortfall is required")
    # The population line (practice, not law -- 0053's clause 4 was struck): say what was read, so a zero
    # or short denominator is visible in the result rather than inferred from silence.
    _filed = sum(1 for _p in passes if isinstance(_p, dict) and (_p.get("artifact")) and not _blank(_p.get("artifact"))
                 and (record_dir / str(_p["artifact"])).is_file()) if isinstance(passes, list) else 0
    print(f"population: {len(dims) if isinstance(dims, list) else 0} dimension(s) declared · "
          f"{len(passes) if isinstance(passes, list) else 0} pass(es) named · {_filed} filed · "
          f"{len(viols)} violation(s) · {len(named)} naming a dimension")
    return errs, [], notes


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_evaluator_record.py <record.json>", file=sys.stderr)
        return 2
    path = Path(argv[1])
    try:
        rec = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        print(f"cannot read record: {e}", file=sys.stderr)
        return 2
    errs, defects = structural(rec)
    filed_errs, filed_defects, notes = check_filed(rec, path.parent)
    errs.extend(filed_errs)
    defects.extend(filed_defects)
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    verified = False
    try:
        from jsonschema import Draft202012Validator
        v = Draft202012Validator(schema)
        verified = True
        for e in sorted(v.iter_errors(rec), key=lambda e: list(e.path)):
            loc = "/".join(str(x) for x in e.path) or "(root)"
            errs.append(f"{loc}: {e.message}")
    except ImportError:
        pass
    for d in defects:
        print(f"defect: {d}")
    for n in notes:
        print(f"note: {n}")
    if errs:
        for e in errs:
            print(e)
        return 1
    print("OK (schema-verified)" if verified else "OK (structural only)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
