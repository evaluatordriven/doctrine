#!/usr/bin/env python3
"""Build or verify MANIFEST.sha256 for the E-DI corpus, against this working tree.

No publishing credential is involved — so a clone of this repo verifies itself with nothing but
Python, which is what lets CI gate a push.

    python3 tools/build_manifest.py            # rewrite the manifest from the working tree
    python3 tools/build_manifest.py --verify    # compare; exit 1 on any difference

The root files are listed explicitly — they are the load set an agent must read, so their presence is a claim
worth asserting. The class folders are walked, so a file added to the corpus cannot be left out of its own
manifest. Naming the root makes a deletion visible; walking the groups makes a grouped addition visible. A root
*addition* fell through both halves — the operating instrument sat unhashed and unmanifested through two commits,
a version bump and a green CI run — so an unlisted root file now fails the build instead of being certified unseen.
"""
import hashlib
import os
import re
import subprocess
import sys

CORPUS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(CORPUS, "MANIFEST.sha256")
ROOT_FILES = [
    "README.md",
    "EDI-QUICKSTART.md",
    "EDI-PLAYBOOK.md",
    "EDI-OPERATING-INSTRUMENT.md",
    "EDI-MACHINE-CONTRACTS.md",
    "EDI-MANDATE.md",
    "EDI-EXAMPLE.md",
    "EDI-FOR-MACHINES.md",
    "EDI-RULE-INDEX.json",
    "EDI-TOOLS.md",
]
GROUPS = ["tools", "schemas"]

# Files that legitimately sit at the root and are not documents in the load set. Every other file at the root
# must be named in ROOT_FILES: a gate that reports PASS over a file it never looked at is not coverage.
ROOT_NON_DOCUMENTS = {"MANIFEST.sha256"}

# Folders that legitimately hold generated or tooling output and are not corpus content.
NON_CORPUS_DIRS = {"out", ".github", "__pycache__"}


def unknown_dirs():
    """FAIL LOUD ON A FOLDER THIS MANIFEST NEVER LOOKS AT.

    WHY THIS EXISTS. GROUPS is a hand-maintained list. A folder added to the corpus but not added to GROUPS is
    walked by nobody — its files are absent from MANIFEST.sha256, so nothing detects a later change to them,
    and `--verify` reports PASS because it only checks the files the manifest already covers. The root-file
    gate above closed this for files; this closes it for directories.

    It was found the honest way: four documents were added to a new folder, the manifest was regenerated, the
    consistency check was run, and ALL CHECKS PASSED — while all four files sat outside the manifest. The
    regeneration reported "262 files" and said nothing. It only surfaced by asking the manifest directly which
    of the files on disk it did not mention.
    """
    return [e for e in sorted(os.listdir(CORPUS))
            if os.path.isdir(os.path.join(CORPUS, e))
            and not e.startswith(".")
            and e not in GROUPS and e not in NON_CORPUS_DIRS]


def gate_dirs():
    """Fail loud on a corpus folder the manifest does not walk."""
    unseen = unknown_dirs()
    for d in unseen:
        n = sum(len(fs) for _, _, fs in os.walk(os.path.join(CORPUS, d)))
        print(f"  FAIL — folder {d}/ is not in GROUPS: its {n} file(s) are outside the manifest entirely")
    return unseen


def unknown_root_files():
    return [e for e in sorted(os.listdir(CORPUS))
            if not os.path.isdir(os.path.join(CORPUS, e))
            and not e.startswith(".")
            and e not in ROOT_FILES and e not in ROOT_NON_DOCUMENTS]


def gate_root():
    """Fail loud on a root file this manifest does not name."""
    missing = unknown_root_files()
    if missing:
        print(f"  FAIL — root file(s) not named in ROOT_FILES: {', '.join(missing)}")
    return missing


def version(text, label):
    m = re.search(r"\*\*Version:\*\*\s*([\d.]+)", text)
    if not m:
        print(f"  [WARN] no version line found in the {label}")
        return "?"
    return m.group(1)


def relpaths():
    paths = []
    for p in ROOT_FILES:
        if not os.path.isfile(os.path.join(CORPUS, p)):
            print(f"  [WARN] expected at the root but absent: {p}")
        else:
            paths.append(p)
    for g in GROUPS:
        d = os.path.join(CORPUS, g)
        if not os.path.isdir(d):
            print(f"  [WARN] class folder missing: {g}/")
            continue
        for root, dirs, files in os.walk(d):
            dirs[:] = [x for x in dirs if not x.startswith(".")]
            for f in sorted(files):
                if f.startswith(".") or f.endswith(".pyc"):
                    continue
                paths.append(os.path.relpath(os.path.join(root, f), CORPUS))
    return sorted(paths, key=lambda p: (("/" in p), p))


def rows():
    out = []
    for rel in relpaths():
        data = open(os.path.join(CORPUS, rel), "rb").read()
        out.append(f"{hashlib.sha256(data).hexdigest()}  {len(data):>7}  {rel}")
    return out


contracts = open(os.path.join(CORPUS, "EDI-MACHINE-CONTRACTS.md"), encoding="utf-8").read()
header = [
    "# E-DI contracts — MANIFEST.sha256",
    "# Computed from the bytes in this tree. Verify with:  python3 tools/build_manifest.py --verify",
    f"# Contracts v{version(contracts, 'Contracts')}. "
    "A file whose hash differs from its recorded hash has been changed",
    "# outside a version bump — which §12 requires to be regenerated in the same pass, not after it.",
    "",
]
def converge():
    """Run the pipeline to convergence before hashing.

    classify_rules rewrites §9's state block, which changes the Contracts' bytes, which changes the
    index the next run derives from it. A manifest built after a single pass therefore records a
    not-yet-settled index, and every later verification reports drift that is only the pipeline settling.
    Two passes and a stability check make that impossible to record."""
    idx = os.path.join(CORPUS, "EDI-RULE-INDEX.json")
    contracts = os.path.join(CORPUS, "EDI-MACHINE-CONTRACTS.md")
    tmp = os.path.join(CORPUS, "out", "_edi-rules.json")
    os.makedirs(os.path.dirname(tmp), exist_ok=True)
    last = None
    for _ in range(4):
        r1 = subprocess.run([sys.executable, os.path.join(CORPUS, "tools", "extract_rules.py"), contracts, tmp],
                            capture_output=True, text=True, cwd=CORPUS)
        r2 = subprocess.run([sys.executable, os.path.join(CORPUS, "tools", "classify_rules.py"), contracts, tmp, CORPUS],
                            capture_output=True, text=True, cwd=CORPUS)
        if r1.returncode or r2.returncode:
            # A step that refused to write leaves the index stale, and a stability check over a file that
            # was never rewritten reports settled. Hashing must not certify a write that did not happen.
            print((r1.stdout + r1.stderr + r2.stdout + r2.stderr).strip()[-800:])
            return False
        now = hashlib.sha256(open(idx, "rb").read()).hexdigest()
        if now == last:
            return True
        last = now
    print("  WARNING: the derived artifacts did not settle in four passes")
    return False


if "--verify" in sys.argv:
    if not os.path.exists(MANIFEST):
        print("  FAIL: no MANIFEST.sha256 to verify against")
        sys.exit(1)
    if gate_root() or gate_dirs():
        sys.exit(1)
    disk = {l.split()[-1]: l.split()[0] for l in open(MANIFEST) if l.strip() and not l.startswith("#")}
    now = {l.split()[-1]: l.split()[0] for l in rows()}
    bad = []
    for k in sorted(set(disk) | set(now)):
        if k not in now:
            bad.append(f"recorded but missing from the tree: {k}")
        elif k not in disk:
            bad.append(f"in the tree but not in the manifest: {k}")
        elif disk[k] != now[k]:
            bad.append(f"changed outside a version bump: {k}")
    if bad:
        print(f"  FAIL — {len(bad)} difference(s):")
        for b in bad:
            print(f"    {b}")
        sys.exit(1)
    print(f"  VERIFIED: all {len(now)} files match the manifest exactly")
    sys.exit(0)

if gate_root() or gate_dirs():
    sys.exit(1)
if not converge():
    print("  FAIL — a regeneration step refused to write; no manifest is built over a stale index")
    sys.exit(1)
rows_now = rows()
body = "\n".join(header + rows_now) + "\n"
open(MANIFEST, "w").write(body)
assert len(body.splitlines()) == len(header) + len(rows_now), "the announced count must be the row count"
print(f"  manifest written: {len(rows_now)} files, {len(body):,} B")
print(f"  header: {header[2]}")
