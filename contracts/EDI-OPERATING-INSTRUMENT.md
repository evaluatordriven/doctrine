# E-DI — the operating instrument (the handoff sheet)

**Authority:** tier 4 in `../AUTHORITY.json` — outranked by tiers 0–3; conflicts follow its conflict rule.

**Sheet** (print it, fill it) · **Verso** (the two entries and the rules) · *v1.13 — 2026-11-02 (DOCTRINE v0.2.1: what the Maker is given follows rule 12 in the sheet's Feedback channel line, A4 and I4, which had kept "only" and "nothing else"). v1.12 — 2026-11-02 (Owner decision: A2 and I2 add the valid-alternative run and the independent pre-read, carrying DOCTRINE D6.2 and D6.3). v1.11 — 2026-11-02 (Owner decision: the Maker-family rule follows `../DOCTRINE.md` §3 — rule 2 and I14 amended; public derivative, Primer provenance removed). v1.10 — 2026-10-29 (0055 as amended: never held-out material on the Maker channel; per-act approval optional/job-declared). v1.9 — 2026-10-29 (0054: Architect decides what is built / what each iteration is given / readiness for the Maker; Evaluator judges; Orchestrator routes).
**Instrument in force:** this instrument — **ratified by the Owner on 2026-09-22 and operable**; the **frame** is `EDI-MANDATE.md`, in force since 2026-09-20 (Contracts §1.7). One real handoff run has been made on it (the JEV skill job, Entry A, commissioned and accepted). A record states the version and hash it ran under; the rehearsal caveat no longer applies.

---

## Profiles (`instrument_profile`)

Record on the job packet: **`full`** or **`mvi`**.

| Profile | When | What is required |
|---------|------|------------------|
| **`full`** | Anything that will be revised, compared, or attributed across runs. Any stakes, low included — a low-stakes artifact nobody will look at twice is where drift goes unmeasured | Full sheet + full schema |
| **`mvi`** | One judgement, no revision comparison. Any stakes, high included — a contract read once, a one-way decision, a specification signed off once | MVI field set below |

**M7.3 still holds:** MVI never licenses omission of the terminal-state alphabet, Maker≠Evaluator on final grade, no silent defaults for fields that remain on the profile, or disposition-beside-verdict.

`mvi` is a **narrower** profile, not a weaker one. The terminal-state alphabet, Maker ≠ Evaluator on the final grade, no silent defaults on any field the profile keeps, and disposition-beside-verdict all still hold (M7.3). What it does not carry is cross-run attribution machinery.

### MVI required fields

1. Entry A|B  
2. Job name + one-sentence done  
3. Artifact pointer  
4. Buyer  
5. Maker identity  
6. Evaluator identity — required, and not the Owner.  
7. Standard in one line + version/hash if any  
8. Cap (finite) + `budget` (any stated unit, including wall-clock, carried in the packet’s `budget` key)  
9. Pass rule — on a scored job this means all of `T_accept`, `T_dim`, `T_reject` — **or** `mode: readings`  
10. Human seat / escalation  
11. Terminal state + notes at end  
12. `mode` — `scored` or `readings`. No default. `scored` only if a Specialist is named at the outset.  

**Deferred on MVI** (absent or N/A — not silently defaulted): multi-row ground-truth hardness table, full control-run N, spread declaration, full escalation class matrix, Level ladder climb audit. **Revision comparisons** elevate to `full`.

### MVI sheet (print)

Use the same vocabulary as the full sheet; label the packet `instrument_profile: mvi`. Fill only the MVI required fields above.


# THE SHEET

**Above the line — fill it before you delegate.**  
**Entry A — before first generation:** job packet MUST validate against `schemas/job-packet.schema.json` (`python3 tools/validate_job_packet.py …`). Failure → stop and ask; do not generate.

| | |
|---|---|
| **Entry** — **commissioned** (not yet made; verso Entry A) or **retrofit** (exists; verso Entry B) | |
| **Job** — **one yardstick per job**: one artifact, one pass rule, one record, one terminal state. Two artifacts is two jobs. Name the unit — file, module, declared feature, or commit — and where a contract spans files, name its anchor and its span. A product or a whole repository may be the unit, **if the pass rule is writable at that level** — the failure mode is naming a repository and then scoring one file. | |
| **Mode** — `scored` (a Specialist is named at the outset, so a bar exists and thresholds are supplied) **or** `readings` (no Specialist named, no thresholds, no numbers; the findings are the output). No default. | |
| **Artifact under test** — path · commit · the surface judged | |
| **Maker** — who produced it, engine and version as the code or config carries it; *unrecoverable* is a finding, not a blank; **and the task classes that engine has been shown to perform, with the run that shows it.** | |
| **Buyer** — whose problem, and what "done" means *in their words* | |
| **Specialist** — who holds the craft standard | |
| **Ground truth** — one row per reference: source · version · hardness | `INVARIANT` / `DOCUMENT` / `PRIOR` |
| **The instrument** — rubric and runner, written and frozen before it judges anything, and hashed | |
| **Evaluator validated against** — the case it must fail | |
| **Feedback channel** — the written, classified critique, given to the Maker with rule 12's input (the best artifact, every known defect and every known workable solution, each with its measurement); never held-out material (Contracts §4.2) | |
| **Bounds** — cap ___ (`generation 0` = the artifact as it stands) · cap counts ___ *(generations \| regenerations)* · budget ___ *(unit stated)* · cost of observation authorized ___ · `T_accept` ___ / `T_dim` ___ / `T_reject` ___ on scale ___ *(only where scoring is licensed: Entry A, and Entry B with a Specialist)* | |
| **Human seat** — which verdicts escalate · **escalation route** — to whom · channel · by when | |
| **Level** — at ___ *(one rung; the rung names who decides)* | L1 say · L2 report · L3 recommend · L4 decide · L5 act |
| **Evaluator** — the seat that judges; who or what runs the instrument · **samples** — readings and spread; **say when a reference is deterministic** (identical readings are determinism, not agreement) | |
| **Resources** — people · access · budget · time · **your availability** | |
| **Next look** — we look on ___ · you ping me if ___ | |
| **Provenance** — the four **execution** seats: Architect · Evaluator · Maker · Orchestrator *(Owner, Buyer, and Specialist are recorded in their own rows above; the full seat set is seven — Playbook §6, Contracts §4)*. One party holding two: say so. The Architect decides what is built, what each iteration is given and when the job is ready for the Maker; the Evaluator judges what was built; the Orchestrator routes (Contracts §4). Where the Orchestrator holds the Architect seat, say so. Where one party is both Evaluator and Orchestrator the record has no independent authority: say so, and the compensating control is an independent re-run of the frozen instrument — required, not optional. | |

**No field is complete until it passes its test.** *Buyer:* the done-rule in their words — a document may carry it if it is quoted and versioned, and the holder is still escalated. *Specialist:* the same, and an improvised profile is labelled and escalated. *Human seat:* a named person, a channel, a clock. If this job requires per-act approval beyond kickoff bounds, name the form and channel on the sheet (standing grant, acting-channel yes, or allowed relay); default is none (Contracts §4.2). *Escalation:* the question, what was tried, why no observable answer exists, and the options with a
recommendation. *Level by consequence:* L1–L2 reversible, unobserved · L3–L4 visible or costly to undo. With no reachable
Buyer or Specialist the dimension set can only be authored by the Orchestrator — **declared, and escalated.**

**A blank line above means you are not ready to delegate. That is the sheet working.**

**↓ Below the line — the Maker, at run start.** The Maker says back the win and the done-rule; the Orchestrator
adjudicates. A difference from the sheet is the first iteration's work, not a failure.

**A recommendation, not a rule, for the Owner to set:** the top rung is for acts, not for things that ship to
users. That is an Owner value; the sheet does not decide it.

---

# THE VERSO

## Entry A — commissioned: the work does not exist yet

*The standard exists before the artifact. That is the whole difference between the entries, and everything else
follows from it.*

- **A1 — Declare the frame first, and in the order the sheet lists.** Buyer, Specialist, ground truth with its
  hardness, the Evaluator, the bounds. Nothing is generated until every must-ask is supplied — and if one cannot
  be *asked*, the run stops here rather than being defaulted.
- **A2 — Write the Evaluator, show it failing, freeze it.** The bad case comes first: a deliberately wrong
  artifact the instrument must catch. Then hash the rubric. Blindness here is **structural** — the standard
  cannot have been tuned to an artifact that does not exist yet. Before it scores anything, run it on a correct solution built differently from the one its author had in mind: an instrument that fails a valid alternative is measuring the author's design, not the bar. Then an adjudicator who did not write the runbook or the scorer reads both against the bar; where they and the bar differ, the bar governs.
- **A3 — The Maker says the win and the done-rule back, in their own words, before generating.** This step exists
  only here. It is the cheapest defect filter in the whole instrument, and it is unavailable in retrofit because
  the Maker has already acted.
- **A4 — Generate and judge in the loop:** observe through a channel the Maker does not control, classify every
  violation into one of rule 4's four locators (`artifact_missed_standard`, `standard_moved`, `dimension_unauthorized`, `frame_at_fault`). Do not grade it. Hand the Maker the classified critique with rule 12's input, never held-out material; revise or stop.
- **A5 — Keep the instrument that accepted the work.** The artifact, its rubric, its ground-truth version and the
  **Evaluator identity** travel together, so a later reader can tell what standard a decision was made against.

**What A buys that B cannot: the failure never reaches the buyer.** B finds what is wrong with what exists; A
prevents what would have been wrong from existing. **What A cannot do that B can:** notice that the frame itself is
wrong. A blind loop executes a bad standard flawlessly — which is why the frame is ratified by the Owner, the
Specialist calibrates it, and the escalation path exists.

**Entry is decided by the artifact, not by intent.** If the standard is written before anything is made, this is
commissioned work. If an artifact already exists — even one nobody planned to evaluate — it is retrofit, including
the case where "generation 0" turns out to be something already live.

## Entry B — retrofit: the work already exists

*Any artifact already made, including one people are using. You cannot re-judge the past; you can only fix the
instrument and run it forward.*

**In a retrofit census the actor is the Orchestrator, until a fix job starts.**

- **R1 — Collect the artifact's own standard, and do not judge yet.** Its docs, tests, published claims,
  interfaces, contracts. For existing work this is the **best ground truth available**: it predates the
  evaluation, so it cannot have been calibrated to it. Hardness is usually `DOCUMENT`. Where the artifact's own documents contradict each other, report the contradiction; do not resolve it by choosing one.
- **R2 — Declare the frame you would hold it to now.** Buyer, Specialist, dimensions, thresholds — plus
  **frozen by circumstance**: the platform, the language or the contract, the sunk decision. That line is what makes
  "the smallest next change" a recommendation instead of a wish.
- **R3 — Freeze and hash the rubric before any read that could reveal a defect.** This is the retrofit's
  substitute for blindness: you cannot be blind to an answer that already exists, so you substitute **declaration
  order**. R1's collection of the standard is not a read that reveals a defect, and any read that is — a scan of the
  code, a test run, a `git log` — comes after the freeze. **The record states which reads preceded the freeze**, as
  a required line and not a footnote, and a reader who has not seen the observations re-runs the frozen instrument
  before anything rests on the result. The freeze records the circumstances as well as the rubric — the platform, the interpreter, the contract in force, and the decisions already sunk: in a retrofit they are part of the instrument, and a reader who does not hold them is not holding what you held. **Where the observation environment differs from the artifact's declared one, the record states it as a limit of the record — never as a violation.**
- **R4 — The past gets a census, not a verdict.** Generation 0 is the artifact as it stands. The first pass
  produces findings; the thresholds apply **forward**. Any fix is a **new job with its own Evaluator**. **Never
  discard what is in service** — the verdict stands and the disposition is the Owner's.
- **The instrument must be shown failing before it judges anything.** If generation 0 is itself the failure — a
  named dimension below its floor for a named reason — that satisfies the requirement; otherwise inject a synthetic
  bad case. **Retrofit form: a named dimension read other than *conforms*, with a quoted reason — or, where scoring
  is licensed, one scored below its floor. An injected case is used only when neither is available.** This is B's
  rule; A carries the same practice as a step. **The model that serves the seat is shown failing too:**
  it must be shown to fail the artifact class it judges, on the artifact in hand or on a control of the same
  class — a model that cannot fail what it judges cannot hold the seat.
- **The premium output: claim-versus-reality.** Rules documented but not implemented, and behaviour implemented
  but not documented. For existing work this is worth more than a score: the artifact is contradicting itself, and
  it can be corrected without relitigating design.
- **The Maker may be unrecoverable** — record that. It caps what can be attributed, not whether the work can be
  evaluated.
- **A blank bound, or an unaskable must-ask, stops generation — not R1–R4.** The census is the zero-cost half: it
  generates nothing and mutates nothing, and a missing value is recorded and escalated rather than invented.

## Readings — and when scoring is allowed

**With no Specialist named at the outset, a job returns readings only** — *conforms*, *does not conform*, *unobserved*
— and never numbers. A score asserts standing against a bar, and there is no bar yet. That is not a consolation
prize: **a reading-only census maps the shape of the asset, and the shape is evidence toward the standard that will
be written.** The map may change what the standard turns out to be.

**With a Specialist named at the outset, the same job may also score**, because the bar exists to be measured
against. **"At the outset" is load-bearing**: a Specialist named after the readings are in does not license scoring,
or the standard would be fitted to the results it is meant to judge.

Either way the readings stand on their quotations, and a dimension with no reading forces `needs_owner`.

## Exits

These six names are **outcomes**. Terminal state is only `accepted`, `needs_owner`, or `rejected`. Pairing is Contracts §2. This sheet does not add a state.

- **accepted** — passed the rule. A readings-only job: every readable dimension conforms.
- **rejected** — below the reject floor, which needs a floor: a job with no scoring may not produce it. **If the artifact is not yet in service, it is discarded; nothing escalates.**
- **needs_owner** — failed but at or above the floor, or the cap reached without a pass. **This is the exit that escalates**; the **highest-scoring version of the work** goes to the Owner, never to the bin.
- **census** — a readings-only job in which **every readable dimension conforms**; its findings are the output. A census that finds a **non-conformance** exits `needs_owner`: the shortfall is recorded with its quotation, and what to do about it is the Owner's.
- **no_observation** — the instrument failed: a truncated answer, a refusal, an unparseable record, a crash, a
  bound exceeded. **No measurement is a finding about the instrument, never about the artifact**, and a record
  may not render "nothing measured" as data: a spread over n = 1 is *not measured*, and a missing verdict is
  never blank.
- **no_artifact** — the Maker produced no artifact: nothing parseable, or nothing at all. Like
  `no_observation` this is a finding about the job's **input**, never a score for the artifact, and it carries the
  same prohibition: **a run that made nothing may not appear as a 0.0 vector.** The record names **which side
  failed** — Maker, instrument, or prompt — because the three have different remedies. A null iteration is not
  counted against the cap and does not displace the incumbent.
- Escalation is an action taken after a `needs_owner`, not a state.

**An artifact already in service is never discarded.** When generation 0 is live and fails the rule, the verdict
stands as `rejected` and **the disposition is the Owner's**: hold and fix in place, or replace. Nothing is
destroyed while people are using it, and the verdict is not rewritten to match the decision.

**Verdict and disposition stay separate.** The Owner may ship a reject or bin an accept; the recorded verdict
stands as the loop produced it, and the decision is recorded alongside it, never as a rewrite.

## System change

Change one thing and read the dimensions against a **same-batch control.** Changing one artifact is the loop, not
the system loop; do not blend the metrics. **A conformance job is not a system change:** it fixes an artifact
against a frozen standard, the standard does not move, and the fixes are ordered by lowest score first and
smallest blast radius first — still one change per generation.

## Report where the frame failed

**If you hold a stronger standard than this frame carries, do not import it silently.** Record the pull and escalate the gap: a frame test that supplements the frame measures the supplement. Outside a test, an imported standard is labelled as borrowed, adapted or ours, and named — never absorbed.

The Orchestrator records every point where this sheet was insufficient, ambiguous, or forced a guess. A run with no
place to say that is not a record; it is a press release.

**An escalation carries four things: the question, what was tried, why no observable answer exists, and — always — the
options with a recommendation.** A question handed to the Owner without options and a recommendation is work pushed
back, not escalated. This holds for a frame defect as much as for a value: *the frame conflicts here, these are the ways
it could be resolved, this is the one I recommend, and this is what changes in the record if you rule otherwise.*

## Rules in force

The twelve are shared by both entries. **B carries one more, its own — the thirteenth — inside Entry B above** — the instrument must be
shown failing — because the evidence that earned it is all retrofit evidence.

**Rules 1–12 are the numbered list below. Entry B's thirteenth is the shown-failing rule stated inside Entry B above — carried there, not renumbered here.**

1. **The Evaluator is a proxy.** Buyer and Specialist hold the bar for “done” (fitness-for-purpose) and “good” (excellence); the Owner ratifies the frame; the Architect writes it. No provenance, no authority. `[ours]`
2. **Three nouns, one blind channel.** Artifact, reference, observation. The Evaluator sees the work; the Maker never produces the observation. **At least one Evaluator differs from the Maker in model family; on every dimension the Maker's family holds no more than half of the Evaluators; an undisclosed family is read as the Maker's.** `[the split is borrowed; the blindness rule is ours]`
3. **A score without an observation is not a score** — that dimension forces `needs_owner`. A fabricated remedy is a defect; an absent remedy is allowed. **Withholding a measured remedy is a defect** — it puts the Maker to work that is already done. **A check on absence carries a presence precondition:** if the artifact contains no instance of the thing checked, the channel reports `UNOBSERVED`, never a passing reading. *"All present in the documentation"* is vacuously true of an empty set, and **a check that cannot fail certifies nothing.** `[ours]`
4. **A disagreement must be locatable:** the artifact missed the standard, the standard moved, the dimension was never authorized, or **the frame itself is at fault.** Three classes, plus the frame — and never "bad Maker." `[ours]`
5. **A capability gap escalates.** Do not regenerate what the Maker cannot act on. `[ours]`
6. **Bounds are supplied, never defaulted; at the cap the work goes to the Owner, not the bin. A bound binds as the
run proceeds, not only before it starts** — a budget checked only at the gate does not bound anything, and the
instrument stops at the bound and records where. `[the cap is common practice; the routing is ours]`
7. **Verdict and disposition are separate acts.** `[ours]`
8. **Ground truth has a hardness** — `INVARIANT` / `DOCUMENT` / `PRIOR` — and a dimension may not claim harder than the channel that carries it. **A drifting reference caps every dimension at its own hardness: fix the reference before enforcing it.** Where the reference the standard needs **does not exist at all**, that is a missing reference — reported as such, never stretched into "the artifact missed the standard." **Every observation names its channel and the seat it ran from. A claim about reachability, availability or operability needs a channel outside the Maker's seat** — a probe from the Maker's own machine is the Maker's own account of its work by another route. **The in-use seat is a channel:** the Owner or the Buyer meeting a defect by *using* the artifact produces an observation — the artifact's identity, the channel (`in-use`), the seat it ran from, the measurement — and it becomes a reading only when a channel reproduces it, never a score on its own. A user report is an observation; a scored dimension requires a channel to reproduce it. `[ours]`
9. **The rung names who decides; it never waives a must-ask.** A value on the list is asked at L5 too. `[Hyatt's ladder; the never-waives rule is ours]`
10. **Keep the instrument that accepted the work** — rubric, Evaluator identity, ground-truth version,
measured spread, **and the code that implements it**: the instrument is both, kept hashed, because a
re-run holding the same rubric and a different runner is a different instrument. **The model that serves
the seat is part of the instrument, and its measured properties are recorded with it** — its strictness
with the artifact class it was tested on, its stability across runs, its completion at the stated budget,
and its cost per reading computed from its own token count, because cost varies by tokenizer and not by
prompt. **The Maker's model is part of the job**, and its task classes are recorded the way rule 10 already
records the Evaluator's: **generation and revision are different classes**, each shown by a completed run. A
job that will iterate requires the revision class — shown by a run, **never by a claim about the
engine.** **A verdict is issued only on at least two scored runs:** one run is a sample, not a measurement,
and a reading resting on one run is labelled as such. Where that model is inconsistent by the same order
as the effect being judged, the control is what separates them. `[ours]`
11. **Smaller, never partial.** A reduced instrument may not skip a must-ask, a terminal-state rule, or a checked line. `[ours]`

12. **Carry the best parts forward.** The loop keeps every artifact it produced. An iteration replaces the incumbent when it is better on at least one scored dimension and worse on none. A reply that is worse on any scored dimension does not replace it. The loop does not stop because a generation failed to improve every dimension. It stops at the cap, or when the pass rule is met. A trade is the **Owner's to declare**, never the loop's to absorb. The next iteration is given **the best artifact the job has produced — best, not merely standing** — together with **every known defect and its measurement**, **every known workable solution and the measurement that establishes it**, and an instruction to proceed. **The standing artifact is the frontier; the best artifact is the input.** The record carries **every iteration's per-dimension vector**.

### Machine extract (derived — cites, does not restate)

One row per verso requirement. Ids are **stable and never renumbered** (the C-lines' discipline). The extract is
derived from the prose above; **where the two disagree, the prose is the defect and the fix is a proposal.**
`tools/check_consistency.py` verifies that every `Cites` value resolves to text in this file.

| Id | Cites | Requirement | Enforcement point |
|----|-------|-------------|-------------------|
| **I1** | A1 | Declare the frame first, in the sheet's order; nothing is generated until every must-ask is supplied. | manual (sheet) · packet `required[]` |
| **I2** | A2 | Write the Evaluator, show it failing on a bad case and passing a valid alternative, have it pre-read against the bar by an adjudicator who did not write it, then freeze and hash the rubric. | manual · record `instrument_in_force` |
| **I3** | A3 | The Maker says the win and the done-rule back, in their own words, before generating. | manual |
| **I4** | A4 | Generate and judge in the loop; observe through a channel the Maker does not control; hand over the classified critique with rule 12's input, never held-out material. | Contracts §2/§7 · manual |
| **I5** | A5 | Keep the instrument that accepted the work — rubric, ground-truth version, Evaluator identity. | C30 · record fields |
| **I6** | R1 | Collect the artifact's own standard and do not judge yet; report contradictions, do not resolve them. | manual |
| **I7** | R2 | Declare the frame you would hold it to now, plus what is **frozen by circumstance**. | manual |
| **I8** | R3 | Freeze and hash the rubric before any defect-revealing read; declaration order substitutes for blindness. | manual · record field |
| **I9** | R4 | The past gets a census, not a verdict; thresholds apply forward; any fix is a new job. | C32 · outcome `census` |
| **I10** | Entry B thirteenth | The instrument — and the model serving the seat — must be shown failing before it judges. Retrofit form: a named dimension read other than *conforms* with a quoted reason, or one scored below its floor; an injected case only where neither is available. | C3/C32 · manual |
| **I11** | R3 | `reads_before_freeze` is a **required line** on an Entry B record, not a footnote. | packet `reads_before_freeze` (required on `entry: B`) · C32 |
| **I12** | Escalation | An escalation carries four things: the question, what was tried, why no observable answer exists, and the options with a recommendation. | manual |
| **I13** | Rule 1 | The Evaluator is a proxy; no provenance, no authority. | manual |
| **I14** | Rule 2 | Three nouns, one blind channel; **At least one Evaluator differs from the Maker in model family; on every dimension the Maker's family holds no more than half of the Evaluators; an undisclosed family is read as the Maker's.** | C-line · `check_role_separation.py` |
| **I15** | Rule 3 | A score without an observation is not a score; a fabricated remedy is a defect and an absent one is allowed; a check on absence carries a presence precondition. | SCHEMA `dimension.observation` · C27 |
| **I16** | Rule 4 | A disagreement must be locatable — three classes plus the frame; never "bad Maker". | C-line |
| **I17** | Rule 5 | A capability gap escalates; do not regenerate what the Maker cannot act on. | manual |
| **I18** | Rule 6 | Bounds are supplied, never defaulted; a bound binds as the run proceeds; at the cap the work goes to the Owner, not the bin. | SCHEMA `bounds.*` required · C-line |
| **I19** | Rule 7 | Verdict and disposition are separate acts. | packet `disposition` |
| **I20** | Rule 8 | Ground truth has a hardness; a drifting reference caps every dimension at its own hardness; every observation names its channel and seat. | SCHEMA `ground_truth_hardness` · record `observation_channel` |
| **I21** | Rule 9 | The rung names who decides; it never waives a must-ask. | manual |
| **I22** | Rule 10 | Keep the instrument that accepted the work, including the code and the seat model's measured properties; a verdict needs ≥2 scored runs. | C30 · record fields |
| **I23** | Rule 11 | Smaller, never partial: a reduced instrument may not skip a must-ask, a terminal-state rule, or a checked line. | manual |
| **I24** | Rule 12 | Carry the best parts forward; a reply replaces the incumbent when it is better on at least one scored dimension and worse on none; a regression does not replace; failing to improve every dimension does not stop the loop; a trade is the Owner's to declare. | record per-dimension vectors |

## What we stand on

- **Covey — stewardship delegation** (*7 Habits*, Habit 3): the five conditions — desired results, guidelines, resources, accountability, consequences — and his maturity rule: narrow the results and add guidelines for the less mature, widen them for the more. **Not:** his language, the gofer-versus-stewardship sermon.
- **Hyatt — five levels of delegation:** L1–L5 as on the sheet. **Not:** L5 as permission to stop thinking.
- **Critic split** — a reviewer **(Evaluator)** that does not produce, and a producer **(Maker)** that revises from *classified* critique. Cite the practice (the writer/reviewer split in agent workflows). **Not:** the machine-learning algorithm that shares the name — no reward signal, no value function, no training.
- **Constitutional form** — the standard is a written, versioned text, a critique cites the clause it enforces, and a revision answers that citation. **Not:** the content (harmlessness is Anthropic's constitution, not ours), same-model self-critique, or a standard baked into weights.
- **Evaluation-driven development** — scorecard before optimization; dimensions, not a pooled average; the evaluation gates the change; diagnose before replacing the Maker. **Not:** golden-set-as-the-only-truth, or a product loop on a one-off job.
- **Teach-back** (clinical health literacy) — the person repeats the instruction in their own words, because "do you understand?" reliably returns *yes*. **Not:** a nod taken as confirmation.
- **Accountability cadence** — Covey's fourth condition, and on the sheet it is a field: *we look on ___ · you ping if ___.* **Not:** "evaluate or hover" as the only two modes.

## Refusals

- No new mandate version — **except** where a rule this sheet carries contradicts a clause in force, and then that clause moves in the same pass, which is §12's discipline applied to the frame. And no "unified framework" that restates a cited source in our vocabulary.
- No clause without a job that needed it. If a rule never fires, demote it. If a gap is already covered above, add a citation, not a clause.
- No human-equivalent schemas until a human job has actually failed for lack of one.
- No scoring voice without a profile; no invented dimensions.

---

*Drafted from Mandate v18 / Contracts v1.10 — provenance, not instruction: everything this sheet
**requires** is written on it — and where it is not, the sheet names what is outstanding and who owes it. **In force since 2026-09-22.** The Owner's words: *"The sheet is ratified and operable."* Both conditions it set for itself are met — ratified in the Owner's own words, and one real handoff run on it (the JEV skill job, Entry A, commissioned and accepted; not a sealed rehearsal). Its author wrote both, so it cannot judge E-DI (§7.2). **v0.15 landed the seven amendments of proposal 0013,
ratified by the Owner on 2026-09-22; v0.16 tightens rule 10 to the instrument it is about, carries the loop as its
own rule — the verso is twelve — and drops the rule-1 citation at the Owner's word.** **v1.0 — the sheet is ratified and operable (2026-09-22), by the Owner's word.** **v1.1 — proposal 0016 clauses 3 and 5 landed on the Owner's word (rule 8's channel-and-seat, rule 12's best-artifact input, rule 3's fabricated-versus-withheld distinction).** **v1.1.1 — a text repair, content preserved (proposal 0015 clause 1, ratified 2026-09-22): rule 10's two copies merged into one, the seat noun corrected at A5, and the frame line returned to the mandate.** **v1.2 — the remaining three clauses of proposal 0016 landed on the Owner's word, clause by clause in the review Doc: `no_artifact` in the Exits list, the Maker's task classes in rule 10 and the Maker row, the channel's seat and the in-use seat in rule 8, the presence precondition in rule 3; and the Refusal narrowed so a clause that contradicts the frame can move (proposal 0015 ruling 3.3).***

---

## Implements

This table cites **up**, to the rules of `../DOCTRINE.md` it carries (doctrine IDs, `D…`). It belongs to this file: when an id here changes, update the table in the same commit. `../tools/check_downhill.py` checks that every id here exists, every doctrine id it names exists, and every doctrine rule is carried somewhere. Basis: *v0.1 tag* means the doctrine's own v0.1 citation named this id; *added 2026-11-02* means it was added in review and confirmed by the Owner on 2026-11-02.

| This file | Carries | Basis |
|---|---|---|
| `I1` | D2.1, D2.2, D2.3, D4.1, D5.entry.A | mixed: D2.1 added, D2.2 added, D2.3 added, D4.1 added, D5.entry.A tag |
| `I2` | D4.2, D5.entry.A, D6.2, D6.3 | mixed: D4.2 tag, D5.entry.A tag, D6.2 added, D6.3 added |
| `I3` | D5.entry.A | v0.1 tag |
| `I4` | D5.entry.A | v0.1 tag |
| `I5` | D5.entry.A | v0.1 tag |
| `I6` | D5.entry.B | v0.1 tag |
| `I7` | D5.entry.B | v0.1 tag |
| `I8` | D5.entry.B | v0.1 tag |
| `I9` | D5.entry.B, D5.outcome.census | mixed: D5.entry.B tag, D5.outcome.census added |
| `I10` | D4.2, D4.5, D6.1 | mixed: D4.2 tag, D4.5 tag, D6.1 added |
| `I11` | D5.entry.B | v0.1 tag |
| `I12` | D4.11 | added 2026-11-02 |
| `I13` | D2.bar, D2.4, D2.no-provenance | mixed: D2.bar added, D2.4 added, D2.no-provenance tag |
| `I14` | D3.family, D4.3 | mixed: D3.family added, D4.3 tag |
| `I15` | D4.2, D4.7 | v0.1 tag |
| `I16` | D4.6 | v0.1 tag |
| `I17` | D4.8 | v0.1 tag |
| `I18` | D4.10, D5.exit.needs-owner | mixed: D4.10 tag, D5.exit.needs-owner added |
| `I19` | D5.disposition | v0.1 tag |
| `I20` | D4.4 | v0.1 tag |
| `I21` | D4.14 | v0.1 tag |
| `I22` | D4.5, D4.12, D6.1, D6.4 | v0.1 tag |
| `I23` | D4.13 | v0.1 tag |
| `I24` | D4.9, D5.step.5 | v0.1 tag; D5.step.5 added 2026-11-02 (v0.2.1) |
