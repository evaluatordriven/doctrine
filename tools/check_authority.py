#!/usr/bin/env python3
"""Check that the chain of command in AUTHORITY.json holds across this repository.

    python3 tools/check_authority.py             # check this tree; exit 1 on any failure
    python3 tools/check_authority.py --selftest  # show every check failing on a planted defect

Checks:
  A1  AUTHORITY.json is well formed: tiers 0-6 contiguous, tier 0 is the Owner, tier 1 is DOCTRINE.md alone
  A2  every file in the repository is classified exactly once (a tier, or no authority)
  A3  every classification pattern matches at least one file (no stale entries)
  A4  each domain has one owner file, and that file sits on a tier
  A5  every load-bearing markdown file on tiers 2-6 carries its tier header, exactly
  A6  no file claims a tier header that is not its own
  A7  For Machines' list is the reading order in AUTHORITY.json, and it does not call itself an authority order
Standard library only. Not authority: a pass means the chain is well formed, not that the files agree
(tools/check_downhill.py checks that).
"""
from __future__ import annotations

import json
import re
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import authority as au  # noqa: E402


def check(root: Path) -> int:
    rep = au.Report("check_authority")
    auth = au.load(root)

    print("=== A1 the chain is well formed ===")
    tiers = [t["tier"] for t in auth["tiers"]]
    rep.ok("A1 tiers are 0..6, each once, in order", tiers == list(range(7)), f"got {tiers}")
    t0 = next((t for t in auth["tiers"] if t["tier"] == 0), {})
    rep.ok("A1 tier 0 is the Owner and holds no file", t0.get("holder") == "The Owner" and not t0.get("files"),
           f"tier 0 = {t0}")
    t1 = next((t for t in auth["tiers"] if t["tier"] == 1), {})
    rep.ok("A1 tier 1 is DOCTRINE.md alone", t1.get("files") == ["DOCTRINE.md"], f"tier 1 = {t1.get('files')}")
    listed = [f for t in auth["tiers"] for f in t.get("files", [])]
    dup = sorted({f for f in listed if listed.count(f) > 1})
    rep.ok("A1 no file sits on two tiers", not dup, f"on two tiers: {dup}")
    rep.ok("A1 the conflict rule is stated", len(auth.get("conflict_rule", [])) >= 3, "conflict_rule missing")

    print("\n=== A2-A3 every file is classified exactly once ===")
    files = au.tracked_files(root)
    unclassified, double = [], []
    for f in files:
        c = au.classify(f, auth)
        if not c:
            unclassified.append(f)
        elif len(c) > 1:
            double.append(f"{f} <- {c}")
    rep.ok(f"A2 every file classified ({len(files)} files)", not unclassified, f"unclassified: {unclassified}")
    rep.ok("A2 no file classified twice", not double, f"classified twice: {double}")
    import fnmatch
    pats = list(au.tier_files(auth)) + list(auth["no_authority"])
    stale = [p for p in pats if not any(fnmatch.fnmatchcase(f, p) for f in files)]
    rep.ok("A3 every pattern matches a file", not stale, f"matches nothing: {stale}")

    print("\n=== A4 each domain has one owner on a tier ===")
    bad = [f"{d} -> {f}" for d, f in auth.get("domains", {}).items()
           if f not in au.tier_files(auth)]
    rep.ok("A4 every domain owner is a tier file", not bad, f"not on a tier: {bad}")
    rep.ok("A4 'everything' belongs to DOCTRINE.md", auth.get("domains", {}).get("everything") == "DOCTRINE.md",
           "domain 'everything' must be DOCTRINE.md's")

    print("\n=== A5-A6 tier headers ===")
    missing, wrong = [], []
    for f in files:
        if not f.endswith(".md"):
            continue
        text = (root / f).read_text(encoding="utf-8")
        t = au.tier_of(f, auth)
        claimed = re.findall(r"^\*\*Authority:\*\* tier (\d+) in", text, re.M)
        if t is not None and t >= 2:
            head = "\n".join(text.split("\n")[:6])
            if au.header_for(t) not in head:
                missing.append(f"{f} (tier {t})")
            if any(int(c) != t for c in claimed):
                wrong.append(f"{f} claims tier {claimed}, is {t}")
        elif claimed:
            wrong.append(f"{f} claims tier {claimed} but is not on tiers 2-6")
    rep.ok("A5 every tier 2-6 markdown file opens with its exact tier header", not missing, f"missing or altered: {missing}")
    rep.ok("A6 no file claims a tier that is not its own", not wrong, "; ".join(wrong))

    print("\n=== A7 For Machines is a reading order, not an authority order ===")
    fm_path = "contracts/EDI-FOR-MACHINES.md"
    fm = (root / fm_path).read_text(encoding="utf-8")
    rep.ok("A7 For Machines does not call its list an authority order",
           "consultation and authority order" not in fm and "It is not an authority order" in fm,
           "For Machines must say its list is not an authority order")
    block = fm[fm.index("## Load set"):fm.index("**Do not load as authority:**")]
    items = re.findall(r"^\d+\. `([^`]+)`", block, re.M)
    names = []
    for it in items:
        p = (Path("contracts") / it).as_posix()
        p = str(Path(p)).replace("contracts/../", "")
        names.append(p if not it.startswith("../") else it[3:])
    names = [n for n in names if n != fm_path]
    want = [f for f in auth["reading_order"] if f != fm_path]
    rep.ok("A7 For Machines' numbered list matches AUTHORITY.json reading_order", names == want,
           f"For Machines {names} vs AUTHORITY.json {want}")
    rep.ok("A7 reading order starts with For Machines", auth["reading_order"][:1] == [fm_path],
           f"starts with {auth['reading_order'][:1]}")
    return rep.done()


# ----------------------------------------------------------------------------- self-test

def _mut_text(rel, old, new):
    def m(root: Path):
        p = root / rel
        s = p.read_text(encoding="utf-8")
        assert old in s, f"self-test mutation anchor missing in {rel}: {old[:60]!r}"
        p.write_text(s.replace(old, new, 1), encoding="utf-8")
    return m


def _mut_json(fn):
    def m(root: Path):
        p = root / "AUTHORITY.json"
        a = json.loads(p.read_text(encoding="utf-8"))
        fn(a)
        p.write_text(json.dumps(a, indent=2, ensure_ascii=False), encoding="utf-8")
    return m


CASES = [
    ("CONTROL: the tree as it stands passes", None, 0, ""),
    ("an unclassified file fails A2", lambda r: (r / "contracts" / "NEW-RULES.md").write_text("# New\n"), 1, "A2 every file classified"),
    ("a file on two tiers fails A1",
     _mut_json(lambda a: a["tiers"][3]["files"].append("contracts/EDI-MANDATE.md")), 1, "A1 no file sits on two tiers"),
    ("the Mandate claiming tier 3 fails A5/A6",
     _mut_text("contracts/EDI-MANDATE.md", "**Authority:** tier 2 in", "**Authority:** tier 3 in"), 1, "A6 no file claims"),
    ("the Instrument losing its header fails A5",
     _mut_text("contracts/EDI-OPERATING-INSTRUMENT.md", "**Authority:** tier 4 in", "**Note:** tier 4 in"), 1, "A5 every tier 2-6"),
    ("For Machines reasserting an authority order fails A7",
     _mut_text("contracts/EDI-FOR-MACHINES.md", "It is not an authority order", "It is the consultation and authority order"), 1, "A7 For Machines does not call"),
    ("For Machines reordering its list fails A7",
     _mut_text("contracts/EDI-FOR-MACHINES.md", "1. `EDI-PLAYBOOK.md`", "1. `EDI-QUICKSTART.md`"), 1, "A7 For Machines' numbered list"),
    ("tier 1 shared with another file fails A1",
     _mut_json(lambda a: a["tiers"][1]["files"].append("contracts/EDI-PLAYBOOK.md")), 1, "A1 tier 1 is DOCTRINE.md alone"),
    ("a domain owned by a no-authority file fails A4",
     _mut_json(lambda a: a["domains"].__setitem__("field names", "contracts/README.md")), 1, "A4 every domain owner"),
]


def selftest() -> int:
    import contextlib, io
    bad = 0
    for name, mut, want, cid in CASES:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "repo"
            shutil.copytree(au.ROOT, root, ignore=shutil.ignore_patterns(".git", "__pycache__", "out"))
            if mut:
                mut(root)
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                got = check(root)
        ok = got == want and (not cid or f"[FAIL] {cid}" in buf.getvalue())
        bad += not ok
        print(f"  {'PASS' if ok else 'FAIL'}  {name}  -> exit {got} (wanted {want}" + (f", failing on {cid!r})" if cid else ")"))
    print(f"\ncheck_authority --selftest: {len(CASES) - bad}/{len(CASES)} cases behaved as required")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else check(au.ROOT))
