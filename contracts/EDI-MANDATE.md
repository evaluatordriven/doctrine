# E-DI — Mandate

**Authority:** tier 2 in `../AUTHORITY.json` — outranked by tiers 0–1; conflicts follow its conflict rule.

**Status:** **IN FORCE** — Owner-ratified frame (2026-09-20), **short form** 2026-09-23.  
**Class:** Weight-bearing. What the E-DI *system* must and must not do.  
**Full text (annexes, provenance, clause labels):** held in the private working corpus and not published; not required to run a job or to verify an implementation.

This page is the **frame**. Seats and program clarity live in **`EDI-PLAYBOOK.md`**. Job form lives in **`EDI-OPERATING-INSTRUMENT.md`**. Software rules live in **`EDI-MACHINE-CONTRACTS.md`**.

---

## 1. The problem (Owner)

**P1.** People are often poor at delegating — to other people, and now to AI agents. Generation is cheap. We need a way to make sure delegation produces **valuable outputs that are fit for purpose**.

**P2.** Delegation fails when done/good are unclear, outputs cannot be checked fairly, the worker lacks skill or resources, or feedback is late or useless. Work is often graded by the Maker or by judges who do not know the **Buyer’s jobs-to-be-done, pains, and gains**, and do not know what **masterful** work looks like. That path produces something idiotic.

**P3.** What we want: a system of delegation that handles poor quality and misalignment by catching them **early** and correcting them through **consistent evaluation**, **actionable feedback**, **resourceful generation**, and **well-managed iteration**. **That is E-DI.**

---

## 2. What E-DI must deliver (M1–M8)

One line each. Detail and enforcement lines: full Mandate + Machine Contracts.

| ID | Name | In plain words |
|----|------|----------------|
| **M1** | Identify early | Done and good exist **before** the first draft. Misalignment is found **before** accept. |
| **M2** | Consistent evaluation | Same standard, same way, every time. Maker never grades own final work. Keep the instrument that judged with the artifact. |
| **M3** | Actionable feedback | Say **how** it falls short (with proof). Optional insight OK; **fabricated remedies are worse than none**. Feedback must be able to change the next version — or do not loop. |
| **M4** | Resourceful generation | The Maker can actually act on the judgment. Capability gaps **escalate**, not endless retry. Carry best work forward; Owner decides hard trades. |
| **M5** | Well-managed iteration | Finite **cap** and **budget**. Stop in a named way. Keep records so a stranger can reconstruct the decision. Feedback while work can still change. |
| **M6** | Escalate without interrogation | Agent answers what is findable. Values, priority, risk, Buyer intent → **Owner**, with what was tried. |
| **M7** | Proportionality | Instrument size matches the job. Smaller instrument is a recorded choice — **not** an excuse to skip must-ask rules. |
| **M8** | Operating level | Declare the ladder rung (L1 do this … L5 act). Ladder changes **who decides**, not what must be supplied. |

**Terminal states (machine alphabet):** `accepted` · `needs_owner` · `rejected`.  
Outcomes may be recorded beside the state (see Instrument / Machine Contracts).

---

## 3. What E-DI does not do (X)

| ID | Exclusion |
|----|-----------|
| **X1** | Does **not** set values — the **Owner** does. |
| **X2** | Does **not** set priority or risk appetite — the **Owner** does. |
| **X3** | Does **not** pick voice/tone/authorial “good” — the **Owner** does (then E-DI can score against that standard). |
| **X4** | Does **not** replace Owner override. Verdict stays as the loop produced it; Owner decision is a **disposition beside** it — **never a rewrite**. |

---

## 4. How we would know it failed (F)

| ID | Failure signal |
|----|----------------|
| **F1** | Work ships with no Buyer in the record who asked for it. |
| **F2** | Judging costs more than the errors it catches (on a fair comparison). |
| **F3** | Work scored above the bar is later rejected by the named Buyer or Specialist, and the record cannot say which dimension failed. |
| **F4** | Two honest runs of the same setup disagree by more than the instrument's normal variation. |
| **F5** | The Owner is asked questions the system could have answered itself. Or the Owner is forced to carry an attention cost the system could have spared: repeated approvals of the same kind, choices without a recommendation, answers that need re-explaining. |
| **F6** | Accepted work cannot be reconstructed from its records. |

---

## 5. How to use this page

- **Running a normal job:** read this short frame if you change system limits; otherwise Playbook + Instrument are enough to start.  
- **Auditing outcomes:** §7 below carries the outcome criteria (Annex B, O1–O4). The dimension set (Annex A) and the full clause text are held in the private working corpus and not published; neither is required to run a job or to verify an implementation.
- **Cite:** `Mandate §1 P2`, `Mandate §3 X4`, `Mandate §4 F6` (stable IDs). Full file keeps the long clause text.

---

## 6. Citation stubs

These stubs are the weight-bearing meaning of ids the other six files cite. The full file is not required to run a job. Seat names are Playbook §6. This file does not have a §Roles.

| ID | Meaning |
|----|---------|
| M1.1 | Done and good exist before the first generation. A definition written after seeing a draft is an anchor on the draft. |
| M3.6 | An influence channel exists — feedback the next generation can consume — or the loop is not run. |
| M4.2 | Capability gaps escalate rather than iterate. A defect above the Maker's capability is the Owner's question, not another regeneration (Contracts §4.1, §6). |
| M4.3 | The loop carries the best parts forward (Instrument rule 12). A trade is the Owner's. |
| M4.5 | Resourcefulness is demonstrated, not asserted: the next evaluation shows the named class resolved, disappeared, or persisted (Contracts §10.2). |
| M5.2 | Terminal states are three. Outcomes recorded beside them: `accepted`, `census`, `needs_owner`, `rejected`, `no_observation`, `no_artifact`. |
| M5.5 | Feedback arrives while the work can still change. The job records the cycle bound. |

---

## 7. Outcome criteria for P1–P3 (Annex B)
Annex status. RATIFIED in full by the Owner on 2026-09-20, with small edits and no changes of substance; published here 2026-11-02, from the full Mandate's §8, with references to unpublished material removed. The criterion ids O1–O4 and the clause ids B.1.1–B.4.3 are unchanged. It sets no thresholds: k, x, the disposition requirement and the bounds remain the Owner's to supply per job.
Why it exists. §1 says what E-DI is for (P1–P3) and §4 says how we would know it failed. Neither said what observation would show the purpose achieved — so process compliance could not be told apart from success, and a reviewer said exactly that. This section supplies the missing half. §4 and this section are one instrument: each criterion is the positive form of a failure condition (F1–F6), and each names the record that carries its observation.
Authority. Contracts §6 (every iteration persisted, so a terminal decision is reconstructable), §10 (retention), §1.6 (versioned ground truth), §10.6 (declared spread), and §2 M1–M5 with §4 F1–F6 above.
The rule this section obeys. A criterion counts only if the record carries its observation — no criterion may rest on the Owner's memory, on a reviewer's impression, or on a number nobody can reproduce. Where a criterion cannot meet that bar today, it says so instead of pretending.
### B.1 Program-level criteria — what would show the purpose achieved
### B.1.1 O1 — The accepted artifact was used for its purpose
Asserts: delegation produced something the buyer put to work (P1's "valuable outputs"). Observation: the accepted artifact's disposition — used as intended, used after amendment, shelved, or replaced. Record: the buyer's disposition recorded with the job — a disposition, not a verdict (X4: the disposition is recorded alongside the verdict, never a rewriting of it). Measurable today: yes, where the buyer records it. Today most do not, so the first job of this criterion is to make the disposition a must-ask value. Fails as: F1 (shipped and wanted by nobody).
### B.1.2 O2 — Misalignment is found early, in the loop, not by a stranger
Asserts: the "identifying them early" half of P3. Observation: the iteration and the cost at which the first P0/P1 violation was recorded, per job. Record: per-iteration artifacts, verdicts and costs (Contracts §6, C12/C16). Criterion: the job declares its own bound before the run — "material misalignment is found by iteration ≤ k, or within x% of budget" — and the audit reports the rate of jobs that met their declared bound. Measurable today: yes — the record already carries iteration counts and cost; only the declared bound is missing, and it is a must-ask value. Fails as: F3, F5; and the "found only after the whole budget was spent" case a reviewer raised against M1's wording.
### B.1.3 O3 — Correction is attributed, not assumed — or it is escalated on the record
Asserts: the "correcting them" half of P3. Observation: per violation class, across consecutive runs — resolved beyond the channel's declared spread, disappeared, persisted, or escalated as a capability gap. Record: the per-dimension, per-class comparison of Contracts §10.2, with the channel spread of §10.6 (C14, C22). Criterion: a class that disappears only inside the spread is not a correction; a class routed to the Owner as a capability gap (M4.2, C25) is recorded as an escalation, which is a different outcome from correction and neither is counted as the other. Measurable today: yes, where the spread has been measured — that is C22's job, and it is the reason C22 came before this section. Fails as: F4; and the conflation of "corrected", "apparently disappeared" and "escalated" that a reviewer named against M4.5.
### B.1.4 O4 — What a job costs, against a comparator that exists
Asserts: proportionality — the judgement is worth what it costs (M7). Observation: Evaluator cost and elapsed time per accepted artifact, and per rejected artifact — the second is where waste shows. Record: the job's recorded budget and costs (Contracts §3, C5). Criterion: cost is reported across a body of jobs, as a rate. It becomes a criterion only with a comparator: the same class of work done without E-DI, or a prior period with different settings. Until a comparator exists, this criterion is reported and not judged. Measurable today: half — cost is recorded; the comparator does not exist. Fails as: F2 (judgements cost more than the errors they prevent). F2 is a comparison; without a comparator it cannot be evaluated, which is why F2 is written the way it is.
### B.1.5 The causal claim, stated as an experiment rather than a criterion
P1 asserts that people and agents need a way to ensure delegation produces valuable outputs, and E-DI claims to be that way. That is a comparative causal claim, and no criterion here establishes it. What would: paired jobs of the same class, one run with E-DI and one without, on a declared comparison — same buyer, same standard, same class of work — reporting O1–O3 for each arm and the spread. Until that experiment is run at least once, "E-DI improves delegation outcomes" is this mandate's hypothesis, and this document says so rather than borrowing authority it has not earned.
### B.2 Mechanism-level observations — one observable per mechanism, all record-carried
M1 identify early — in the record: the definition of done and good, the thresholds, and the frame's authorization all pre-date the first generation, with timestamps. Fails as F3.
M2 consistent evaluation — one rubric version and one instrument identity across the job's runs, with each channel's spread declared and re-measured on a trigger. Fails as F4.
M3 actionable feedback — every violation carries a class and an observation; remedies appear only where insights exist (Contracts §5) — an empty or fabricated remedy is the defect, not its absence. Fails as F3.
M4 resourceful generation — the Maker is a recorded choice; the named violation classes resolve beyond spread, or escalate as capability gaps; "billed rerolls" are counted, and the count is the waste metric. Fails as F2.
M5 well-managed iteration — every job ends in a named terminal state, and a stranger can reconstruct the decision from the records without re-running the loop. Fails as F6.
### B.3 How this section and §4 fit together
§4 is the conditions under which E-DI has failed. B.1–B.2 are the observations that would show it working. Each failure condition now has a positive counterpart, so a job can report either side: the negations are the F-list, the positives are O1–O4 and the mechanism list. Neither is authoritative about the other; together they are one instrument, and a job that reports neither is reporting nothing.
### B.4 Cadence, and who measures
B.4.1 The audit is a scheduled, deterministic job that reads the job records, not the hooks and not anyone's recollection, because hooks are fail-open. B.4.2 It reports, across a body of jobs: O1's disposition rate, O2's met-bound rate, O3's class-attribution table, O4's cost per accepted artifact, and the billed-reroll count. Silent when healthy; a report only when a rate moves. B.4.3 The Owner reads rates, not individual judgements. Any rate that fails its declared bound is a frame question for him (Contracts §1.7), not a score for an agent to compute.

---

## 8. Implements

This table cites **up**, to the rules of `../DOCTRINE.md` it carries (doctrine IDs, `D…`). It belongs to this file: when an id here changes, update the table in the same commit. `../tools/check_downhill.py` checks that every id here exists, every doctrine id it names exists, and every doctrine rule is carried somewhere. Basis: *v0.1 tag* means the doctrine's own v0.1 citation named this id; *added 2026-11-02* means it was added in review and confirmed by the Owner on 2026-11-02.

| This file | Carries | Basis |
|---|---|---|
| `F1` | D8.F1 | v0.1 tag |
| `F2` | D8.F2 | v0.1 tag |
| `F3` | D8.F3 | v0.1 tag |
| `F4` | D8.F4 | v0.1 tag |
| `F5` | D4.11, D8.F5 | v0.1 tag |
| `F6` | D4.12, D7.record, D8.F6 | v0.1 tag |
| `M1` | D4.1, D5.move.1 | mixed: D4.1 tag, D5.move.1 added |
| `M1.1` | D4.1 | v0.1 tag |
| `M2` | D3.maker-never-judges, D4.3, D4.12, D5.move.3 | mixed: D3.maker-never-judges added, D4.3 tag, D4.12 tag, D5.move.3 added |
| `M3` | D4.7 | v0.1 tag |
| `M3.6` | D4.8 | v0.1 tag |
| `M4` | D4.8 | v0.1 tag |
| `M4.3` | D4.9 | added 2026-11-02 |
| `M5` | D4.10, D4.12, D5.move.4, D7.record | mixed: D4.10 tag, D4.12 tag, D5.move.4 added, D7.record tag |
| `M5.2` | D5.exit.accepted, D5.exit.needs-owner, D5.exit.rejected, D5.outcome.census, D5.outcome.no-observation, D5.outcome.no-artifact | v0.1 tag |
| `M6` | D4.11 | v0.1 tag |
| `M7` | D4.13 | v0.1 tag |
| `M8` | D4.14 | v0.1 tag |
| `X1` | D2.frame | v0.1 tag |
| `X2` | D2.frame | v0.1 tag |
| `X3` | D2.frame | v0.1 tag |
| `X4` | D3.Owner, D5.disposition | v0.1 tag |

---

## 9. Revision note

**2026-11-02 (publication):** Annex B published as §7; M4.2 and M4.5 stubs added; up-citations to `../DOCTRINE.md` in §8. **Owner ratification:** **2026-09-24** — the Owner ratified this short front as the weight-bearing frame (P/M/X/F meaning unchanged; compression only). **2026-11-02:** F1–F6 now carry `../DOCTRINE.md` §8's words, which win; F5 gains the Owner-attention signals.

**Short form 2026-09-23.** Full text held in the private working corpus and not published.

**Original ratification:** 2026-09-20 (clause-by-clause). Later M4.3 / M5.2 outcome extensions 2026-09-22 — see full file.
