"""Shared reading of AUTHORITY.json for this repository's checkers. Standard library only.

Not authority itself: AUTHORITY.json is the chain of command; this module only reads it.
"""
from __future__ import annotations

import fnmatch
import json
import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class Report:
    """Collects named results. A check that never ran is not a pass."""

    def __init__(self, title: str):
        self.title = title
        self.fails: list[tuple[str, str]] = []
        self.passes: list[str] = []
        self.notes: list[str] = []

    def ok(self, cid: str, cond: bool, detail: str = "") -> bool:
        if cond:
            self.passes.append(cid)
            print(f"  [PASS] {cid}")
        else:
            self.fails.append((cid, detail))
            print(f"  [FAIL] {cid}   {detail}")
        return cond

    def note(self, text: str) -> None:
        self.notes.append(text)
        print(f"  [NOTE] {text}")

    def done(self) -> int:
        print()
        if self.fails:
            print(f"{self.title}: {len(self.fails)} FAILED, {len(self.passes)} passed")
            for cid, d in self.fails:
                print(f"  - {cid}: {d}")
            return 1
        if not self.passes:
            print(f"{self.title}: NOTHING RAN — that is a failure, not a pass")
            return 1
        print(f"{self.title}: ALL {len(self.passes)} CHECKS PASSED")
        return 0


def load(root: Path = ROOT) -> dict:
    return json.loads((root / "AUTHORITY.json").read_text(encoding="utf-8"))


def tier_files(auth: dict) -> dict[str, int]:
    """pattern -> tier, for tiers that hold files."""
    out: dict[str, int] = {}
    for t in auth["tiers"]:
        for f in t.get("files", []):
            out[f] = t["tier"]
    return out


def tracked_files(root: Path = ROOT) -> list[str]:
    """Files in the repository: git's view when it is a checkout, else a walk."""
    try:
        r = subprocess.run(["git", "-C", str(root), "ls-files", "-co", "--exclude-standard"],
                           capture_output=True, text=True, check=True)
        files = [l for l in r.stdout.splitlines() if l]
        if files:
            return sorted(f for f in files if (root / f).is_file())
    except Exception:  # noqa: BLE001
        pass
    out = []
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in {".git", "__pycache__", "out"}]
        for f in fn:
            out.append(str(Path(dp, f).relative_to(root)).replace(os.sep, "/"))
    return sorted(out)


def classify(path: str, auth: dict) -> list[str]:
    """Every pattern (tier file or no_authority) that claims this path."""
    pats = list(tier_files(auth)) + list(auth["no_authority"])
    return [p for p in pats if fnmatch.fnmatchcase(path, p)]


def tier_of(path: str, auth: dict) -> int | None:
    for pat, t in tier_files(auth).items():
        if fnmatch.fnmatchcase(path, pat):
            return t
    return None


def header_for(tier: int) -> str:
    return (f"**Authority:** tier {tier} in `../AUTHORITY.json` — outranked by tiers 0–{tier - 1}; "
            f"conflicts follow its conflict rule.")


def resolve(term: str, defined_in: dict[str, bool], auth: dict) -> tuple[str, str]:
    """The conflict rule, mechanised for terms a program can see.

    defined_in maps file -> whether that file states the term. Walk the tiers from 1 down; the first
    tier whose file states the term is the authority. Returns (verdict, authority file):
    verdict "decided" when a higher file answers, "needs_owner" when none does."""
    tiers = sorted({t["tier"] for t in auth["tiers"] if t["tier"] >= 1})
    for t in tiers:
        for f, has in defined_in.items():
            if has and tier_of(f, auth) == t:
                return "decided", f
    return "needs_owner", ""
