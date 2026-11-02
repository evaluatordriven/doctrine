NOT AUTHORITY. Maintainer toolchain. Do not load to run a job. `EDI-RULE-INDEX.json` is a maintainer index, not a runtime gate.

## The corpus regenerates and verifies itself

Two scripts in `tools/` are the corpus's own gate, and both are pure standard library so a fresh clone needs no
setup:

| Script | What it does |
|---|---|
| `check_consistency.py` | structure, §-references, §9 contiguity, **and** `extract_rules.py` → `classify_rules.py` leaving the Contracts and `EDI-RULE-INDEX.json` byte-identical — §12's "regenerate the derived artifacts in the same pass" made mechanical — then the manifest |
| `build_manifest.py` | builds or `--verify`s `MANIFEST.sha256` against this tree; root files are named **and an unlisted root file fails the build** (a deletion shows, and a root addition cannot hide), class folders are walked (a grouped addition shows); the announced count is asserted against the row count |

This folder clones and verifies without a single credential.

**One lesson this repo bought immediately.** `tools/classify_rules.py` was the 56-rule table from the v1.4 era
while the Contracts carried 64 rules: the published tool could not classify the published document, and the local
check passed only because a scratch copy in a temp directory held the newer table. The corpus now carries the
64-rule classifier, and `check_consistency.py` refuses to report an unchanged-file comparison when the writer
crashed before writing — a PASS over a comparison that never ran is how a broken regeneration passes for a
working one.

# EDI-tools — the corpus's own generator

Retained because §12 requires the derived artifacts to be regenerated in the same pass as a change, and
a corpus that mandates regeneration but does not ship the generator cannot be revised by a successor.

Run from the repo root: `python3`

| Script | Does |
|--------|------|
| `extract_rules.py` | Rule inventory from the Contracts at the corpus root, plus §9's conformance surface parsed from its table. Runs eight self-tests before emitting — **do not trust its output unless they pass** |
| `classify_rules.py` | Owns §9's *State at vX* block (**computed, never typed**) and `EDI-RULE-INDEX.json`. Asserts the invariant on every run: every in-scope rule has exactly one disposition; every `LINE` names a live §9 row; every live §9 row is claimed by at least one rule |
| `check_consistency.py` | The corpus's self-check: structure, §-references, §9 contiguity, the derived artifacts regenerating byte-identically, and the manifest. Run before every commit |
| `build_manifest.py` | Builds or `--verify`s `MANIFEST.sha256`. Root files are named and an unlisted root file fails the build; class folders are walked; the announced count is asserted, never derived from rendered text |

```
tools/extract_rules.py    [contracts.md] [out.json]
tools/classify_rules.py   [contracts.md] [rules.json] [outdir]
```

Both default to the Contracts in this folder, so a version bump is: edit the Contracts, run
`extract_rules.py`, extend the authored disposition table in `classify_rules.py`, run it, publish.

## Why these exist

A hand-rolled extractor omits what it cannot match and reports a count nobody diffs. Four times now:

1. Plumbline's checklist carried 12 of §9's 14 lines — instrument retention (C13) and revision
   control (C14) were absent, so no audit could find a §10 violation.
2. PARAD's `rules.json` carried 26 of 29 clauses — the label group `[A-Z0-9 \-]+?` is uppercase-only,
   so P8/P19/P20 were dropped silently.
3. The first extractor written for this corpus found 31 rules and missed every section declared
   NORMATIVE by its *heading* — §6 alone carried five requirements.
4. **Regenerating the checklist from the Contracts silently dropped the authored `why` field and the
   compound `section` refs.** The checklist is *derived plus annotated*, not purely derived.
   "Regenerate, never hand-edit" is correct for a purely derived artifact and wrong for this one. Patch
   it.
5. **Patch-only drifts the other way, and slower to notice.** `patch_checklist.py` added lines to a
   checklist that was already behind, so by 2026-09-20 Plumbline's copy carried 17 lines and declared
   `contracts_version: 1.2` while the Contracts had reached `C1`–`C27` at v1.8 — ten lines missing, two
   vocabulary renames behind, and an inventory reading 47 in scope / 23 uncovered against a true 64 / 0.
   The failure is structural, not careless: a tool that only ever *adds* cannot see what it never had, and
   nothing compared its output to the source. A rebuild derives the skeleton from §9 and
   re-attaches annotations by identifier, so the count is asserted rather than trusted, and a clause whose
   text changed is visible in the diff as a changed line rather than an absent one.
6. **A named list makes a deletion visible and an addition invisible.** `build_manifest.py` stated that asymmetry
   in its own docstring, and the case it missed was the one it named: `EDI-OPERATING-INSTRUMENT.md` sat at the
   corpus root, in force, indexed as a root document — and outside `ROOT_FILES`, so nothing hashed it. `--verify`
   reported *"all files match the manifest exactly"* and CI stayed green through two commits, a version bump and
   the ratification of the instrument itself, because **a pass over a file that was never looked at is not
   coverage.** Rule 10 requires the instrument kept hashed; the corpus's own instrument was not, and its hash was
   recorded nowhere. Two repairs, same lesson: the walk is **fail-loud on an unlisted root file**, and the count
   the tool *announces* is asserted against its own row count — the same build announced *"manifest written: 109
   files"* for a 110-row manifest, because the figure a reader quotes was derived from rendered text instead of
   from the rows just hashed.

## The rule

**A generator is tested against a known count before its output is used, and an artifact that carries
authored content is rebuilt from its source with the annotations re-attached — not regenerated wholesale,
and not patched indefinitely.** `extract_rules.py` asserts its own correctness —
every heading-level NORMATIVE section must yield rules — because without that assertion it fails
silently in exactly the way it is meant to detect. A checklist rebuild asserts that it parsed every §9
line before writing, so a line it cannot match is an error rather than an omission.

## What changed at v1.4, and why it mattered

- `extract_rules.py` v2 read a **scratch copy of an earlier version**, by absolute path outside this
  folder, and asserted a **14-line checkbox surface** from the v1.0 layout. v1.3 rewrote §9 as a table,
  so the surface parse found nothing and the assertion could never fail — a self-test that had stopped
  testing. v3 reads the Contracts beside it, parses §9's table, drops `EXAMPLE` labels (an example is
  never a requirement, §0), and checks structure rather than one version's counts.
- `classify_rules.py` v1 was a one-shot transition script (it built v1.3 out of v1.2, with the counts
  hard-coded and the state block typed by hand). v2 is the steady-state classifier described above:
  the disposition table is authored and reviewable row by row, and everything else is computed.
- **`C`-ids are stable and never renumbered. `R`-ids are positional, so they are version-scoped** — the
  index records the Contracts version and sha256 it was generated from. Cite `C`-ids in audits.

## Job packet tools (proposals 0018 / 0020)

```bash
python3 tools/validate_job_packet.py schemas/fixtures/example-job-packet.json
python3 tools/check_terminal_state.py --packet schemas/fixtures/example-job-packet.json
python3 tools/check_role_separation.py --packet schemas/fixtures/example-job-packet.json
```

Schema: `schemas/job-packet.schema.json`. Install `jsonschema` for full draft validation; stdlib structural check always runs.


## Job packet consistency gate (0021)

`python3 tools/check_consistency.py` enumerates the fixture set and asserts each expectation. **The gate's
enumeration is authoritative; the list below is kept in step and the count is stated so drift is visible.**
Ten fixtures:

- `schemas/fixtures/example-job-packet.json` → OK
- `schemas/fixtures/mvi-job-packet.json` → OK
- `schemas/fixtures/bad-unratified-accept.json` → must FAIL
- `schemas/fixtures/bad-unratified-filled.json` → must FAIL
- `schemas/fixtures/bad-readings-rejected.json` → must FAIL
- `schemas/fixtures/bad-census-on-scored.json` → must FAIL
- `schemas/fixtures/bad-readings-empty-bounds.json` → must FAIL
- `schemas/fixtures/bad-entry-b-no-reads.json` → must FAIL
- `schemas/fixtures/bad-mode-absent.json` → must FAIL *(0032: `mode` is required; absence must not default to `scored`)*
- `schemas/fixtures/bad-owner-evaluator-object.json` → must FAIL *(0032: the Owner cannot hold the Evaluator seat in object shape either)*

The gate also checks the Instrument's machine extract: `I`-ids sequential and unique, the extract covers A1–A5,
R1–R4 and rules 1–12, and **every `Cites` value resolves to text in `EDI-OPERATING-INSTRUMENT.md`** (0033 clause 4).

## Templates (0040)

`schemas/templates/mandate-skeleton.md` is a starting shape for a Principal-authored mandate.
**Not authority. Not a fixture. Not a record.** The fixture gate does not run it. The packet key it
fills is `mandate_ref.doc` plus `mandate_ref.version`.

## Evaluator record (0041)

`tools/validate_evaluator_record.py` checks the shape of a scored Evaluator record. A pass is not C8. The Orchestrator stamps `instrument_in_force` after the Evaluator returns; the Evaluator does not emit the hashes. `defect: saw_gt` is a name, not a failed file — the Orchestrator exits `needs_owner`.



