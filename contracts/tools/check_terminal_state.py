#!/usr/bin/env python3
"""Assert terminal_state ∈ {accepted, needs_owner, rejected}.

Usage: python3 tools/check_terminal_state.py <state>
   or: python3 tools/check_terminal_state.py --packet <job.json>
"""
import json, sys
from pathlib import Path
ALLOWED = {"accepted", "needs_owner", "rejected"}

def main(argv):
    if len(argv) == 2 and argv[1] not in ("-h", "--help"):
        s = argv[1]
    elif len(argv) == 3 and argv[1] == "--packet":
        s = json.loads(Path(argv[2]).read_text())["terminal_state"]
    else:
        print(__doc__.strip()); return 2
    if s not in ALLOWED:
        print(f"illegal terminal_state: {s!r}"); return 1
    print("OK", s); return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
