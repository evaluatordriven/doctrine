# Changelog

## 0.2.1 — 2026-11-02, ratified by the Owner

**Fixes a defect in v0.2: the doctrine kept rules the contracts had already replaced, and the chain of
command made the stale rule win.** Reported by the custody maintainers (VizH). The wording is VizH's lift
(`doctrine-lift-C`, `86d09e8`), applied to v0.2 with its source tags and Primer citations removed, since
v0.2 carries no tags and the Primer is kept out.

- **§3 seats.** The Architect decides what gets built next, what the next round is handed, and whether a
  job is ready to go to the Maker; it never scores, and never picks the version that carries forward by
  preference. The Evaluator alone scores. The Orchestrator assembles, delivers and checks the Maker's input,
  applies the pass rule, enforces the cap, escalates and keeps the record; it never chooses what an
  iteration receives or rules on readiness. Was: "Runs the loop: dispatch, feedback, bounds, the record."
  (Contracts §4, C37; proposal 0054.)
- **§3, two new paragraphs with new ids.** `D3.routing` (the Architect designs, the Orchestrator routes,
  the Evaluator alone scores; readiness is a design check, never a predicted pass) and `D3.held-out` (what
  held-out material is, and that it never goes to the Maker). (Contracts §4, §4.2, C37, C39.)
- **§4 principle 9.** The carry-forward test, not the Architect's preference, picks the version that goes
  forward, and the next round is handed the best artifact, every known defect and every known workable
  solution, each with its measurement, with held-out material filtered out. (Instrument rule 12.)
- **§5 core sequence.** "Build the Evaluator, build the Maker" becomes "have the Evaluator in place before
  the Maker produces". (Instrument A2.)
- **§5 steps 5 and 6.** Was: "send the classified shortfall back to the Maker as constraints. Nothing else
  goes back." Now the next round receives the best artifact, every known defect and every known workable
  solution with their measurements, with the held-out exclusion applied to all of it. Revisions answer only
  what the Evaluator reported. (Instrument rule 12; Contracts §4.2, C39; proposal 0055.)
- **§5 "Where the human sits".** Per-act approval is not required by default; the kickoff frame, budget and
  bounds suffice unless the job declares otherwise, and then it declares which form of approval counts. On
  novel ground, "a person stays in every turn" becomes "a job may declare closer oversight". (Contracts
  §4.2, C40; proposal 0055.)
- **§3, a second never-waived exception (Owner, ratified 2026-11-02): whoever disposes of the work does
  not judge it** (`D3.disposer-never-judges`). It follows from D5.disposition and matches custody/v1 CL1-6
  ("the approver is not an evaluator"). The Owner may still hold the Maker's seat, disclosed.
- **§10.** "This articulation" no longer describes only v0.1. "Applied to itself" records the failure:
  v0.2's checkers verified that each rule was cited below the doctrine, not that the citing text agreed.
- **Operating Instrument v1.12 → v1.13.** Three places still carried the old rule inside the Instrument,
  against its own rule 12: the sheet's *Feedback channel* line ("the Maker's only input"), A4 ("the
  classified critique and nothing else") and I4 ("classified critique only"). Each now gives the classified
  critique with rule 12's input, never held-out material.
- **Contracts v1.26.1 → v1.27.0.** §4's Owner row bars the Owner from the Evaluator's seat in a job it
  disposes of, citing the new doctrine rule. It no longer bars the Maker's seat, which DOCTRINE §3 allows
  when disclosed. The job-packet schema, `validate_job_packet`, `check_role_separation` and the fixtures
  already enforce Owner ≠ Evaluator (proposal 0028 A) and are unchanged. The rule index is unchanged, since
  the roles table is not extracted.
- **README, smallest crew.** One person plus two model families (or a model and a script that person did
  not write) can run a job; the one seat the person may not take is the Evaluator's.
- **Contracts v1.26.0 → v1.26.1, editorial.** The §11 *Implements* table adds C39 and C40, and widens C37
  and §4. §12 pins the Instrument at v1.13. The rule index is regenerated: still 86 rules, with unchanged
  dispositions. The Instrument's I24 (rule 12) now also carries D5.step.5.
- **`check_downhill.py` D10, wording.** For the rules that failed (the Orchestrator's and Architect's seats,
  step 5, where the human sits), DOCTRINE.md and its carriers must state the same terms, and neither may
  keep the replaced wording. Nine must-fail cases, including the seat-sharing rule and the Contracts' old Owner ban; run against v0.2's
  DOCTRINE.md, D10 fails nine checks.
  D8 now reads three-part doctrine versions.

**Audit of every up-citation for agreement, not only existence.** Every rule and carrier was re-read. Apart
from the items above, one disagreement was found: Contracts §4 barred the Owner from the Maker's and the
Evaluator's seats, while DOCTRINE §3 allowed any disclosed sharing but one. The Owner resolved it with the
second exception above.

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
