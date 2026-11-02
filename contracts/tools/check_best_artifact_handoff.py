#!/usr/bin/env python3
"""Check the I24 handoff. The tool owns the best hash. The caller does not pass it.

A pass is not C8. This tool does not score. It does not write the artifact.
"""
import hashlib
import json
import sys
from pathlib import Path

RECORD = "edi-best-artifact.json"
BANNED = {"--best", "--best-path", "--best-hash", "--best-artifact"}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fail(check: str) -> int:
    print(f"fail: {check}")
    return 1


def load_record(job_dir: Path):
    path = job_dir / RECORD
    if not path.is_file():
        return None
    return json.loads(path.read_text())


def save_record(job_dir: Path, original: str, best: str) -> None:
    (job_dir / RECORD).write_text(json.dumps({
        "original_sha256": original,
        "best_sha256": best,
    }) + "\n")


def improves(incumbent: dict, candidate: dict) -> bool:
    if not incumbent or not candidate:
        return False
    if set(incumbent) - set(candidate):
        return False
    better = False
    for key, old in incumbent.items():
        new = candidate[key]
        if new < old:
            return False
        if new > old:
            better = True
    return better


def parse(argv):
    if any(a in BANNED or a.startswith("--best") for a in argv):
        return None, "caller_supplied_best_path"
    args = {
        "job_dir": None,
        "original": None,
        "maker_input": None,
        "incumbent": None,
        "candidate": None,
        "incumbent_vector": None,
        "candidate_vector": None,
        "unusable": False,
    }
    i = 1
    flags = {
        "--job-dir": "job_dir",
        "--original": "original",
        "--maker-input": "maker_input",
        "--incumbent": "incumbent",
        "--candidate": "candidate",
        "--incumbent-vector": "incumbent_vector",
        "--candidate-vector": "candidate_vector",
    }
    while i < len(argv):
        key = argv[i]
        if key == "--unusable":
            args["unusable"] = True
            i += 1
            continue
        if key not in flags or i + 1 >= len(argv):
            return None, "bad_args"
        args[flags[key]] = argv[i + 1]
        i += 2
    if not all(args[k] for k in ("job_dir", "original", "maker_input", "incumbent")):
        return None, "bad_args"
    return args, None


def as_vector(raw):
    if raw is None:
        return None
    data = json.loads(raw)
    if not isinstance(data, dict):
        raise ValueError("vector")
    return data


def main(argv) -> int:
    args, err = parse(argv)
    if err or args is None:
        return fail(err or "bad_args")
    job_dir = Path(args["job_dir"])
    original = Path(args["original"])
    maker_input = Path(args["maker_input"])
    incumbent = Path(args["incumbent"])
    original_hash = sha256(original)
    maker_hash = sha256(maker_input)
    incumbent_hash = sha256(incumbent)
    record = load_record(job_dir)
    best = None if record is None else record.get("best_sha256")

    if record is not None and record.get("original_sha256") != original_hash:
        return fail("original_hash_changed")

    if best is None:
        if args["unusable"]:
            if incumbent_hash != original_hash:
                return fail("unusable_replaced")
            print("OK")
            return 0
        if args["candidate"] is None:
            if incumbent_hash != original_hash:
                return fail("record_missing_incumbent_differs")
            if maker_hash != original_hash:
                return fail("maker_input_is_not_original")
            print("OK")
            return 0
        candidate_hash = sha256(Path(args["candidate"]))
        if incumbent_hash != candidate_hash:
            return fail("incumbent_is_not_first_artifact")
        save_record(job_dir, original_hash, candidate_hash)
        print("OK")
        return 0

    if maker_hash != best:
        if maker_hash == original_hash:
            return fail("maker_input_is_original")
        return fail("maker_input_is_not_best")

    if args["unusable"] or args["candidate"] is None:
        if incumbent_hash != best:
            return fail("non_dominating_replaced")
        print("OK")
        return 0

    candidate_hash = sha256(Path(args["candidate"]))
    try:
        inc_vec = as_vector(args["incumbent_vector"])
        cand_vec = as_vector(args["candidate_vector"])
    except (json.JSONDecodeError, ValueError):
        return fail("bad_vector")
    if inc_vec is None or cand_vec is None or not improves(inc_vec, cand_vec):
        if incumbent_hash != best:
            return fail("not_an_improvement")
        print("OK")
        return 0
    if incumbent_hash != candidate_hash:
        return fail("improvement_incumbent_mismatch")
    save_record(job_dir, original_hash, candidate_hash)
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
