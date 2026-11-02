#!/usr/bin/env python3
"""Consistency checks for the E-DI corpus. Runs from anywhere; resolves paths against this repo.

Exit code 1 on any failure, so CI can refuse a push. Checks:

  1. the Contracts' structure: §0–§12 present, sequential, unique; subsections sequential
  2. every §-reference in the Contracts resolves, including §9's `enforces` column, and §9's rows are
     contiguous from C1 with no gaps
  3. every companion document's §-references resolve too
  4. the derived artifacts regenerate **byte-identically** — extract_rules.py then classify_rules.py, over the
     Contracts, then git-diffed — which is §12's rule that a version bump regenerates derived artifacts in the
     same pass, made mechanical
  5. MANIFEST.sha256 verifies against this tree

A §-reference qualified by another corpus's name (`Mandate §2 M3.1`, `PARAD §6 P27`) is that document's own
numbering and is not resolved here.
"""
import hashlib
import os
import re
import subprocess
import sys

CORPUS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = sys.executable
CONTRACTS = os.path.join(CORPUS, "EDI-MACHINE-CONTRACTS.md")
GROUPS = ["", "tools"]

# The public contracts carry only the load set and its machine layer. The private working corpus also held
# proposals, reviews, evaluation records and teaching documents; they are lineage, not law, and are not here.
COMPANIONS = ["README.md", "EDI-MANDATE.md", "EDI-OPERATING-INSTRUMENT.md", "EDI-TOOLS.md"]
# EDI-CHANGELOG.md is excluded deliberately: a changelog cites the sections that existed when each entry was
# written, so a reference that no longer resolves is the record working, not a defect.
fails = []


def resolve(name):
    for g in GROUPS:
        p = os.path.join(CORPUS, g, name) if g else os.path.join(CORPUS, name)
        if os.path.exists(p):
            return p
    return None


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {detail}" if not ok else ""))
    if not ok:
        fails.append(name)


def refs_in(text):
    stripped = re.sub(r"(?:Mandate|PARAD)\s*§\d+(?:\.\d+)?", "", text)
    return set(re.findall(r"§(\d+(?:\.\d+)?)", stripped))


txt = open(CONTRACTS, encoding="utf-8").read()

print("\n=== structure ===")
h2 = re.findall(r"^## (\d+)\.", txt, re.M)
h3 = re.findall(r"^### (\d+\.\d+)", txt, re.M)
have = set(h2) | set(h3)
check(f"§0–§12 present, sequential and unique ({len(h2)} sections, {len(h3)} subsections)",
      h2 == [str(i) for i in range(13)], f"{h2}")
for parent in h2:
    kids = sorted(int(s.split(".")[1]) for s in h3 if s.startswith(parent + "."))
    if kids:
        check(f"§{parent} subsections sequential", kids == list(range(1, len(kids) + 1)), f"{kids}")

print("\n=== references ===")
dangling = sorted(r for r in refs_in(txt) if r not in have and r != "9")
check(f"no dangling §-reference in the Contracts ({len(refs_in(txt))} distinct targets)", not dangling, f"{dangling}")
rows = re.findall(r"^\|\s*(?:~~)?\*{0,2}(C\d+)\*{0,2}(?:~~)?\s*\|.*?\|\s*([^|]+?)\s*\|\s*$", txt, re.M)
bad = [(cid, col) for cid, col in rows
       if not all(r in have or r == "9" for r in re.findall(r"§(\d+(?:\.\d+)?)", col))]
check("every §9 row's `enforces` column resolves", not bad, f"{bad}")
ids = [r[0] for r in rows]
check("§9 rows contiguous from C1 with no gaps", ids == [f"C{i}" for i in range(1, len(ids) + 1)], f"{ids}")

print("\n=== companion documents ===")
for name in COMPANIONS:
    p = resolve(name)
    if not p:
        check(f"{name} present", False, "not found in the root or any class folder")
        continue
    d = sorted(r for r in refs_in(open(p, encoding="utf-8").read()) if r not in have and r != "9")
    check(f"{name}: no dangling §-reference", not d, f"{d}")

print("\n=== derived artifacts regenerate byte-identically ===")
before = {f: hashlib.sha256(open(os.path.join(CORPUS, f), "rb").read()).hexdigest()
          for f in ("EDI-MACHINE-CONTRACTS.md", "EDI-RULE-INDEX.json")}
tmp = os.path.join(CORPUS, "_edi-rules.json")
r1 = subprocess.run([PY, os.path.join(CORPUS, "tools", "extract_rules.py"), CONTRACTS, tmp],
                    capture_output=True, text=True, cwd=CORPUS)
check("extract_rules.py runs clean (it self-tests first)", r1.returncode == 0,
      (r1.stdout + r1.stderr)[-300:])
r2 = subprocess.run([PY, os.path.join(CORPUS, "tools", "classify_rules.py"), CONTRACTS, tmp, CORPUS],
                    capture_output=True, text=True, cwd=CORPUS)
check("classify_rules.py runs clean (invariant asserted on every run)", r2.returncode == 0,
      (r2.stdout + r2.stderr)[-300:])
if r1.returncode or r2.returncode:
    # a comparison against unchanged files proves nothing when the writer crashed before writing —
    # reporting PASS here is how a broken regeneration passes for a working one
    check("derived artifacts unchanged by regeneration", False,
          "not run: a regeneration step failed, so an unchanged file proves nothing")
else:
    after = {f: hashlib.sha256(open(os.path.join(CORPUS, f), "rb").read()).hexdigest()
             for f in before}
    for f in before:
        check(f"{f} unchanged by regeneration", before[f] == after[f],
              f"{before[f][:12]} -> {after[f][:12]}")
if os.path.exists(tmp):
    os.remove(tmp)

print("\n=== manifest ===")
r3 = subprocess.run([PY, os.path.join(CORPUS, "tools", "build_manifest.py"), "--verify"],
                    capture_output=True, text=True, cwd=CORPUS)
print("  " + r3.stdout.strip().replace("\n", "\n  "))
check("MANIFEST.sha256 verifies against this tree", r3.returncode == 0)

# and a manifest that changes when nothing changed is not a manifest
h1 = hashlib.sha256(open(os.path.join(CORPUS, "MANIFEST.sha256"), "rb").read()).hexdigest()
subprocess.run([PY, os.path.join(CORPUS, "tools", "build_manifest.py")], capture_output=True, text=True, cwd=CORPUS)
h2 = hashlib.sha256(open(os.path.join(CORPUS, "MANIFEST.sha256"), "rb").read()).hexdigest()
check("MANIFEST.sha256 stable under a second build", h1 == h2,
      "a manifest that changes when nothing changed is not a manifest")
r4 = subprocess.run([PY, os.path.join(CORPUS, "tools", "build_manifest.py"), "--verify"],
                    capture_output=True, text=True, cwd=CORPUS)
check("MANIFEST.sha256 verifies after a rebuild", r4.returncode == 0,
      r4.stdout.strip()[-200:])

print("\n=== job packet schema (0018/0021) ===")
vp = os.path.join(CORPUS, "tools", "validate_job_packet.py")
fix = os.path.join(CORPUS, "schemas", "fixtures")
for name, want_ok in (
    ("example-job-packet.json", True),
    ("mvi-job-packet.json", True),
    ("readings-census.json", True),
    ("bad-unratified-accept.json", False),
    ("bad-unratified-filled.json", False),
    ("bad-readings-rejected.json", False),
    ("bad-census-on-scored.json", False),
    ("bad-readings-empty-bounds.json", False),
    ("bad-entry-b-no-reads.json", False),
    ("bad-mode-absent.json", False),
    ("bad-owner-evaluator-object.json", False),
    ("evaluator-kind-script.json", True),
    ("bad-evaluator-kind.json", False),
):
    path = os.path.join(fix, name)
    if not os.path.isfile(path):
        check(f"fixture present: {name}", False, "missing")
        continue
    r = subprocess.run([PY, vp, path], capture_output=True, text=True, cwd=CORPUS)
    ok = (r.returncode == 0) if want_ok else (r.returncode != 0)
    check(f"validate_job_packet {name} expect={'OK' if want_ok else 'FAIL'}",
          ok, (r.stdout or r.stderr or "")[:120].strip())

print("\n=== evaluator record schema (0041) ===")
vr = os.path.join(CORPUS, "tools", "validate_evaluator_record.py")
for name, want_ok in (
    ("evaluator-record-example.json", True),
    ("evaluator-record-saw-gt.json", True),
    ("bad-evaluator-record-empty-observation.json", False),
    ("bad-evaluator-record-extra-key.json", False),
    ("bad-evaluator-record-instrument-string.json", False),
    ("bad-evaluator-record-unlabelled-extension.json", False),
    ("bad-evaluator-record-unfiled-pass.json", False),
    ("bad-evaluator-record-pass-disagreement.json", False),
    ("bad-evaluator-record-unattributable-pass.json", False),
    ("bad-evaluator-record-regenerate-without-violation.json", False),
    ("bad-evaluator-record-below-floor-unnamed.json", False),
):
    path = os.path.join(fix, name)
    if not os.path.isfile(path):
        check(f"fixture present: {name}", False, "missing")
        continue
    r = subprocess.run([PY, vr, path], capture_output=True, text=True, cwd=CORPUS)
    ok = (r.returncode == 0) if want_ok else (r.returncode != 0)
    check(f"validate_evaluator_record {name} expect={'OK' if want_ok else 'FAIL'}",
          ok, (r.stdout or r.stderr or "")[:160].strip())
    if name == "evaluator-record-saw-gt.json":
        check("saw_gt fixture names the defect and does not fail the file",
              r.returncode == 0 and "defect: saw_gt" in r.stdout,
              (r.stdout or "")[:160].strip())
    if name == "bad-evaluator-record-empty-observation.json":
        check("empty observation error names observation",
              r.returncode != 0 and "observation" in (r.stdout + r.stderr),
              (r.stdout or r.stderr or "")[:160].strip())
    if name == "bad-evaluator-record-unfiled-pass.json":
        check("unfiled pass fails FOR THAT REASON and names it",
              r.returncode != 0 and "not filed" in r.stdout
              and "pass-not-filed-anywhere.json" in r.stdout,
              (r.stdout or "")[:200].strip())
    if name == "bad-evaluator-record-pass-disagreement.json":
        check("pass disagreement fails FOR THAT REASON and names it",
              r.returncode != 0 and "disagrees with the filed pass" in r.stdout,
              (r.stdout or "")[:200].strip())
    if name == "bad-evaluator-record-unattributable-pass.json":
        check("an unattributable score fails FOR THAT REASON (C35) and names both sides",
              r.returncode != 0 and "evidence not attributable" in r.stdout and "'D1'" in r.stdout,
              (r.stdout or "")[:220].strip())
    if name == "bad-evaluator-record-regenerate-without-violation.json":
        check("a regenerate with nothing to send back fails FOR THAT REASON (C36)",
              r.returncode != 0 and "names nothing it sends back" in r.stdout,
              (r.stdout or "")[:220].strip())
    if name == "bad-evaluator-record-below-floor-unnamed.json":
        check("a below-floor dimension with no violation naming it fails FOR THAT REASON (C36)",
              r.returncode != 0 and "below-floor dimension 'clarity'" in r.stdout and "'clarity'" in r.stdout,
              (r.stdout or "")[:220].strip())


print("\n=== instrument version pin (0026) ===")
inst = open(os.path.join(CORPUS, "EDI-OPERATING-INSTRUMENT.md"), encoding="utf-8").read()
im = re.search(r"\*v(\d+\.\d+)", inst)
cm = re.search(r"instrument-v(\d+\.\d+)", txt)
check(
    "instrument version pin matches header",
    bool(im and cm and im.group(1) == cm.group(1)),
    f"header={im.group(1) if im else None} pin={cm.group(1) if cm else None}",
)

print("\n=== instrument machine extract (0033 clause 4) ===")
_extract = re.findall(r"^\|\s*\*\*I(\d+)\*\*\s*\|\s*([^|]+?)\s*\|", inst, re.M)
if not _extract:
    check("machine extract present", False, "no I-id rows found in EDI-OPERATING-INSTRUMENT.md")
else:
    ids = [int(n) for n, _ in _extract]
    check("I-ids present and sequential from I1", ids == list(range(1, len(ids) + 1)),
          f"got {ids}")
    check("I-ids unique", len(set(ids)) == len(ids))
    check("extract covers A1-A5 and R1-R4",
          all(f"A{i}" in [c.strip() for _, c in _extract] for i in range(1, 6))
          and all(f"R{i}" in [c.strip() for _, c in _extract] for i in range(1, 5)))
    check("extract covers rules 1-12",
          all(f"Rule {i}" in [c.strip() for _, c in _extract] for i in range(1, 13)))
    # every Cites value resolves to text in THIS file
    rules_block = inst.split("## Rules in force", 1)[-1].split("### Machine extract", 1)[0]
    unresolved = []
    for _, cite in _extract:
        cite = cite.strip()
        if re.fullmatch(r"A[1-5]", cite):
            ok = re.search(rf"\*\*{cite} —", inst) is not None
        elif re.fullmatch(r"R[1-4]", cite):
            ok = re.search(rf"\*\*{cite} —", inst) is not None
        elif re.fullmatch(r"Rule \d+", cite):
            n = cite.split()[1]
            ok = re.search(rf"^{n}\. \*\*", rules_block, re.M) is not None
        elif cite == "Entry B thirteenth":
            ok = "thirteenth" in inst
        elif cite == "Escalation":
            ok = "An escalation carries four things" in inst
        else:
            ok = False
        if not ok:
            unresolved.append(cite)
    check("every extract Cites value resolves inside the Instrument", not unresolved,
          f"unresolved: {unresolved}")

print("\n=== fixtures: the registry reconciles against the directory ===")
# The control §10.2 requires, applied to an enumeration. Practice, not law: proposal 0053's clause 4 was
# struck, and this is what survived from it -- a registered list is a reader's own count, so an
# unregistered fixture and an unreferenced pass file are both invisible to the run that trusts the list.
# Both numbers are reported, so a disagreement is visible rather than inferred from silence.
_fdir = os.path.join(CORPUS, "schemas", "fixtures")
_on_disk = sorted(f for f in os.listdir(_fdir) if f.endswith(".json"))
_src = open(os.path.abspath(__file__), encoding="utf-8").read()
_named = set(re.findall(r'"([^"]+\.json)"', _src))
for _f in _on_disk:                      # a fixture may be an artifact another fixture references
    try:
        _named |= set(re.findall(r'"([^"]+\.json)"', open(os.path.join(_fdir, _f), encoding="utf-8").read()))
    except Exception:
        pass
_unaccounted = [f for f in _on_disk if f not in _named]
_referenced = sorted(set(re.findall(r'"(pass-[^"]+\.json)"',
                                    "".join(open(os.path.join(_fdir, f), encoding="utf-8").read()
                                            for f in _on_disk if not f.startswith("pass-")))))
_missing = [r for r in _referenced if not os.path.exists(os.path.join(_fdir, r))]
# A referenced pass that does not exist is legitimate ONLY where the check that exists for it already fails
# that record for a not-filed pass -- no name list and no exemption: the missing reference is accounted for
# by the verdict it is there to produce. (bad-evaluator-record-unfiled-pass.json is exactly that fixture.)
_missing_by_rule = []
for _r in _missing:
    _owners = [f for f in _on_disk if not f.startswith("pass-")
               and f'"{_r}"' in open(os.path.join(_fdir, f), encoding="utf-8").read()]
    _ok = False
    for _o in _owners:
        _rr = subprocess.run([PY, os.path.join(CORPUS, "tools", "validate_evaluator_record.py"),
                              os.path.join(_fdir, _o)], capture_output=True, text=True)
        if "not filed" in (_rr.stdout or ""):
            _ok = True
    if not _ok:
        _missing_by_rule.append(_r)
check(f"every fixture on disk is accounted for ({len(_on_disk)} on disk · "
      f"{len(_on_disk) - len(_unaccounted)} accounted · {len(_unaccounted)} unaccounted)",
      not _unaccounted, f"unaccounted: {_unaccounted}")
check(f"every referenced pass exists OR is accounted for by the check that exists for it "
      f"({len(_referenced)} references · {len(_missing)} missing · "
      f"{len(_missing) - len(_missing_by_rule)} accounted by their own reason)", not _missing_by_rule,
      f"unaccounted: {_missing_by_rule}")

print(f"\n{'ALL CHECKS PASSED' if not fails else 'FAILURES: ' + str(fails)}")
sys.exit(1 if fails else 0)
