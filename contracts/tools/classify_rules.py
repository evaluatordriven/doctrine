#!/usr/bin/env python3
"""E-DI rule classifier — owns §9's "State at vX" block and EDI-RULE-INDEX.json.

Usage:  classify_rules.py [contracts.md] [rules.json] [outdir]

Why it exists: the coverage invariant (§9) says every NORMATIVE rule has exactly one disposition, and
that a version which does not publish its dispositions has not run the invariant. This script is the
enforcement: the disposition table below is authored and reviewable row by row; every in-scope rule
must appear in it exactly once; every `LINE` must name a live §9 identifier; every live §9 row must be
claimed by at least one rule. It computes the counts, writes them into the Contracts (§9 state block —
computed, never typed), and emits the index. A failure here is a defect in the corpus, not in the run.

NOTE ON RULE IDS: `R`-ids are positional and therefore version-scoped — adding a section shifts them.
They are not cited outside `EDI-RULE-INDEX.json`. **`C`-ids are stable and never renumbered** (§12);
cite those.
"""
import hashlib
import json
import os
import re
import sys

CORPUS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = os.path.join(CORPUS, "out")   # scratch inside the corpus, never a session directory
CANON = os.path.join(CORPUS, "EDI-MACHINE-CONTRACTS.md")
_SRC_DEFAULT = f"{T}/EDI-MACHINE-CONTRACTS.md"
_ARGS = [a for a in sys.argv[1:] if not a.startswith("--")]
# The deliberate acknowledgement, and the only flag: the ids the table is keyed on have moved, the
# shift has been read, and the table has been re-keyed for it. Same shape as Plumbline's --repin.
REKEY = "--rekey" in sys.argv
if not _ARGS and not os.path.exists(_SRC_DEFAULT):
    # Standalone use: stage a scratch copy of the canonical Contracts. This tool rewrites §9 in place, so it must
    # never be pointed at the canonical text itself. Without this the corpus cannot check itself from the repo
    # alone, which was an open defect: it only ever ran under build_manifest, which stages the copy for it.
    import shutil
    os.makedirs(T, exist_ok=True)
    shutil.copyfile(CANON, _SRC_DEFAULT)
SRC = _ARGS[0] if len(_ARGS) > 0 else _SRC_DEFAULT
RULES = _ARGS[1] if len(_ARGS) > 1 else f"{T}/_edi-rules.json"
OUTDIR = _ARGS[2] if len(_ARGS) > 2 else T

# ============================ authored classification (v1.5) ============================
# Every in-scope NORMATIVE rule carries exactly one disposition. Reviewable row by row; not inferred.
LINE = {
    "R2": "C1",
    "R3": "C2",
    "R4": "C3",
    "R7": "C19",
    "R8": "C19",
    "R9": "C20",
    "R10": "C20",
    "R11": "C21",
    "R12": "C23",
    "R13": "C28",
    "R14": "C31",
    "R15": "C9",
    "R16": "C11",
    "R17": "C4",
    "R18": "C4",
    "R19": "C5",
    "R20": "C8",
    "R21": "C33 — scored frame (ground_truth source/version/hardness, mandate_ref doc+version, escalation route). Not structurally enforced: feedback forms, dimension set, retained-instrument reuse, task classes, escalation classes.",
    "R22": "C33 — scored frame (ground_truth source/version/hardness, mandate_ref doc+version, escalation route). Not structurally enforced: feedback forms, dimension set, retained-instrument reuse, task classes, escalation classes.",
    "R24": "C29",
    "R25": "C6",
    "R27": "C37",
    "R28": "C25",
    "R29": "C25",
    "R30": "C36",
    "R31": "C25",
    "R32": "C16",
    "R33": "C38",
    "R34": "C39",
    "R35": "C40",
    "R36": "C8",
    "R37": "C27",
    "R38": "C26",
    "R39": "C26",
    "R40": "C30",
    "R41": "C34",
    "R42": "C34",
    "R43": "C34",
    "R44": "C34",
    "R45": "C34",
    "R46": "C36",
    "R47": "C35",
    "R48": "C35",
    "R51": "C12",
    "R52": "C16",
    "R53": "C11",
    "R54": "C6",
    "R55": "C7",
    "R56": "C10",
    "R57": "C15",
    "R58": "C15",
    "R59": "C18",
    "R60": "C18",
    "R61": "C18",
    "R62": "C13",
    "R63": "C34",
    "R64": "C13",
    "R65": "C14",
    "R66": "C14",
    "R67": "C14",
    "R68": "C14",
    "R69": "C14",
    "R70": "C14",
    "R71": "C14",
    "R72": "C14",
    "R73": "C24",
    "R74": "C24",
    "R76": "C13",
    "R77": "C13",
    "R78": "C22",
    "R79": "C22",
    "R80": "C22",
    "R84": "C23",
    "R86": "C32",
}
SCHEMA = {
    "R23": "job-packet.schema.json — ratified:false forbids terminal accepted and forbids top-level bounds, specialist, and standard_ref",
    "R26": "job-packet.schema.json — seats are NOT required by the schema; Owner-as-Evaluator is rejected by validate_job_packet and check_role_separation (0028 A). Seven-seat object is not schema-required.",
}
NONE = {
    "R1": "definition of the term NORMATIVE",
    "R5": "build-order step — no conformance content beyond §1's ordering",
    "R6": "build-order step — no conformance content beyond §1's ordering",
    "R49": "orchestrator interface description",
    "R50": "orchestrator interface description",
    "R75": "explanation of why the two governance objects fail differently",
    "R81": "corpus self-description — the baseline label; nothing a deployment is audited for",
    "R82": "the vocabulary rename — how to read records filed before v1.8, not an implementation duty",
    "R83": "corpus self-description — the baseline label; nothing a deployment is audited for",
    "R85": "corpus self-description — the operating instrument's registration, authority rank and revision rule",
}
# The version is READ from the Contracts, never typed here: a hand-typed figure is a claim the tool cannot check,
# it goes stale on the next version bump, and it reads as authoritative the whole time — this constant said
# "1.9.2" while the document it described had already moved to v1.10.
_V = re.search(r"\*\*Version:\*\*\s*v?([\d.]+)", open(SRC, encoding="utf-8").read())
assert _V, f"no **Version:** line in {SRC} — the version is read from the document, never typed here"
VERSION = _V.group(1)

# ============================ load ============================
rules = json.load(open(RULES))["rules"]
in_scope = [r["id"] for r in rules]
by_id = {r["id"]: r for r in rules}
classified = set(LINE) | set(SCHEMA) | set(NONE)

missing = sorted(set(in_scope) - classified, key=lambda x: int(x[1:]))
extra = sorted(classified - set(in_scope), key=lambda x: int(x[1:]))
assert not missing, f"rules with NO disposition (a defect in this corpus): {missing}"
assert not extra, f"dispositions naming rules that do not exist: {extra}"
for a, b in (("LINE", "SCHEMA"), ("LINE", "NONE"), ("SCHEMA", "NONE")):
    ov = set(globals()[a]) & set(globals()[b])
    assert not ov, f"{a}/{b} overlap: {sorted(ov)}"

# §9 surface: every LINE clause must be a live row; every live row must be claimed
rows = json.load(open(RULES))["surface"]
live = {r["id"] for r in rows if not r["retired"]}
def _cid(v):
    m = re.match(r"(C\d+)", v)
    if not m:
        raise SystemExit(f"LINE via must start with a C-id: {v!r}")
    return m.group(1)
cited = {_cid(v) for v in LINE.values()}
assert cited <= live, f"LINE names a clause missing from §9's live surface: {sorted(cited - live)}"
unclaimed = sorted(live - cited, key=lambda x: int(x[1:]))
assert not unclaimed, f"§9 rows no rule points at: {unclaimed}"

# ==================== rule identity: the table must not silently re-point ====================
# R-ids are positional (see the note at the top), so an insertion moves every later id, and the
# assertions above cannot see it: they check that ids exist, that a LINE value starts with a live
# C-id, and that every live C-id is claimed. None of them binds an id to the RULE it was classified
# for. Measured 2026-10-05: an insertion that added one rule and no new §9 row left the tool
# reporting `UNCOVERED: 0` while 22 of 73 rows carried another rule's disposition.
#
# The comparison is against the index ALREADY ON DISK, which at this moment still records the
# previous binding -- classify is about to overwrite it.
_BASELINE = os.path.join(OUTDIR, "EDI-RULE-INDEX.json")


def _binding(rule):
    """(section, text prefix). The prefix, not the whole text: the index stores text[:400] and the
    extractor emits it raw, so a full-text comparison fires on a rule that did not change."""
    return (str(rule.get("section", "")), re.sub(r"\s+", " ", str(rule.get("text", ""))).strip()[:80])


if os.path.exists(_BASELINE):
    _prev = json.load(open(_BASELINE))["rules"]
    _moved = [(r["id"], _binding(r), _binding(by_id[r["id"]]))
              for r in _prev if r["id"] in by_id and _binding(r) != _binding(by_id[r["id"]])]
    if _moved:
        _ids = [m[0] for m in _moved]
        print(f"  the rule at {len(_moved)} id(s) is not the rule that was there before (R-ids are positional):")
        print(f"    moved: {', '.join(_ids)}")
        for _rid, _was, _now in _moved[:6]:
            print(f"    {_rid}: was §{_was[0]} {_was[1][:62]!r}")
            print(f"           now §{_now[0]} {_now[1][:62]!r}")
        if len(_moved) > 6:
            print(f"    ... and {len(_moved) - 6} more, in the list above")
        if not REKEY:
            raise SystemExit(
                f"REFUSED: {len(_moved)} id(s) no longer hold the rule they were classified for. Re-key the "
                f"disposition table for the shifted ids, re-read every entry the shift moved, then re-run with "
                f"--rekey to restate the baseline."
            )
        print(f"  --rekey: baseline restated for {len(_moved)} id(s). The dispositions above are now yours.")

counts = {"in_scope": len(in_scope), "line": len(LINE), "schema": len(SCHEMA), "none": len(NONE),
          "uncovered": 0}
assert sum(counts[k] for k in ("line", "schema", "none", "uncovered")) == counts["in_scope"]

print(f"in-scope rules: {counts['in_scope']}")
print(f"  LINE     : {counts['line']}  (across {len(cited)} live §9 rows)")
print(f"  SCHEMA   : {counts['schema']}")
print(f"  NONE     : {counts['none']}")
print(f"  UNCOVERED: {counts['uncovered']}")

# ============================ §9 state block (computed) ============================
state = f"""**State at v{VERSION}.** Of **{counts['in_scope']} in-scope NORMATIVE rules**:
**{counts['line']} are `LINE`**, **{counts['schema']} are `SCHEMA`**, **{counts['none']} are `NONE`**,
and **{counts['uncovered']} remain uncovered**.
"""

src = open(SRC).read()
blk = re.compile(r"(\*\*State at v[0-9.]+\*\*.*?|\<!--STATE_BLOCK--\>)(?=\nAn implementation that cannot tick)", re.S)
m = blk.search(src)
assert m, "§9 state-block anchor not found"
out = src[:m.start()] + state + src[m.end():]
assert "<!--STATE_BLOCK-->" not in out
with open(SRC, "w") as fh:
    fh.write(out)

# read back and re-assert the published numbers match what was computed
back = open(SRC).read()
mn = re.search(r"\*\*State at v([0-9.]+)\.\*\* Of \*\*(\d+) in-scope NORMATIVE rules\*\*:\s*\n"
               r"\*\*(\d+) are `LINE`\*\*, \*\*(\d+) are `SCHEMA`\*\*, \*\*(\d+) are `NONE`\*\*,\s*\n"
               r"and \*\*(\d+) remain uncovered\*\*", back)
assert mn, "state block written but not re-parsable"
got = dict(zip(("version", "in_scope", "line", "schema", "none", "uncovered"), mn.groups()))
assert got["version"] == VERSION and int(got["in_scope"]) == counts["in_scope"] \
    and int(got["line"]) == counts["line"] and int(got["schema"]) == counts["schema"] \
    and int(got["none"]) == counts["none"] and int(got["uncovered"]) == counts["uncovered"], got
print(f"\n§9 state block rewritten in {os.path.basename(SRC)} and read back: {got}")

# ============================ the rule index ============================
index = {
    "corpus": "E-DI", "contracts_version": VERSION,
    "generated_from": "EDI-MACHINE-CONTRACTS.md",
    "extracted_by": "extract_rules.py (v3 — reads this corpus, parses §9's table)",
    "dispositions": {"LINE": "enforced by an addressed §9 line — audited per deployment",
                     "SCHEMA": "enforced structurally by a named schema or hook",
                     "NONE": "a rule about the corpus: definition, rationale, or interface description"},
    "counts": counts,
    "generated_from_sha256": hashlib.sha256(open(SRC, "rb").read()).hexdigest(),
    "rules": [{"id": rid, "section": by_id[rid]["section"],
               "disposition": "LINE" if rid in LINE else "SCHEMA" if rid in SCHEMA else "NONE",
               "via": LINE.get(rid) or SCHEMA.get(rid) or NONE.get(rid),
               "text": by_id[rid]["text"][:400]} for rid in sorted(in_scope, key=lambda x: int(x[1:]))],
}
dst = os.path.join(OUTDIR, "EDI-RULE-INDEX.json")
json.dump(index, open(dst, "w"), indent=2)
print(f"rule index: {len(index['rules'])} rules -> {dst}")
print(f"sha256 contracts v{VERSION} {index['generated_from_sha256'][:16]}")
