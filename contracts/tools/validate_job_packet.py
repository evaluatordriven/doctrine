#!/usr/bin/env python3
"""Validate an E-DI job packet against schemas/job-packet.schema.json.

Usage:  python3 tools/validate_job_packet.py <packet.json|packet.yaml>
Exit 0 = ok; 1 = errors; 2 = usage/IO.
Stdlib structural check is the CI gate (no jsonschema required). If jsonschema
is installed, Draft 2020-12 runs as well; a packet must pass both. The verdict names
which of the two produced it: `OK (schema-verified)` or `OK (structural only)` -- a weaker
law must not wear the same word as a stronger one (proposal 0049).
"""
from __future__ import annotations
import json, sys
from pathlib import Path

CORPUS = Path(__file__).resolve().parents[1]
SCHEMA = CORPUS / "schemas" / "job-packet.schema.json"
TERMINALS = {"accepted", "needs_owner", "rejected"}
OUTCOMES = {
    "accepted", "census", "needs_owner", "rejected", "no_observation", "no_artifact",
}
SCORED_BOUND_KEYS = ("T_accept", "T_dim", "T_reject", "cap", "budget")


def load_packet(path: Path):
    text = path.read_text(encoding="utf-8")
    if path.suffix in {".yaml", ".yml"}:
        try:
            import yaml  # type: ignore
        except ImportError:
            print("YAML packet requires PyYAML; use JSON or pip install pyyaml", file=sys.stderr)
            sys.exit(2)
        return yaml.safe_load(text)
    return json.loads(text)


def _empty(v) -> bool:
    return v in (None, "", {}, [])


def structural(packet: dict, schema: dict) -> list[str]:
    errs = []
    if not isinstance(packet, dict):
        return ["root must be object"]
    for k in schema.get("required", []):
        if k not in packet:
            errs.append(f"missing required: {k}")
    if "entry" in packet and packet["entry"] not in ("A", "B"):
        errs.append(f"entry must be A|B, got {packet.get('entry')!r}")
    if "instrument_profile" in packet and packet["instrument_profile"] not in ("full", "mvi"):
        errs.append("instrument_profile must be full|mvi")
    if "terminal_state" in packet and packet["terminal_state"] not in TERMINALS:
        errs.append(f"illegal terminal_state: {packet.get('terminal_state')!r}")
    mode = packet.get("mode")
    if mode is not None and mode not in ("scored", "readings"):
        errs.append(f"mode must be scored|readings, got {mode!r}")
    if mode == "readings":
        if "bounds" in packet:
            errs.append("readings mode must not supply bounds/thresholds")
        if "specialist" in packet and not _empty(packet.get("specialist")):
            errs.append("readings mode must not name a specialist")
        if packet.get("terminal_state") == "rejected" or packet.get("outcome") == "rejected":
            errs.append("readings mode may not produce rejected")
    if mode == "scored":
        if "specialist" not in packet:
            errs.append("scored mode missing: specialist")
        bounds = packet.get("bounds")
        if not isinstance(bounds, dict):
            errs.append("scored mode missing: bounds object")
        else:
            for k in SCORED_BOUND_KEYS:
                if k not in bounds:
                    errs.append(f"scored bounds missing: {k}")
        gt = packet.get("ground_truth")
        if not isinstance(gt, list) or not gt:
            errs.append("scored mode missing: ground_truth")
        elif not all(isinstance(row, dict) for row in gt):
            errs.append("ground_truth rows must be objects")
        else:
            for i, row in enumerate(gt):
                for k in ("source", "version", "hardness"):
                    if k not in row or _empty(row.get(k)) or (isinstance(row.get(k), str) and not row[k].strip()):
                        errs.append(f"ground_truth[{i}] missing: {k}")
                if row.get("hardness") not in ("INVARIANT", "DOCUMENT", "PRIOR"):
                    errs.append(f"ground_truth[{i}] hardness must be INVARIANT|DOCUMENT|PRIOR")
        mandate = packet.get("mandate_ref")
        if not isinstance(mandate, dict):
            errs.append("scored mode missing: mandate_ref")
        else:
            for k in ("doc", "version"):
                v = mandate.get(k)
                if not isinstance(v, str) or not v.strip():
                    errs.append(f"mandate_ref missing: {k}")
        esc = packet.get("escalation")
        if esc is None or _empty(esc) or (isinstance(esc, str) and not esc.strip()):
            errs.append("scored mode missing: escalation")
    if packet.get("ratified") is not False:
        for k in ("human_seat", "standard_ref"):
            v = packet.get(k)
            if k not in packet or _empty(v) or (isinstance(v, str) and not v.strip()):
                errs.append(f"missing required: {k}")
    if packet.get("ratified") is False:
        if packet.get("terminal_state") == "accepted":
            errs.append("ratified:false cannot have terminal_state accepted")
        for k in ("bounds", "specialist", "standard_ref"):
            if k in packet:
                errs.append(f"ratified:false must not have top-level {k}")
    if "terminal_state" in packet:
        outcome = packet.get("outcome")
        if outcome not in OUTCOMES:
            errs.append("terminal_state requires outcome from the six-value enum")
        else:
            ts = packet["terminal_state"]
            if outcome in ("no_observation", "no_artifact") and ts != "needs_owner":
                errs.append(f"outcome {outcome} requires terminal_state needs_owner")
            if outcome == "census" and not (ts == "accepted" and mode == "readings"):
                errs.append("outcome census requires terminal_state accepted and mode readings")
            if outcome == "rejected" and not (ts == "rejected" and mode == "scored"):
                errs.append("outcome rejected requires terminal_state rejected and mode scored")
            if outcome == "accepted" and ts != "accepted":
                errs.append("outcome accepted requires terminal_state accepted")
            if outcome == "needs_owner" and ts != "needs_owner":
                errs.append("outcome needs_owner requires terminal_state needs_owner")
    if packet.get("entry") == "B":
        rbf = packet.get("reads_before_freeze")
        ok = (isinstance(rbf, str) and bool(rbf.strip())) or (isinstance(rbf, list) and len(rbf) > 0)
        if not ok:
            errs.append("entry B requires non-empty reads_before_freeze")
    ev = packet.get("evaluator")
    if isinstance(ev, str) and ev.strip().lower() == "owner":
        errs.append("Owner must not hold the Evaluator seat")
    elif isinstance(ev, dict):
        if "kind" in ev and ev["kind"] not in ("person", "model", "script"):
            errs.append("evaluator.kind must be person, model or script")
        identity_keys = ("name", "who", "seat", "holder")
        found_identity_key = any(k in ev for k in identity_keys)
        values_to_check = (
            [ev[k] for k in identity_keys if k in ev] if found_identity_key
            else list(ev.values())
        )
        if any(isinstance(v, str) and v.strip().lower() == "owner" for v in values_to_check):
            errs.append("Owner must not hold the Evaluator seat")
    for k in ("job_name", "buyer"):
        if k in packet and (not isinstance(packet[k], str) or not packet[k].strip()):
            errs.append(f"{k} must be non-empty string")
    if "artifact" in packet and packet["artifact"] in (None, "", {}):
        errs.append("artifact must be non-empty")
    return errs


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    path = Path(argv[1])
    if not path.is_file():
        print(f"not a file: {path}", file=sys.stderr)
        return 2
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    packet = load_packet(path)
    errs = structural(packet, schema)
    verified = False
    try:
        import jsonschema  # type: ignore
        from jsonschema import Draft202012Validator
        v = Draft202012Validator(schema)
        verified = True
        for e in sorted(v.iter_errors(packet), key=lambda e: list(e.path)):
            loc = "/".join(str(x) for x in e.path) or "(root)"
            errs.append(f"{loc}: {e.message}")
    except ImportError:
        pass
    if errs:
        for e in errs:
            print(e)
        return 1
    print("OK (schema-verified)" if verified else "OK (structural only)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
