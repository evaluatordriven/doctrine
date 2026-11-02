#!/usr/bin/env python3
"""E-DI rule extractor v3 — rule inventory + §9 conformance surface, from the Contracts.

Usage:  extract_rules.py <contracts.md> [out.json]

Fixes over v2:
  - v2 hard-coded a scratch path and a 14-line checkbox surface from the v1.0 layout; v1.3 made §9 a
    markdown table, so the surface parse found nothing and the self-test could not fail loudly.
  - the surface is now parsed from §9's table rows (identifier + clause text), and asserted non-empty.
  - self-tests are structural (a section declared NORMATIVE must yield rules; §9 must parse; the
    per-run-value rule must be found), not counts tied to one version.
Self-tests run before the output is trusted — do not use the output if they fail.
"""
import json
import os
import re
import sys

SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser(
    os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                 "EDI-MACHINE-CONTRACTS.md"))
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.expanduser(
    os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                 "out", "_edi-rules.json"))

lines = open(SRC).read().splitlines()

# ---- section index -------------------------------------------------------
sections = []
for i, ln in enumerate(lines):
    m = re.match(r"^##\s+(\d+)\.\s*(.*)$", ln)
    if m:
        sections.append((i, m.group(1), m.group(2).strip(), "(NORMATIVE)" in m.group(2)))
        continue
    m = re.match(r"^###\s+(\d+\.\d+)\s*(.*)$", ln)
    if m:
        sections.append((i, m.group(1), m.group(2).strip(), "(NORMATIVE)" in ln))


def sec_of(i):
    sid, title = "preamble", None
    for (si, s, t, _) in sections:
        if si < i:
            sid, title = s, t
    return sid, title


def span(n):
    return sections[n + 1][0] if n + 1 < len(sections) else len(lines)


def clean(t):
    t = re.sub(r"^\s*[-*]\s+", "", t.strip())
    t = re.sub(r"\s+", " ", t)
    return t


surface, rules = [], []

# ---- pass A: explicit `**NORMATIVE` rules (anywhere) ---------------------
for i, ln in enumerate(lines):
    s = ln.strip()
    if s.startswith("- **NORMATIVE") or s.startswith("**NORMATIVE") \
       or re.match(r"^-\s+\*\*NORMATIVE", s):
        sid, title = sec_of(i)
        if sid == "9":                      # §9's rows ARE the surface, not rules
            continue
        rules.append({"section": sid, "section_title": title,
                      "declared_by": "line", "text": clean(ln)[:420]})

# ---- pass B: requirements inside a NORMATIVE-by-heading section ----------
LINE_MARKED = {r["section"] for r in rules}
for n, (si, sid, title, norm) in enumerate(sections):
    if not norm or sid == "9":
        continue
    for ln in lines[si + 1:span(n)]:
        s = ln.strip()
        m = re.match(r"^(\d+)\.\s+\*\*(.+?)\*\*", s)            # numbered bold requirement
        if m:
            rules.append({"section": sid, "section_title": title,
                          "declared_by": "heading+numbered",
                          "text": f"{m.group(1)}. {m.group(2)}"})
            continue
        m = re.match(r"^\d+\.\s+([a-z].*)$", s)                 # numbered plain requirement (§8)
        if m and sid == "8":
            rules.append({"section": sid, "section_title": title,
                          "declared_by": "heading+numbered", "text": m.group(1)[:420]})
            continue
        m = re.match(r"^\*\*([A-Z][^*]{2,60}?):?\*\*", s)       # bold-label requirement
        if m and sid not in LINE_MARKED and not s.startswith("**EXAMPLE"):
            rules.append({"section": sid, "section_title": title,
                          "declared_by": "heading+bold-label", "text": clean(s)[:420]})

# ---- pass C: §9's table IS the conformance surface -----------------------
for ln in lines:
    m = re.match(r"^\|\s*(?:~~)?\*{0,2}(C\d+)\*{0,2}(?:~~)?\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$", ln)
    if m:
        retired = "~~" in ln or "RETIRED" in ln
        surface.append({"id": m.group(1), "clause": m.group(2), "enforces": m.group(3),
                        "retired": retired})

# ---- dedupe + stable ids -------------------------------------------------
seen, deduped = set(), []
for r in rules:
    key = (r["section"], r["text"][:70])
    if key in seen:
        continue
    seen.add(key)
    deduped.append(r)


def sortkey(r):
    s = r["section"]
    return tuple(int(p) for p in s.split(".")) if re.match(r"^\d+(\.\d+)?$", s) else (0,)


deduped.sort(key=sortkey)
for n, r in enumerate(deduped, 1):
    r["id"] = f"R{n}"

# ---- self-tests ----------------------------------------------------------
declared_norm = {s[1] for s in sections if s[3]}
present = {r["section"] for r in deduped} | {"9"}


def satisfied(s):
    """A section declared NORMATIVE is satisfied by its own rules or by a subsection's."""
    return s in present or any(p.startswith(s + ".") for p in present)


missing = sorted(s for s in declared_norm if not satisfied(s))
surface_ids = {s["id"] for s in surface}
live_rows = {s["id"] for s in surface if not s["retired"]}


def run_tests():
    return [
        ("every heading-level NORMATIVE section yields rules, directly or through a subsection", not missing, f"missing={missing}"),
        ("§6 orchestrator requirements found",
         len([r for r in deduped if r["section"] == "6"]) >= 5,
         f"§6={len([r for r in deduped if r['section'] == '6'])}"),
        ("no mangled NORMATIVE text",
         not any(r["text"].startswith("*NORMATIVE") for r in deduped), ""),
        ("§9 surface parsed as a table", len(surface) >= 17, f"rows={len(surface)} ids={sorted(surface_ids)}"),
        ("§9 has no duplicate identifiers", len(surface_ids) == len(surface),
         f"{len(surface_ids)} ids for {len(surface)} rows"),
        ("contracts carry §7.3 per-run-value rule",
         any("per-run value" in r["text"] for r in deduped), ""),
        ("every rule has non-empty text",
         all(r["text"].strip() for r in deduped), ""),
        ("rule count exceeds the 47 in scope at v1.3", len(deduped) >= 47, f"count={len(deduped)}"),
    ]


print("=== extractor self-tests ===")
fails = 0
for name, ok, detail in run_tests():
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {detail}" if not ok else ""))
    fails += 0 if ok else 1

print(f"\n=== {len(deduped)} NORMATIVE rules | {len(surface)} surface rows "
      f"({len(live_rows)} live, {len(surface)-len(live_rows)} retired) ===")
by = {}
for r in deduped:
    by.setdefault(r["section"], []).append(r)
for s in sorted(by, key=lambda x: tuple(int(p) for p in x.split(".")) if re.match(r"^\d+(\.\d+)?$", x) else (0,)):
    print(f"\n§{s}")
    for r in by[s]:
        print(f"  {r['id']:>4} [{r['declared_by']:<20}] {r['text'][:104]}")

print("\n=== §9 surface ===")
for s in surface:
    print(f"  {s['id']:<6} -> {s['enforces']:<12} {'RETIRED' if s['retired'] else ''} {s['clause'][:70]}")

json.dump({"source": SRC, "rule_count": len(deduped),
           "surface_count": len(surface), "surface_live": sorted(live_rows),
           "rules": deduped, "surface": surface},
          open(OUT, "w"), indent=2)
print(f"\nwrote {OUT}")
sys.exit(1 if fails else 0)
