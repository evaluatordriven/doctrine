#!/usr/bin/env python3
"""Maker identity must not equal Evaluator identity on the same job.

Owner must not hold the Evaluator seat (proposal 0028 clause A).
"Family" is not machine-checkable yet; this tool checks exact identity only.

Usage: python3 tools/check_role_separation.py --packet <job.json>
Optional: --allow-separate-calls if packet.maker_evaluator_separate_calls is true
          (same model, separate calls — recorded). That flag does not allow
          Owner-as-Evaluator.
"""
import json, sys
from pathlib import Path


def ident(x):
    if isinstance(x, dict):
        return json.dumps(x, sort_keys=True)
    return str(x).strip().lower()


def owner_ident(p):
    if "owner" in p and p["owner"] not in (None, ""):
        return ident(p["owner"])
    if ident(p.get("human_seat", "")) == "owner":
        return "owner"
    return None


def main(argv):
    if len(argv) < 3 or argv[1] != "--packet":
        print((__doc__ or "").strip())
        return 2
    p = json.loads(Path(argv[2]).read_text())
    m, e = p.get("maker"), p.get("evaluator")
    if m is None or e is None:
        print("missing maker or evaluator")
        return 1
    ei = ident(e)
    oi = owner_ident(p)
    if ei == "owner" or (oi is not None and ei == oi):
        print("FAIL: Owner must not hold the Evaluator seat")
        return 1
    if ident(m) == ei:
        if p.get("maker_evaluator_separate_calls") is True or "--allow-separate-calls" in argv:
            print("OK (same identity recorded as separate calls)")
            return 0
        print("FAIL: maker identity equals evaluator identity")
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
