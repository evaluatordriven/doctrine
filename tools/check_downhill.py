#!/usr/bin/env python3
"""Check that every lower tier agrees with the tiers above it (AUTHORITY.json). Checks run downhill only:
the higher file is the reference, and a disagreement is reported as a defect in the lower file.

    python3 tools/check_downhill.py              # check this tree; exit 1 on any failure
    python3 tools/check_downhill.py --strict     # also fail on doctrine rules whose gap status is "open"
    python3 tools/check_downhill.py --selftest   # show every check failing on a planted defect

Checks:
  D1  seats: the Playbook's seat table and the Contracts' seat list name DOCTRINE.md's seats
  D2  terminal states: For Machines and the job-packet schema carry DOCTRINE.md's three exits
  D3  outcomes: DOCTRINE.md's outcomes are in the job-packet schema's outcome enum
  D4  failure signals: the Mandate's F1-F6 carry DOCTRINE.md §8's words
  D5  family rule: the Operating Instrument's rule 2 and I14 carry DOCTRINE.md §3's rule
  D6  up-citation: every doctrine rule (D-ID) is carried by a lower file's Implements table, or declared
      not yet carried in AUTHORITY.json; every D-ID a table names exists; every local id a table names
      exists in its own file; DOCTRINE.md carries no source tags (the trace lives in the tables)
  D7  same tier: every Mandate id the Playbook cites exists in the Mandate; a gap is first tested against
      the tiers above, and goes to the Owner if none answers it
  D8  versions: the README's version claims match the files' own headers
  D9  links: relative links in the README, the contracts README and the CHANGELOG resolve
Standard library only. A pass means the mechanical checks agree; agreement in meaning that no program can
see is the implementing agent's job under the conflict rule.
"""
from __future__ import annotations

import contextlib
import io
import json
import re
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import authority as au  # noqa: E402

DOC, PB, MD, CT, IN, FM, EX = ("DOCTRINE.md", "contracts/EDI-PLAYBOOK.md", "contracts/EDI-MANDATE.md",
                              "contracts/EDI-MACHINE-CONTRACTS.md", "contracts/EDI-OPERATING-INSTRUMENT.md",
                              "contracts/EDI-FOR-MACHINES.md", "contracts/EDI-EXAMPLE.md")
SCHEMA = "contracts/schemas/job-packet.schema.json"


def norm(s: str) -> str:
    s = re.sub(r"⟨[^⟩]*⟩", "", s)
    s = s.replace("’", "'").replace("“", '"').replace("”", '"')
    return " ".join(s.split()).strip()


def section(text: str, start: str, end_pat: str = r"^## ") -> str:
    i = text.index(start)
    m = re.compile(end_pat, re.M).search(text, i + len(start))
    return text[i:m.start() if m else len(text)]


def mandate_defines(md: str, ident: str) -> bool:
    """An id is defined where the Mandate states it: a table row that opens with it, or a bold lead-in."""
    e = re.escape(ident)
    return bool(re.search(rf"^\| \*{{0,2}}{e}\*{{0,2}} \|", md, re.M) or re.search(rf"^\*\*{e}\.\*\*", md, re.M))


def defect(rep, cid, ok, lower, authority_file, detail):
    rep.ok(cid, ok, f"defect in {lower} (decided by {authority_file}): {detail}")


def check(root: Path, strict: bool = False) -> int:
    rep = au.Report("check_downhill")
    auth = au.load(root)
    rd = lambda f: (root / f).read_text(encoding="utf-8")
    doc_raw, pb, md, ct, ins, fm = rd(DOC), rd(PB), rd(MD), rd(CT), rd(IN), rd(FM)
    doc = re.sub(r'<a id="[^"]+"></a>', "", doc_raw)  # the anchors are for linking, not for reading

    print("=== D1 seats ===")
    seats = set(re.findall(r"^\| \*\*(\w+)\*\* \|", section(doc, "## 3. The seats"), re.M))
    rep.ok("D1 DOCTRINE.md names seven seats", len(seats) == 7, f"found {sorted(seats)}")
    pseats = set(re.findall(r"^\| \*\*(\w+)\*\* \|", section(pb, "## 6. Who does what"), re.M))
    defect(rep, "D1 the Playbook's seat table names DOCTRINE.md's seats", pseats == seats, PB, DOC,
           f"Playbook {sorted(pseats)} vs doctrine {sorted(seats)}")
    m = re.search(r"names who holds each — ([^.(]+)", ct)
    cseats = set(re.findall(r"\b([A-Z][a-z]+)\b", m.group(1))) if m else set()
    defect(rep, "D1 the Contracts' seat list names DOCTRINE.md's seats", cseats == seats, CT, DOC,
           f"Contracts {sorted(cseats)} vs doctrine {sorted(seats)}")

    print("\n=== D2-D3 terminal states and outcomes ===")
    exits_sec = section(doc, "### The exits", r"^\*\*Verdict and disposition")
    states = {s.replace(" ", "_") for s in re.findall(r"\*\*(accepted|needs owner|rejected)\*\*", exits_sec)}
    rep.ok("D2 DOCTRINE.md names three exits", len(states) == 3, f"found {sorted(states)}")
    fm_states = set(re.findall(r"`(\w+)`", re.search(r"Only: (.+?)\.", fm).group(1))) if re.search(r"Only: (.+?)\.", fm) else set()
    defect(rep, "D2 For Machines' terminal alphabet is DOCTRINE.md's", fm_states == states, FM, DOC,
           f"For Machines {sorted(fm_states)} vs doctrine {sorted(states)}")
    sch = json.loads(rd(SCHEMA))
    sch_states = set(sch["properties"]["terminal_state"].get("enum", []))
    defect(rep, "D2 the schema's terminal_state enum is DOCTRINE.md's", sch_states == states, SCHEMA, DOC,
           f"schema {sorted(sch_states)} vs doctrine {sorted(states)}")
    outcomes = {o.replace(" ", "_") for o in re.findall(r"^- \*([a-z ]+)\*:", exits_sec, re.M)}
    sch_out = set(sch["properties"]["outcome"].get("enum", []))
    defect(rep, "D3 DOCTRINE.md's outcomes are in the schema's outcome enum", outcomes and outcomes <= sch_out, SCHEMA, DOC,
           f"missing from schema: {sorted(outcomes - sch_out)}")

    print("\n=== D4 failure signals ===")
    s8 = section(doc, "## 8. How you would know it failed", r"^\*\*What is claimed")
    dF = {k: norm(v) for k, v in re.findall(r"^- \*\*(F\d)\.\*\* (.+?)(?=^- \*\*F\d\.|\Z)", s8, re.S | re.M)}
    mF = {k: norm(v) for k, v in re.findall(r"^\| \*\*(F\d)\*\* \| (.+) \|$", md, re.M)}
    rep.ok("D4 DOCTRINE.md states F1-F6", sorted(dF) == [f"F{i}" for i in range(1, 7)], f"found {sorted(dF)}")
    diff = [k for k in dF if mF.get(k) != dF[k]]
    defect(rep, "D4 the Mandate's F1-F6 carry DOCTRINE.md §8's words", not diff, MD, DOC, f"differ: {diff}")

    print("\n=== D5 the Maker-family rule ===")
    s3 = section(doc, "## 3. The seats")
    keys = ["differs from the Maker in model family", "no more than half", "undisclosed"]
    rep.ok("D5 DOCTRINE.md §3 states the family rule", all(k in norm(s3) for k in keys),
           f"missing in doctrine: {[k for k in keys if k not in norm(s3)]}")
    rule2 = re.search(r"^2\. \*\*Three nouns.+?(?=^3\. )", ins, re.S | re.M)
    i14 = re.search(r"^\| \*\*I14\*\* \|.+$", ins, re.M)
    for name, blk in (("rule 2", rule2), ("I14", i14)):
        t = norm(blk.group(0)) if blk else ""
        defect(rep, f"D5 the Instrument's {name} carries DOCTRINE.md's family rule", all(k in t for k in keys), IN, DOC,
               f"missing: {[k for k in keys if k not in t]}")
        defect(rep, f"D5 the Instrument's {name} does not keep the old outright ban",
               "does not hold the Evaluator seat" not in t, IN, DOC, "the outright family ban is back")

    print("\n=== D6 up-citation: every doctrine rule is carried, and every citation resolves ===")
    dids = re.findall(r'<a id="(D[^"]+)"></a>', doc_raw)
    dup = sorted({d for d in dids if dids.count(d) > 1})
    rep.ok(f"D6 DOCTRINE.md anchors {len(dids)} rules, each id once", bool(dids) and not dup, f"repeated: {dup}")
    rep.ok("D6 DOCTRINE.md carries no source tags", "⟨" not in doc_raw,
           "a ⟨…⟩ tag is back; the trace belongs in the lower files' Implements tables")
    carried, bad_did, bad_local, tables = {}, [], [], {}
    local_ok = {
        PB: lambda l: bool(re.match(r"§(\d+)$", l)) and bool(re.search(rf"^## {l[1:]}\. ", pb, re.M)),
        MD: lambda l: mandate_defines(md, l),
        CT: lambda l: (bool(re.match(r"§[\d.]+$", l)) and bool(re.search(rf"^#+ {re.escape(l[1:])}[ .]", ct, re.M)))
                      or (bool(re.match(r"C\d+$", l)) and bool(re.search(rf"^\| (\*\*)?{l}(\*\*)? \|", ct, re.M))),
        IN: lambda l: bool(re.match(r"I\d+$", l)) and bool(re.search(rf"^\| \*\*{l}\*\* \|", ins, re.M)),
    }
    for f, text in ((PB, pb), (MD, md), (CT, ct), (IN, ins)):
        n = text.count("| This file | Carries | Basis |")
        rep.ok(f"D6 {f} has one Implements table", n == 1, f"found {n}")
        if n != 1:
            continue
        blk = text[text.index("| This file | Carries | Basis |"):]
        blk = blk[:blk.find("\n\n")] if "\n\n" in blk else blk
        for loc, ds in re.findall(r"^\| `([^`]+)` \| ([^|]+) \|", blk, re.M):
            if not local_ok[f](loc):
                bad_local.append(f"{f}: `{loc}` is not an id in this file")
            for d in (x.strip() for x in ds.split(",")):
                if d not in dids:
                    bad_did.append(f"{f}: `{loc}` names {d}, which DOCTRINE.md does not define")
                carried.setdefault(d, []).append(f"{f}:{loc}")
    gaps = auth.get("not_yet_carried", {})
    uncovered = [d for d in dids if d not in carried and d not in gaps]
    stale = [d for d in gaps if d in carried or d not in dids]
    defect(rep, "D6 every local id in an Implements table exists in its own file", not bad_local, "the table's file", DOC,
           "; ".join(bad_local))
    defect(rep, "D6 every doctrine id an Implements table names exists", not bad_did, "the table's file", DOC,
           "; ".join(bad_did))
    rep.ok("D6 every doctrine rule is carried by a lower file, or declared not yet carried", not uncovered,
           f"no lower file carries {uncovered}: implement it below, or declare it in AUTHORITY.json not_yet_carried")
    rep.ok("D6 every declared gap is still a gap (no stale entries)", not stale,
           f"remove from not_yet_carried: {stale}")
    rep.note(f"{len(carried)} of {len(dids)} doctrine rules carried; declared gaps: {sorted(gaps)}")
    open_gaps = sorted(d for d, g in gaps.items() if g.get("status") == "open")
    if open_gaps:
        msg = f"OPEN Owner decisions: doctrine rules no law carries yet: {open_gaps}"
        if strict:
            rep.ok("D6 --strict: no open gaps", False, msg)
        else:
            rep.note(msg + " (use --strict to fail on them)")

    print("\n=== D7 same tier: the Playbook's Mandate ids exist in the Mandate ===")
    cited = set()
    for a, b in re.findall(r"Mandate \*{0,2}([A-Z]\d+(?:\.\d+)?)(?:\*{0,2}[–-]\*{0,2}([A-Z]\d+(?:\.\d+)?))?\*{0,2}", pb):
        cited.add(a)
        if b:  # a range: every id in it must exist, not only the first
            pa, pb_ = a.rsplit(".", 1) if "." in a else (a[0], a[1:]), b.rsplit(".", 1) if "." in b else (b[0], b[1:])
            if pa[0] == pb_[0] and pa[1].isdigit() and pb_[1].isdigit():
                sep = "." if "." in a else ""
                cited.update(f"{pa[0]}{sep}{k}" for k in range(int(pa[1]), int(pb_[1]) + 1))
            else:
                cited.add(b)
    missing = sorted(c for c in cited if not mandate_defines(md, c))
    rep.ok(f"D7 the Playbook cites {len(cited)} Mandate ids", bool(cited), "none found; the check would be vacuous")
    for c in missing:
        verdict, by = au.resolve(c, {DOC: bool(re.search(rf"\*\*{re.escape(c)}\.?\*\*", doc))}, auth)
        if verdict == "decided":
            defect(rep, f"D7 Mandate id {c} cited by the Playbook", False, MD, by,
                   f"{by} states {c}; the Mandate must carry it")
        else:
            rep.ok(f"D7 Mandate id {c} cited by the Playbook", False,
                   f"needs Owner: {PB} and {MD} (both tier 2) disagree on {c}, and no higher tier answers it "
                   f"(checked {DOC})")
    if not missing:
        rep.ok("D7 every Mandate id the Playbook cites exists in the Mandate", True)

    print("\n=== D8 version claims ===")
    readme = rd("README.md")
    m = re.search(r"Contracts\s+v(\S+)\s+and\s+Operating\s+Instrument\s+v(\S+?),\s+published", readme)
    cv = re.search(r"^\*\*Version:\*\* (\S+)", ct, re.M)
    iv = re.search(r"\*v(\d+\.\d+) —", ins)
    rep.ok("D8 the README states the contracts' versions", bool(m), "no 'Contracts vX and Operating Instrument vY, published' line")
    if m and cv and iv:
        rep.ok("D8 the README's Contracts version is the Contracts' header", m.group(1) == cv.group(1),
               f"README v{m.group(1)} vs header v{cv.group(1)}")
        rep.ok("D8 the README's Instrument version is the Instrument's header", m.group(2) == iv.group(1),
               f"README v{m.group(2)} vs header v{iv.group(1)}")

    dm = re.search(r"Doctrine version (\d+\.\d+)", readme)
    dv = re.search(r"^Version (\d+\.\d+)", doc, re.M)
    rep.ok("D8 the README's doctrine version is DOCTRINE.md's", bool(dm and dv) and dm.group(1) == dv.group(1),
           f"README {dm.group(1) if dm else None} vs DOCTRINE.md {dv.group(1) if dv else None}")

    print("\n=== D9 relative links ===")
    broken = []
    for f in ("README.md", "contracts/README.md", "CHANGELOG.md"):
        for link in re.findall(r"\]\(([^)#]+)\)", rd(f)):
            if "://" in link:
                continue
            if not ((root / f).parent / link).exists():
                broken.append(f"{f} -> {link}")
    rep.ok("D9 every relative link resolves", not broken, f"broken: {broken}")
    return rep.done()


# ----------------------------------------------------------------------------- self-test

def _edit(rel, old, new):
    def m(root: Path):
        p = root / rel
        s = p.read_text(encoding="utf-8")
        assert old in s, f"self-test anchor missing in {rel}: {old[:60]!r}"
        p.write_text(s.replace(old, new, 1), encoding="utf-8")
    return m


def _stale_version(root: Path):
    p = root / "README.md"
    s = p.read_text(encoding="utf-8")
    s2 = re.sub(r"Contracts v[\d.]+ and Operating Instrument", "Contracts v0.0.0 and Operating Instrument", s, count=1)
    assert s2 != s, "self-test anchor missing: the README's contracts version line"
    p.write_text(s2, encoding="utf-8")


def _open_gap(root: Path):
    """Declare a real doctrine rule as an open gap, and remove what carries it, so strict mode has one to fail on."""
    a = json.loads((root / "AUTHORITY.json").read_text(encoding="utf-8"))
    a["not_yet_carried"] = {"D4.14": {"status": "open", "note": "self-test"}}
    (root / "AUTHORITY.json").write_text(json.dumps(a), encoding="utf-8")
    _edit(IN, "| `I21` | D4.14 |", "| `I21` | D4.13 |")(root)
    _edit(MD, "| `M8` | D4.14 |", "| `M8` | D4.13 |")(root)


def _stale_gap(root: Path):
    a = json.loads((root / "AUTHORITY.json").read_text(encoding="utf-8"))
    a["not_yet_carried"] = {"D6.2": {"status": "open", "note": "self-test: still declared, but I2 carries it"}}
    (root / "AUTHORITY.json").write_text(json.dumps(a), encoding="utf-8")


def _schema_states(root: Path):
    p = root / SCHEMA
    s = json.loads(p.read_text(encoding="utf-8"))
    s["properties"]["terminal_state"]["enum"].append("abandoned")
    p.write_text(json.dumps(s, indent=2), encoding="utf-8")


CASES = [
    ("CONTROL: the tree as it stands passes", None, False, 0, ""),
    ("a seat renamed in the Playbook is a Playbook defect (D1)",
     _edit(PB, "| **Buyer** |", "| **Customer** |"), False, 1, "D1 the Playbook's seat table"),
    ("a fourth terminal state in For Machines fails D2",
     _edit(FM, "Only: `accepted` | `needs_owner` | `rejected`", "Only: `accepted` | `needs_owner` | `rejected` | `abandoned`"),
     False, 1, "D2 For Machines' terminal alphabet"),
    ("a fourth terminal state in the schema fails D2", _schema_states, False, 1, "D2 the schema's terminal_state"),
    ("the Mandate's F5 trimmed back fails D4",
     _edit(MD, " Or the Owner is forced to carry an attention cost", " Or maybe a cost"), False, 1, "D4 the Mandate's F1-F6"),
    ("the old outright family ban restored in rule 2 fails D5",
     _edit(IN, "**At least one Evaluator differs from the Maker in model family;", "**The Maker's family does not hold the Evaluator seat. At least one Evaluator differs from the Maker in model family;"),
     False, 1, "D5 the Instrument's rule 2 does not keep"),
    ("a Mandate id an Implements table names, removed from the Mandate, fails D6",
     _edit(MD, "| **M8** |", "| **MX** |"), False, 1, "D6 every local id"),
    ("an Implements row naming a doctrine id that does not exist fails D6",
     _edit(IN, "| `I21` | D4.14 |", "| `I21` | D4.15 |"), False, 1, "D6 every doctrine id an Implements table names"),
    ("a new doctrine rule no lower file carries fails D6",
     _edit(DOC, '14. <a id="D4.14"></a>', '15. <a id="D4.15"></a>Placeholder rule.\n\n14. <a id="D4.14"></a>'), False, 1,
     "D6 every doctrine rule is carried"),
    ("a source tag reintroduced in DOCTRINE.md fails D6",
     _edit(DOC, "**Proportion.**", "**Proportion.** ⟨Mandate M7⟩"), False, 1, "D6 DOCTRINE.md carries no source tags"),
    ("a declared gap that is now carried is stale and fails D6", _stale_gap, False, 1, "D6 every declared gap is still a gap"),
    ("same tier, no higher answer: the Playbook citing a Mandate id that does not exist goes to the Owner (D7)",
     _edit(PB, "(Mandate **P2**;", "(Mandate **X9**; Mandate **P2**;"), False, 1, "D7 Mandate id X9"),
    ("same tier, a cited range: every id in it is checked, not only the first (D7)",
     _edit(PB, "(Mandate **P2**;", "(Mandate **M1.1–M1.2**; Mandate **P2**;"), False, 1, "D7 Mandate id M1.2"),
    ("a stale version claim in the README fails D8", _stale_version, False, 1, "D8 the README's Contracts version"),
    ("a stale doctrine version in the README fails D8",
     _edit("README.md", "Doctrine version 0.2", "Doctrine version 0.1"), False, 1, "D8 the README's doctrine version"),
    ("a broken relative link fails D9",
     _edit("README.md", "[`CHANGELOG.md`](CHANGELOG.md)", "[`CHANGELOG.md`](CHANGES.md)"), False, 1, "D9 every relative link"),
    ("--strict fails while a declared gap is open", _open_gap, True, 1, "D6 --strict"),
]


def selftest() -> int:
    bad = 0
    for name, mut, strict, want, cid in CASES:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "repo"
            shutil.copytree(au.ROOT, root, ignore=shutil.ignore_patterns(".git", "__pycache__", "out"))
            if mut:
                mut(root)
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                got = check(root, strict)
        ok = got == want and (not cid or f"[FAIL] {cid}" in buf.getvalue())
        bad += not ok
        print(f"  {'PASS' if ok else 'FAIL'}  {name}  -> exit {got} (wanted {want}"
              + (f", failing on {cid!r})" if cid else ")"))
        if not ok:
            print("\n".join("        " + l for l in buf.getvalue().splitlines() if "[FAIL]" in l))
    print(f"\ncheck_downhill --selftest: {len(CASES) - bad}/{len(CASES)} cases behaved as required")
    return 1 if bad else 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    sys.exit(check(au.ROOT, "--strict" in sys.argv))
