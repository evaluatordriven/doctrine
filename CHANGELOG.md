# Changelog

## 0.2 — 2026-11-02, ratified by the Owner

**Added `contracts/`: the machine contracts, published from the Owner's private working corpus.** An
implementation can now be tested by anyone against public law. Taken from the corpus at Contracts v1.24.0
and Operating Instrument v1.10.

Published as they were, apart from the edits listed below:

- the seven load-set files: Playbook, Quickstart, Operating Instrument, Machine Contracts, Mandate, Example,
  For Machines;
- `schemas/` (job packet, evaluator record, pass), the 43 fixtures and the mandate template;
- `EDI-RULE-INDEX.json` and the nine tools that validate packets and records, gate single rules,
  regenerate the rule index and check the folder.

**Owner decisions applied**

- **Doctrine v0.2 ratified by the Owner, 2026-11-02**, with the up-citation links added in review confirmed.
  §10 "Applied to itself" records how v0.2 was checked: by this repository's checkers, not by a reader from
  another model family.
- **`evaluator.kind` in the job packet** (optional: `person`, `model` or `script`), so a job can record
  who holds the Evaluator seat, as the Contracts §4 Evaluator row requires. Both the schema and the
  standard-library validator check it. There are two new fixtures, one that must pass and one that must
  fail; 45 fixtures in all. For Machines lists the field. It is optional for now, so existing packets still
  validate; a later version may require it.
- **Status facts move out of the doctrine**. §7's sentence on the custody record's
  candidacy and its known implementations, and §6's "the Architect's seat is not yet tested this way; that
  gap is open", now live in the README's dated status lines. The doctrine no longer has to change when an
  implementation ships or a test passes. The rule "test every seat" (D6.1) is unchanged.
- **An Evaluator seat is described by what it does and what holds it** (DOCTRINE §3).
  It replaces "two forms of the Evaluator seat". What it does: the reader (the usual form, new
  `D3.reader`), the adjudicator, the test author. What holds it: a person, a model or a script (new
  `D3.holder`), each tested by controls in every batch. The Contracts §4 Evaluator row carries both.
  Contracts v1.25.0 → v1.26.0; the rule index is unchanged at 86 rules. 67 doctrine rules, all carried.
- **The four uncarried doctrine rules are now carried by law** (Owner, accepting the recommendations):
  - D6.2 (check every instrument against a valid alternative) and D6.3 (an independent pre-read) are
    added to Instrument A2 and I2. Instrument v1.11 → v1.12.
  - D3.adjudicator and D3.test-author are added to the Contracts §4 roles table as named forms of the
    Evaluator seat. Contracts v1.24.1 → v1.25.0. The rule index is unchanged at 86 rules, because the
    roles table is not extracted as rules.

  All 65 doctrine rules are now carried, and CI passes in strict mode.
- **Citations point up (doctrine v0.2).** Every normative item in `DOCTRINE.md` has a
  stable id: 65 in all, from `D2.bar` to `D8.F6`. They are invisible HTML anchors, so the text reads as
  before. The ⟨…⟩ source tags are removed. Their job moves to *Implements* tables at the end of the
  Playbook, the Mandate (§8), the Contracts (§11) and the Instrument. Each table maps that file's own ids to
  the doctrine rules they carry, and is seeded from the v0.1 tags; rows added in review are marked for the
  Owner to confirm. Of 65 rules, 61 are carried. Four are declared in `AUTHORITY.json` as not yet carried by
  any law: D3.adjudicator, D3.test-author, D6.2 (valid alternative) and D6.3 (independent pre-read).
  Apart from the removed tags and the anchors, `DOCTRINE.md` is v0.1 word for word, except for these changes:
  - the §10 Origin paragraph is rewritten;
  - "marked ⟨practice⟩ above" is dropped;
  - existing words in §6 and §8 now link to the evidence;
  - the version line now reads v0.2;
  - §7 no longer says no product loop emits `custody/v1`: Plumbline does, and two of its records verify
    at CL1. The stranger-test status is updated to v0.9.7;
  - §10 links the custody release records at `github.com/evaluatordriven/custody` instead of the old
    address.
- **Annex B published as Mandate §7** (outcome criteria O1–O4 and the causal claim B.1.5), ratified
  2026-09-20, with its references to unpublished material removed. Mandate stubs M4.2 and M4.5 are
  added. Plumbline enforces B.1.2 (`k`, `x`), and testers can now read it.
- **`check_downhill.py` D6 is now the up-citation check**, and CI runs `--strict`, which fails while any
  declared gap is open.
- **A chain of command: `AUTHORITY.json`.** Tier 0, the Owner. Tier 1, `DOCTRINE.md`. Tier 2, the
  Playbook and the Mandate, sharing it. Tier 3, the Contracts. Tier 4, the Operating Instrument. Tier 5,
  the schemas and fixtures. Tier 6, For Machines, the Quickstart and the Example. A higher tier wins. A
  same-tier disagreement is first tested against every higher tier, nearest first, then escalated to the
  Owner. Every load-bearing markdown file names its tier in a header. For Machines' list is now a reading
  order, not an authority order; before this, it ranked the Quickstart and the Instrument above the
  Contracts, against Contracts §0 and §12. It now reads `DOCTRINE.md` first.
- **The Playbook cites Mandate M2, not M2.3–M2.4** (Owner decision). M2.3–M2.4 exist only in the
  unpublished full Mandate; the short M2 carries the same rule. Found by `check_downhill.py` D7 on its first run.
- **Mandate F1–F6 carry `DOCTRINE.md` §8's words.** F5 gains the Owner-attention signals: repeated
  approvals of the same kind, choices without a recommendation, answers that need re-explaining.
- **Two checkers, each shipped with must-fail cases:** `tools/check_authority.py` (the chain holds) and
  `tools/check_downhill.py` (every lower tier agrees with the tiers above it). Both run in CI.
- **`DOCTRINE.md` wins.** If anything else in this repository conflicts with `DOCTRINE.md`, the doctrine
  governs, and the other file is the defect, escalated to the Owner. The README, the contracts README,
  Contracts §0, For Machines (now `../DOCTRINE.md` sits above the load order) and the Playbook say so.
- **The Maker-family rule follows `DOCTRINE.md` §3.** Operating Instrument rule 2 and I14 now read: at
  least one Evaluator differs from the Maker in model family; on every dimension the Maker's family holds
  no more than half of the Evaluators; an undisclosed family is read as the Maker's. Before this, both
  barred the Maker's family from the Evaluator seat. Instrument v1.10 → v1.11. `check_role_separation.py`
  checks identity only, as before: family is not in the job packet, so this rule is not yet
  machine-checked here. custody/v1 CL2-3 checks it on the record.
- **custody/v1 governs the record's terms.** Contracts §0 states it. §10 is retitled "Retention and
  revision", so it no longer names a second "custody". Its method rules (revision, regression,
  revalidation, spread) are unchanged. Contracts v1.24.0 → v1.24.1.

**Editorial only.** None of these edits adds, removes or rewords a NORMATIVE rule. The rule index still
holds 86 in-scope rules with identical dispositions.

- Primer material is removed: attributions in Contracts §1.6–§1.7, the Instrument's provenance line and
  the Playbook's teaching references, which now point to `DOCTRINE.md`.
- References to private material are removed: the full-text annexes, proposals, evaluation records,
  publishing scripts and home-directory paths.
- Harness-specific material is removed: the Hermes skill and plugin belong to implementations.
- Ratification lines name "the Owner" rather than an internal initial.
- The corpus tools check the public file set. `check_consistency.py` and `build_manifest.py` no longer
  expect the private corpus's teaching and history files.

**Not published:** the Primer, Architecture, the change history, proposals, evaluation records, audience
notes, the full-text annexes, and the Hermes skill and plugin.

## 0.1 — 2026-10-25

Doctrine v0.1, ratified by its Owner.
