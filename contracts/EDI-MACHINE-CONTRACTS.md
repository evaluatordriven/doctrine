# E-DI — Machine Contracts

**Authority:** tier 3 in `../AUTHORITY.json` — outranked by tiers 0–2; conflicts follow its conflict rule.

**Status:** normative. **This is the file an agent must obey.**
**Audience:** agent implementing or operating an E-DI loop.
**Object:** machine specification of E-DI (roles, states, schemas, pass rule).
**Version:** 1.27.0 — 2026-11-02 (Owner decision, DOCTRINE v0.2.1 D3.disposer-never-judges: §4's Owner row bars the Owner from the Evaluator's seat in a job it disposes of, and no longer from the Maker's seat, which DOCTRINE §3 allows when disclosed; no rule-index change, the roles table is not extracted). 1.26.1 — 2026-11-02 (DOCTRINE v0.2.1, editorial: §11 Implements gains C39 (D3.held-out, D5.step.5) and C40 (D5.human), widens C37 to D3.Orchestrator, D3.routing and D5.step.5, and §4 to D3.routing; §12 pins the Operating Instrument v1.13; no NORMATIVE rule changes meaning). 1.26.0 — 2026-11-02 (Owner decision: §4's Evaluator row names the reader form and the seat's holders, a person, a model or a script, carrying DOCTRINE D3.reader and D3.holder; roles table, no rule-index change. v1.25.0 — 2026-11-02: Owner decision: §4 names the adjudicator and the test author as forms of the Evaluator seat, carrying DOCTRINE D3.adjudicator and D3.test-author; no rule-index change, the roles table is not extracted. v1.24.1 — 2026-11-02: public derivative: editorial only — Primer attributions removed, the authority chain of `../AUTHORITY.json` and custody/v1 precedence stated in §0, §10 retitled; no NORMATIVE rule added, removed or reworded. v1.24.0 — 2026-10-29: 0055 as amended: seat-to-seat communication; held-out never reaches the Maker; per-act approval optional and job-declared; C38–C40 appended).
**Owner ratification:** **2026-09-24** — the Owner ratified this short front as the weight-bearing Machine Contracts (NORMATIVE law unchanged from v1.12; compression + seat Title Case + §0/§12 cleanup only).
**Scope:** roles as binding behaviour, states, schemas, the pass rule. Missing fact → **ask**, never invent.

---

## 0. How to read this document

Two kinds of statement appear here, and they are labelled:

- **NORMATIVE** — required. An implementation that violates it is not implementing E-DI.
- **EXAMPLE** — a value that worked in one deployment. Never a requirement, never a default to copy blindly, never a reason to reject a different value. (Most worked EXAMPLES live in the v1.12 full text, which is not published; the short front keeps the label so you can still tell law from illustration when an EXAMPLE appears.)

Authority follows `../AUTHORITY.json`. `../DOCTRINE.md` (tier 1) and the Playbook and Mandate (tier 2) outrank this document, and a conflict with them is a defect here. This document (tier 3) outranks the Operating Instrument, the schemas and fixtures, For Machines, the Quickstart and the Example on roles, states, schemas and the pass rule. **The retained record's terms belong to custody/v1** (https://github.com/evaluatordriven/custody): where this document and custody/v1 name the same field or term of the record, custody/v1 governs, and §10 adds only method rules the record does not carry. Evidence docs have no authority.

The **mandate** (§1.7) is the frame the work is judged against — supplied by the Owner — not ranked among the corpus's own files.

If a fact is needed and is not specified here, **ask** — do not invent a value.

---

## 1. Design-time order (NORMATIVE)

Build in this order. Each step depends on the one before it, and each step states its own rule.

### 1.1 Define the Buyer and the Specialists (NORMATIVE)

**NORMATIVE:** record the Buyer with provenance on every job. Record the Specialist with provenance
on a job that has a bar in force (`mode: scored`, and not sitting in `ratified: false`). A rubric
that cannot answer *"who is buying this, and which master of the craft approved the standard?"* is
invalid. A readings job has no bar: it names no Specialist at the outset (§3); the field is omitted,
not filled with a dummy.

### 1.2 Define ground truth, at a declared hardness (NORMATIVE)

**NORMATIVE:** name what the Evaluator judges against — source document, invariant, test, reference
set, or measurement — its **version in force**, and the channel that carries it. Ground truth is
**versioned, not immutable**: it may move, and when it moves the version moves with it (§10.1, §10.3).
Immutability is the hardest grade available, not the definition of ground truth (§1.6).

### 1.3 Write the Evaluator (NORMATIVE)

**NORMATIVE:** dimensions, anchors, pass rule, violation classes, verdict enum — and the Evaluator
exists before any generation begins.

### 1.4 Build the Maker (NORMATIVE)

**NORMATIVE:** the Maker is stood up after the Evaluator, so nothing is generated against a standard
that is still being written.

### 1.5 Build the Orchestrator (NORMATIVE)

**NORMATIVE:** loop mechanics, bounds, state store, escalation path.

An implementation must not accept work generated before its Evaluator existed, except as a
baseline measurement explicitly labelled as such.

`entry: B` is the machine name for that baseline. The rule is C32. The procedure is Instrument Entry B. This paragraph does not restate R1–R4.

### 1.6 Ground truth is versioned, at a declared hardness (NORMATIVE)

**NORMATIVE:** ground truth carries two properties beyond its identity — a **version** and a
**hardness grade** — and both are recorded with the job. A judgement that cites ground truth without
its version cannot be re-established later; one that cites it without its hardness cannot be weighted.

Hardness is how much the Evaluator may lean on it. The grade is supplied per job and is never defaulted:

- **`INVARIANT`** — an artifact that cannot move while the job runs: a test, a byte-identical input, a
  specified interface, a doctrinal or mathematical invariant. The Evaluator may lean fully: a disagreement
  is a defect in the artifact, not an argument with the standard.
- **`DOCUMENT`** — a source of record a Principal authors and may revise: a policy, a brief, a voice
  profile, a mandate. The Evaluator may lean only on the version in force, and that version is recorded
  with the judgement. A `DOCUMENT` cannot support a dimension that asserts permanence, and revising it
  is a revalidation trigger (§10.3).
- **`PRIOR`** — expert or empirical judgement where no artifact settles the question: market data,
clinical consensus, a Specialist's taste. The Evaluator may lean only as far as the reference carries it,
  and the dimension reports its uncertainty rather than absorbing it.

**NORMATIVE:** a dimension's stated hardness must be no harder than the ground truth that carries it.
A `DOCUMENT` used as if it were an `INVARIANT` is the defect this section exists to name — the loop
then reports the standard's movement as a change in the artifact, which is §10.2's failure with a
different source.

The lesson — *ground truth comes in kinds, same discipline, different hardness* — is
what this section makes mechanical. Kinds that differ in hardness differ in what a score from them can
be used for.

### 1.7 The frame has an instrument: the mandate (NORMATIVE)

**NORMATIVE:** the frame — what the work must accomplish, and what it must not do — is supplied as a
**mandate**: a document authored by the Principal, in the Principal's own words, holding the problem
statement, the scope, the **exclusions**, and the conditions under which the work has failed. A frame
asserted in prose inside a doctrine is not an instrument; the mandate is. The mandate in force is
named, by version, with the job.

**NORMATIVE:** the mandate's scope and exclusions bound the dimension set. A dimension the mandate
excludes is a **frame violation**: it may not be scored, and a job carrying one cannot reach
`accepted` — its exit is `needs_owner`. A dimension the mandate neither authorizes nor excludes is a
**frame question**: it is escalated to the Principal, not scored as work quality. Authorizing a new
dimension is a mandate revision, and a mandate revision is a revalidation trigger (§10.3).

**NORMATIVE — the ground truth is not the Maker's to improve.** Where the mandate names a source
of record as read-only, a Maker that submits a revised *source* rather than a revised *artifact*
has crossed the frame: the submission is the wrong object, and the finding is recorded as a frame
violation. The loop's brief is to make the artifact match the frame, never to move the frame to match
the artifact. This is the failure mode named when the source's authority is said to be
*assumed, not iterated*.

**NORMATIVE — a doctrine that judges has a mandate too.** Where a doctrine, rubric or corpus judges
other work, its own mandate is what closes the recursion: authored by the Principal, predating the
corpus, naming what the corpus must accomplish and what it must not do. While that mandate is
unratified, no dimension scoring the corpus against its purpose may be `pass` — it is `not_assessed`
and reported. An Evaluator without a prior reference measures persuasiveness, and a rubric that passes its
own bar is not a verdict.

---

## 2. Run-time loop (NORMATIVE)

State machine. **Every path ends in a named terminal state; there is no fifth state in which the
loop quietly ends.**

Pairing rule: `accept` / `reject` are Evaluator verdict words. `accepted` / `rejected` are terminal words. Do not emit either pair in the other slot. `census`, `no_observation`, and `no_artifact` are outcomes, never terminal states.

| Situation | `terminal_state` | `outcome` | Evaluator `verdict` (not terminal) |
|-----------|------------------|-----------|-------------------------------------|
| Scored pass | `accepted` | `accepted` | `accept` |
| Readings pass | `accepted` | `census` | `accept` |
| Readings job, one or more dimensions read *does not conform* | `needs_owner` | `needs_owner` | `needs_owner` |
| Below `T_reject` | `rejected` | `rejected` | `reject` |
| Cap, still at or above `T_reject`, not a pass | `needs_owner` | `needs_owner` | `needs_owner` |
| Instrument failed | `needs_owner` | `no_observation` | do not emit a score |
| Maker produced nothing | `needs_owner` | `no_artifact` | do not emit a 0.0 vector |
| Not done, under cap, at or above `T_reject` | non-terminal `regenerating` | — | `regenerate` |

| State | Meaning | Exit |
|-------|---------|------|
| `pending` | job accepted, no generation yet | → `generating` |
| `generating` | the Maker is producing or revising | → `evaluating` |
| `evaluating` | the Evaluator is scoring against ground truth | → `accepted` / `regenerating` / `needs_owner` / `rejected` |
| `regenerating` | violations sent back as constraints | → `evaluating`; if iteration count ≥ cap → `needs_owner` |
| `accepted` | **terminal** — score meets the pass rule | ship |
| `needs_owner` | **terminal** — inside the human band at the cap, or an escalation class fired | a human decides |
| `rejected` | **terminal** — below the reject floor at any iteration | discard |

`regenerating` is **not** a terminal state. Terminal states are exactly: `accepted`,
`needs_owner`, `rejected`.

**NORMATIVE — a job records its terminal state *and* the outcome it exited under.** The state alphabet is
three; the outcomes are six, and an outcome is not a state. `accepted` (a scored job that passed) · `census` (a
readings-only job in which every readable dimension conforms, §3; a `does not conform` reading is not a census — it exits `needs_owner` with outcome `needs_owner`) · `needs_owner` (failed at or above the reject floor, or
the cap reached without a pass) · `rejected` (below the reject floor; scored jobs only) · `no_observation` (no
verdict exists — the instrument failed, §5) · **`no_artifact`** (the Maker produced nothing: nothing
parseable, or nothing at all — below) — whose **terminal states are `needs_owner`**, because an instrument failure,
or a Maker that made nothing, must not end a job with no human in the loop. A **readings-only job's terminal state is `accepted`**, with
`census` as its outcome; a record carrying an outcome without its terminal state, or a terminal state
without its outcome, is incomplete.

**NORMATIVE — the Maker-side outcome.** A run in which the Maker produced **no artifact** records outcome
`no_artifact`, with terminal state `needs_owner`: nothing was made, so nothing is scored, and a run that made
nothing may never be rendered as a 0.0 vector. The test is **structural** — does the delivered content parse
as an artifact at all — and never a character count. The record names **which side failed** (Maker,
instrument, or prompt), because the three have different remedies, and a null iteration is not counted
against the cap and does not displace the incumbent.

**NORMATIVE:** `rejected` means *below the reject floor*. Reaching the cap without passing is
**not** a rejection — if the score is at or above the floor, the cap produces `needs_owner`
(§3). An implementation that routes cap-reached work to `rejected` is discarding work a human was
supposed to see.

**NORMATIVE:** escalation classes fire from `evaluating` directly (values or doctrine involved →
always a human). Escalating to a second engine after a terminal non-accept is an
*action taken after* a terminal state, not a state of its own, and it does not extend the loop.

---

## 3. Pass-rule algebra (NORMATIVE shape; EXAMPLE values)

```text
pass(job)          :=  mean(dimension scores) >= T_accept AND min(dimension scores) >= T_dim    (scored job)
pass_readings(job) :=  every readable dimension reads conforms                                  (readings-only job)

accept     : pass(job) OR pass_readings(job)
regenerate : not pass(job) AND min(score) >= T_reject AND iterations < cap
needs_owner: not pass(job) AND min(score) >= T_reject AND iterations >= cap
rejected   : min(score) < T_reject                        (scored jobs only: a readings-only job may not produce it)
```

- **NORMATIVE:** a pass requires both an average threshold **and** a per-dimension floor. An
  average alone permits a fatal defect to be averaged away.
- **NORMATIVE:** the thresholds are fixed **before** the run and recorded with the job.
- **NORMATIVE:** the iteration cap is finite and recorded with the job. Iterations are counted from
  0 before the first generation, incremented once per generation, so the cap is the total number of
  generations permitted — not the number of regenerations. An implementation must state which it
  counts; off-by-one at the cap silently changes the cost and the escalation rate.

- **NORMATIVE:** dimension scores are integers or one-decimal reals on a 1–10 scale, unless the job
  records a different scale alongside its pass rule. An implementation must not silently rescale.
- **NORMATIVE — the must-ask list.** These are supplied per job and recorded with it, never
  defaulted: Buyer; Specialist; ground truth, its version, its hardness grade and the channel that
  carries it; the Maker — the engine, its version, and the feedback forms it can consume; the
  mandate in force and the dimensions it authorizes or excludes; the dimension set;
  `T_accept`; `T_dim`; `T_reject`; the iteration cap; the budget; the human seat; the escalation
  classes; and, on a revision, whether a retained instrument of §10 is being re-used and which one.
  If one is missing, **ask** — do not infer it from an example in this file, and do not
  ship a code default, *even a default equal to the example above*. A default that happens to match
  an example is still non-compliant: the next job silently inherits it, and the standard was never
  agreed for that job.
- **NORMATIVE — the frame a scored job cannot run without (C33).** A `mode: scored` job carries, before generation, a non-empty `ground_truth` (each row: `source`, `version`, `hardness`), a `mandate_ref` of `doc` plus `version`, and a non-empty `escalation` route. Readings jobs are not subject to this. The other must-asks — the Maker's feedback forms, the dimension set, retained-instrument reuse, task classes, escalation classes — stay supplied per job and are **not** structurally enforced. A gate that validates without this frame has not shown the job is ready.
- **NORMATIVE — when a value cannot be obtained.** If a must-ask value is unavailable (no human, no
  record), the job may still run, but it runs **unratified**, and the implementation must: propose
  each value; record its provenance as *proposed, unratified*; surface an explicit ratification
  request; and **never reach the `accepted` terminal state** — the best exit available is
  `needs_owner`. A job that ships on thresholds it chose for itself has validated itself against its
  own standard, which is the failure this document exists to prevent.

  **Where unratified values may sit:** in a single top-level `proposed` block flagged
  `ratified: false` — and **nowhere else**. Not in the runtime configuration, not under a
  `pass_rule.thresholds`-shaped field, not as an argument default. A value that occupies the place a
  configured value occupies will be used as one, whatever the note above it says: an agent that marks
  a threshold "PROPOSED (unratified)" while still emitting it inside `config` has not separated the
  two, and the next reader will take it as configured. While `ratified: false`, the runtime
  configuration for the must-ask fields must be **absent or empty**, and the loop's only possible
  terminal state is `needs_owner`.

- **NORMATIVE — the readings form, where no bar exists yet.** A job with **no Specialist named at the outset**
  declares `mode: readings`, supplies **no thresholds** — `T_accept`, `T_dim` and `T_reject` are absent and nothing
  defaults them — and **may not score**: it returns readings (*conforms*, *does not conform*, *unobserved*) and never
  numbers, because a score asserts standing against a bar and there is no bar yet. Its pass rule is `pass_readings`
  and its outcome is `census` (§2); **it may not produce `rejected`**, because there is no floor to be below. *At the
  outset* is load-bearing: a Specialist named after the readings are in does not license scoring, or the standard
  would be fitted to the results it is meant to judge. This is the case §3's unratified-value rule reaches from the
  other side: the job is not unratified, it is **unbarred**, and it says so.

When an engine cannot consume feedback, the loop is invalid: an implementation must either insert
an influence channel (paraphrase, a promptable re-generation pass, or human) or decline to run the loop.

---

## 4. Roles (NORMATIVE)

| Role | May do | Must never do |
|------|--------|---------------|
| **Owner** | Own the outcome; ratify the frame; set the values, the priority and the risk appetite; authorize the dimension set; declare a trade; dispose of a rejected artifact | Author the standard; score the work; hold the Evaluator's seat in a job it disposes of (`../DOCTRINE.md` D3.disposer-never-judges) |
| **Architect** | Define *done* and *good*; author the standard; set the thresholds; write the frame instrument (§1.7); **decide what is built next, what each iteration is given and whether the job is ready to hand to the Maker — a design decision, never a score (§4 below)** | Score the work; produce the artifact; ratify the frame it authored — **the Owner ratifies** |
| **Evaluator** | Score against ground truth; emit the schema in §5; classify violations; recommend a verdict; read each dimension through a channel the Maker did not produce. The seat is held by a person, a model or a script, recorded with the job; whichever holds it reads the batch's controls | Generate or edit the artifact; widen its own authority beyond §3 |
| **Maker** | Produce and revise the artifact from the job, the standard, and the last verdict | Score its own output; declare itself accepted; change the standard |
| **Orchestrator** | Dispatch, route verdicts, enforce bounds, own state and logs, escalate | Generate content; score content; impersonate either role; **decide what an iteration is given or whether the job is ready for the Maker — it assembles, delivers and verifies that input (§4 below)** |
| **Evaluator: adjudicator** | Rule on a disagreement between Evaluators by reading the work itself (the code, the text); record the ruling beside the readings it settles | Resolve a split by averaging; rule without reading the work |
| **Evaluator: test author** | Write an independent observation channel: a test, a planted case, a task for a reader who has never seen the work | Be the Maker; see the Maker's reasoning |

**NORMATIVE:** the Maker and the Evaluator must not be the same model instance in the same
job. If they are the same *model*, they must be separate *calls* with no shared working state, and
the implementation must record that fact with the job.

**NORMATIVE — the seats are named, and they are separate.** The seats are a **job-level fact**: the job packet
names who holds each — Owner, Architect, Buyer, Specialist, Maker, Evaluator, Orchestrator — and one party may hold
several, recorded as such (§3's must-ask list, §8). The **Owner** and the **Architect** are two seats, not one: the
Architect authors the standard and the frame, the Owner ratifies them and sets the values. A party holding both
authors and ratifies, which is recorded with the job, because nothing else distinguishes that arrangement from a
single seat.

**Definition — the word *Principal*.** Where this document says *the Principal*, it means those two seats in the
work each holds: the **Architect** authors the standard and the frame, the **Owner** ratifies them, sets the values,
authorizes the dimension set and disposes of a rejection. The mandate ruled the two separate (Playbook §6) and asked for this reconciliation; it adds no seat and changes no rule.


**NORMATIVE — the Orchestrator routes; the Architect designs.** What is to be built next, and therefore
what the next iteration is given — which known defects and which workable solutions go with the artifact that
carries forward, and what else is included as relevant (Instrument rule 12) — and whether a job is ready to
hand to the Maker are the **Architect's** decisions. The **Architect decides what is to be built and what the
iteration is given; the Evaluator alone judges whether what was built meets the standard; the Architect never
scores.** **Which artifact carries forward is picked mechanically by rule 12's test on the Evaluator's
scores; the Architect decides only what goes with it — which parts are kept, which are redone, and the
request the Maker is given — and never picks the artifact on its own judgement.** **A job is ready for the
Maker when its input and design are ready: every file the Maker needs is pinned, the fixes are specified, and
nothing in the request contradicts the bar. Readiness is never a prediction that the work will pass;
predicting a pass is scoring, and only the Evaluator scores.** The **Orchestrator** assembles that input, delivers it, verifies that what was
delivered is what was decided (§7.3), records both, and applies the pass rule; where it sees a gap it
recommends, as an escalation requires (Instrument I12), and the Architect decides. The Architect's seat may be
held by the Owner, by a delegate, or by a bot, recorded as such (above); **it is never the Orchestrator's by
default.** A party that both routes and decides the design is a declared double-hat on the record, because
otherwise the seat falls to whoever is operating the loop and nothing in the record shows it.

**Definition — research is the Architect's capability, not a seat.** Gathering existing practice and
adoptable solutions before a build starts — and whenever the Architect needs it to decide what an iteration
is given — is work the Architect does or commissions. It adds no seat and no engine to the loop. Research
delegated as its own job is a job on the sheet, with its own Buyer, standard, Evaluator and exits (Playbook
§2, *Note on "researching"*).

### 4.1 The Maker is a supplied, resourced choice (NORMATIVE)

**NORMATIVE — the Maker is a supplied, resourced choice.** The Maker is a must-ask value,
recorded with the job: the engine, its version, and the specific feedback forms it can consume. A
Maker that cannot consume the feedback the Evaluator emits is not a weak loop, it is an invalid one
(§3): the implementation supplies a Maker that can act on the verdict, inserts a channel that can, or
declines to run.

**NORMATIVE — an iteration must be able to address what it was given.** A regeneration tasked with a
violation it cannot act on is not an iteration; it is a billed reroll. Where a violation names a defect
beyond the Maker's capability, the Orchestrator escalates it as a capability gap (§4, §6) rather than
spending the cap on it.

**NORMATIVE — an iteration names what it sends back.** Where the verdict is `regenerate`, the record carries
at least one violation: an iteration that names nothing it is tasked with is, by the clause above, not an
iteration. This creates no new concept — it makes the clause above checkable, as C34 did for the filing of
passes — so a `regenerate` verdict filing no violation **fails the record** rather than reading as a clean
run. Nothing here requires a remedy (§5), and nothing here decides whether the iteration should have been
taken: that is the Orchestrator's, and the deficiency it exposes is the loop's, not the reading's.

**NORMATIVE — resourcefulness is demonstrated, not asserted.** A Maker may not be recorded as suitable
on the strength of a verdict. What shows it is the next evaluation: the named violation class resolved,
disappeared, or persisted (§10.2's per-dimension attribution). A class that persists in every run of a
cell is structural, not noise, and the response is the capability escalation above — not another
regeneration.

**NORMATIVE — who applies the algebra.** The Evaluator emits scores, violations, and a
*recommended* verdict. It does not own the loop. The Orchestrator is the sole applier of the pass
rule, the cap, and escalation. An Evaluator that decides whether to iterate, or an Orchestrator that
scores, has collapsed two roles into one.


### 4.2 Seat-to-seat communication (NORMATIVE)

**NORMATIVE — the Maker and the Evaluator speak only through the Orchestrator.** The Maker and the Evaluator
receive work only as a dispatch from the Orchestrator and return what they produce only to the Orchestrator.
Neither addresses the other: the Evaluator receives the artifact by reference and hash, never the Maker's
account of it (§7.2), and the Maker receives findings only as the Orchestrator's relay (below). No seat
instructs the Evaluator on a score during a run: the instrument frozen for the job is the only word on
scoring the Evaluator takes, and a change to it is a new instrument (§10.3, Instrument rule 10), authored by
the Architect and ratified by the Owner. The Owner, Architect, Buyer and Specialist may speak with one
another directly; what they decide reaches a run only as the recorded frame, standard or decision, and the
Orchestrator delivers it. The one direct edge between a person and an acting seat that is reserved for
**approval** is defined below; it is used only when the job requires a per-act approval. A capability gap, a
say-back, or a dispute with the standard goes from the Maker to the Orchestrator, which escalates (§6).

| from ↓ to → | Owner | Architect | Buyer | Specialist | Orchestrator | Maker | Evaluator |
|---|---|---|---|---|---|---|---|
| **Owner** | · | D | D | D | D | A | A |
| **Architect** | D | · | D | D | D | R | F |
| **Buyer** | D | D | · | D | D | R | F |
| **Specialist** | D | D | D | · | D | R | F |
| **Orchestrator** | D | D | D | D | · | D † | D |
| **Maker** | A | — | — | — | D | · | **—** |
| **Evaluator** | A | R † | — | — | D | **—** | · |

**D** direct. **R** only as the Orchestrator's delivery, recorded. **F** only through the frame or standard
frozen before generation — never a run-time word on scoring. **A** approval edge — used **only when the job
requires a per-act approval** and only in the form the job declared; the seat that will act may ask for a yes
or no, stating what is to be run, under which handoff (by hash) and at what cost — and nothing else, in
particular no claim about its own work's quality. Default jobs declare **no** per-act approval; design and
routing still use **D**/**R** as the other cells say. **—** forbidden. **†** never carries held-out material
(below). The *approver* is the Owner, or the named person the Owner records for that approval; it is not an
eighth seat.

**Definition — held-out material.** Only material the Maker cannot see: content the instrument holds against
the work that is not in the job, the standard, the Maker's own artifact and repository, or the material
named in its handoff — control cases and planted cases kept outside the Maker's reach, the expected answers
on them, and the Evaluator's raw evidence about them. Material the Maker can see is not held-out because the
instrument also holds it: an expected value on a fixture in the Maker's own repository is not held-out.

**NORMATIVE — held-out material never reaches the Maker.** No message to the Maker contains held-out
material, from any seat. Findings reach the Maker — and the Architect, which decides what the Maker is given
(§4) — as the Evaluator's classified violations carrying **every known defect with its measurement**,
including an expected value on material the Maker can see, with the locator, the class, the shortfall and any
established remedy (Instrument rules 3 and 12). Only held-out material is withheld. The Evaluator holds
held-out material, as does the seat that authored it; the Orchestrator holds it in custody by hash and may
read it only to check outgoing messages against it. The Architect does not see it by default; an Architect,
an Owner, or any other seat that has seen it is recorded as having seen it. Before dispatch, the Orchestrator
checks every built Maker message against held-out material by a stated method and records the method, the
result and who ran it; a message that fails the check is not sent. **Where the Orchestrator has authored both
the dimension set and the held-out material — the fallback when no Buyer or Specialist is reachable — the
Evaluator or the Architect also runs the check before dispatch, and the record names who ran it.**

**NORMATIVE — dispatch runs on the Orchestrator; per-act approval is optional and job-declared.** A Maker
generation and an Evaluator pass run only on the Orchestrator's dispatch, within the bounds, and an Evaluator
pass names the artifact by hash, verified by the Orchestrator. **Per-act approval is not required by this
corpus.** Kickoff ratification of the frame, the budget and the bounds is enough for the Orchestrator to run
inside them unless the job declares otherwise. Which acts (if any) need a human yes beyond that kickoff — a
paid call, a batch, a re-run — is the job's declaration: its bounds and its level (Instrument rule 9), not a
standing duty to sit in the Maker's or Evaluator's chat.

**When the job requires an approval, the job also declares the form.** Allowed forms include at least:
(1) **standing / kickoff authorization** in the Owner's or Orchestrator's channel — a recorded grant such as
"run iteration 2 within $X / these parts" — after which dispatches under that grant need no fresh yes in the
acting seat's chat; (2) **direct yes in the acting seat's own channel** — an optional stricter mode for jobs
that choose it; (3) **relayed yes** — allowed only if the job's declared form allows relay. **A relayed
approval authorizes nothing unless the job's declared approval form allows relay and the record labels it as
relayed.** Each approval the job requires is recorded with the approver, the time with its zone, the channel,
whether it was direct or relayed, its words (or a paraphrase labelled as one), and what it covers. A form the
job did not declare authorizes nothing.

Ratifying the frame (which freezes the bar), authorizing the dimension set, declaring a trade and disposing of
an artifact remain the Owner's (above, Instrument rule 7). **A decision the Owner makes may be relayed** to the
seat that executes it, recorded as relayed. Decisions and approvals are different things: decisions may always
relay; approvals follow only the job's declared form.

---

## 5. Evaluator output (NORMATIVE schema)

The Evaluator returns structured data, never prose alone. Prose may accompany it; it may not
replace it.

**EXAMPLE values in `pass_rule` below — not defaults, not requirements.** An implementation that copies `8.5` / `7.0` / `6` without the job supplying them is non-compliant (§3). The block shows keys, not a bar.

```json
{
  "job_id": "string",
  "iteration": 0,
  "passes": [
    { "pass_id": "string", "kind": "scored | confirmation", "status": "filed | void",
      "artifact": "the pass's own filed file, resolved relative to this record (§10.1)" }
  ],
  "dimensions": [
    { "name": "string", "score": "<number, not a const>", "scale": "1-10 unless the job records another",
      "anchor_note": "what this score means here",
      "observation": "what the dimension was scored on, produced by the channel named below — required; an empty value leaves the dimension with no observation (§5, C27)",
      "observation_channel": "which channel produced this dimension's observation",
      "ground_truth_access": "none | blind_to_gt | saw_gt" }
  ],
  "pass_rule": {
    "accept": "<copied from packet T_accept>",
    "dimension_floor": "<copied from packet T_dim>",
    "reject": "<copied from packet T_reject>",
    "cap": "<copied from packet cap>"
  },
  "violations": [
    {
      "id": "V1",
      "class": "artifact_missed_standard | standard_moved | dimension_unauthorized | frame_at_fault",
      "dimension": "<the dimension this violation holds against, where the shortfall is per-dimension;
                    omitted where the shortfall is the pass rule's mean>",
      "observation": "the quoted text or observed behavior that constitutes the violation",
      "remedy": "the Evaluator's insight into what would rectify the condition, where it has one — omitted otherwise"
    }
  ],
  "verdict": "accept | regenerate | needs_owner | reject",
  "ground_truth_ref": "the artifact or invariant this scoring used",
  "ground_truth_version": "the version of the ground truth in force for this scoring (§1.6)",
  "ground_truth_hardness": "INVARIANT | DOCUMENT | PRIOR — supplied per job, never defaulted (§1.6)",
  "mandate_ref": { "doc": "<the mandate in force>", "version": "<its version>" },
  "instrument_in_force": {
    "version": "<Orchestrator stamps>",
    "rubric_sha256": "<Orchestrator stamps>",
    "code_sha256": "<Orchestrator stamps>"
  },
  "evaluator_identity": "model + version",
  "channel_blind": true,
  "ratified": true
}
```

*(Packet ↔ record mapping: `T_accept` ≡ `pass_rule.accept` · `T_dim` ≡ `pass_rule.dimension_floor` · `T_reject` ≡ `pass_rule.reject` · `cap` ≡ `pass_rule.cap`. These are the same values; an implementation copies them from the packet and must not carry a third name. The Orchestrator stamps `instrument_in_force` — version and both hashes — after the Evaluator returns. The Evaluator does not emit the hashes. Shape is checked by `schemas/evaluator-record.schema.json` and `tools/validate_evaluator_record.py`. A pass of that checker is not C8.)*

**NORMATIVE:**
- Every score carries its observation. A score with no observation is discarded, not averaged.
- **NORMATIVE — the `observation` field is required on every dimension.** The dimension object carries
  the observation its score rests on: the quoted text, the measurement, the observed behaviour. A
  dimension whose `observation` is empty or absent has no observation, and it has exactly one outcome — the
  forced `needs_owner` stated below — never a synthesised score, never an average, never a below-floor
  number put into `min()`.
- Every violation is classified into rule 4's locator — where the disagreement lies, not a severity and not an escalation class. Classification does not assign a route. The pass rule and the cap assign the route (§3, §4); the Orchestrator applies them.
- **EXAMPLE values are not a severity scale.** `P0`, `P1`, and `P2` are not defined. An implementation must not copy them, must not invent substitutes, and must not route on a severity the corpus has not ratified. A severity scale is a later proposal, and only after a job has failed for lack of one. Routing stays with the pass rule and the cap (§3, §4): the Orchestrator applies them.
- **NORMATIVE — the shortfall is required; the remedy is not.** Every violation states what the item
  failed to do against the standard, with the observation that shows it and the class it belongs to. A
  remedy is included where the Evaluator has an insight into what would rectify the condition, and its
  absence is not a defect in the record. A verdict that cannot say *how* an item falls short is not
  feedback, whatever else it contains; an Evaluator that prescribes without an insight has moved into the
  Maker's role.
- **NORMATIVE — a fabricated remedy is worse than an absent one.** A remedy supplied to complete the
  field, with no insight behind it, is itself a violation: it sends the Maker to fix something the
  Evaluator never observed.
- **NORMATIVE — the record names the instrument in force.** Every record carries the instrument it was made
  under: its version, and the hash of the rubric and of the code that implements it. A re-run holding the same
  rubric and a different runner is a different instrument (§10.1, §10.3), so a record that names none cannot be
  re-run, compared, or revalidated — and a record that names a component's hash while a different component scored
  misreports the instrument it is evidence about.
- `channel_blind` asserts that every observation channel met §7.2; `ratified` asserts that no must-ask
  value is *proposed, unratified* (§3). A record with `ratified: false` can never be part of an
  `accepted` terminal state. A scoring that names neither `ground_truth_version` nor
  `ground_truth_hardness` is incomplete: the first cannot be re-established later, the second
  cannot be weighted, and a dimension may not claim ground truth harder than its channel carries
  (§1.6).
- `ground_truth_access` is a closed enum. `saw_gt` on any dimension invalidates that dimension's
  observation (the channel had access to the answer it was checking), and the dimension then fails per
  the rule below.
- A dimension with no observation **fails**, and a job containing one can never reach `accepted`. Its
  exit is a **forced `needs_owner`** — not `rejected`. A missing observation means *the job could
  not be judged*, which is a different fact from *it was judged and found wanting*. Do not synthesise
  a below-floor score for it: that puts an invented number into `min()` and misreports the reason the
  job stopped.
- The verdict field is exactly one of the four values in §2/§3. Implementations must not invent
  synonyms (no "minor-revision" alongside "regenerate"; pick one vocabulary and use it).

- **NORMATIVE — a record names the passes that produced it.** A §5 record carries `passes`: one entry
  per run that produced a reading, or was attempted and produced none. An entry names the pass
  (`pass_id`), what it was for (`kind`), how it ended (`status`), and the pass's own filed artifact
  (`artifact`, resolved relative to the record). A record's scores are attributable only to the passes it
  names. A job that ran one pass files one pass: the rule is that what ran is filed.
- **NORMATIVE — a filed pass carries its own shape.** A pass filed beside the record (§10.1) carries:
  `pass_id`, the name the record uses for it; `kind` — `scored`, the pass produced a per-dimension score,
  or `confirmation`, the pass read a rule through a second channel to cross-check a reading another
  channel produced, and **how a confirmation reading weighs is the instrument's declaration (§10.1,
  rubric), not this clause's**; `status` — `filed`, or `void` where the pass produced no usable reading,
  in which case `void_cause` is required and `scores` may not be carried, because a pass that was attempted
  and produced nothing is filed as `void`, never omitted; `channel`, the observing channel, and where the
  channel is a model its `provider`, `model` and `family`; `rubric_sha256` and `code_sha256` for the
  instrument that produced it (§10.1, C30); `run_ref`, the host's own identifier for the run, recorded as
  the host's value — this corpus does not interpret it, and no corpus rule may require a host-specific
  name; and `scores`, one entry per dimension the pass observed.
- **NORMATIVE — a record may not name a pass that is not filed.** Every pass a §5 record names is filed
  beside it (§10.1). A record whose instrument required ≥2 passes names fewer only by filing each attempt,
  the voided ones included.
- **NORMATIVE — the check, and what failing it means.** A checker fails a record naming a pass that is not
  filed beside it. **Failing the check is not a defect in a reading already taken:** a closed job's records
  are not re-issued, and the reported fact is *evidence not filed* — which is what the job's own declaration
  already records. A dimension observed by a single pass is labelled as such (Instrument rule 10): one run
  is a sample, not a measurement, and it is not a non-conformance.
- **NORMATIVE — this clause defines no spread.** The range across the passes on one artifact is **not**
  `spread`. `spread` is §10.6's: the `max − min` of N repeated passes of **one fixed input through one
  channel**, per dimension, and it is a property of the channel, not of the artifact under judgement. A
  program that records the range across its own passes on the artifact records it as a labelled instance
  extension (§8/C18); that range is not §10.6's spread, and nothing may be attributed through it as one.
- **NORMATIVE — a dimension below the floor is a violation, and it names the dimension.** Where a dimension
  is scored below `T_dim`, the record carries a violation for it, whose `class` is rule 4's locator and whose
  `dimension` is that dimension's name. The shortfall is required and the remedy is not, exactly as the
  clause above states. A violation that cannot say which dimension it holds against does not attribute — a
  class table built from such violations cannot bind a class to what it was measured on — so where the
  shortfall is **per-dimension** the name is required, and where the shortfall is the pass rule's **mean** the
  violation names no dimension and that absence is not a defect. This is the one place a violation carries a
  dimension: a violation is not required to be per-dimension, and one that is not is complete without it.
- **NORMATIVE — one dimension, one name.** The instrument's dimension list is the vocabulary for the job: a
  record's `dimensions[].name`, a filed pass's `scores[].dimension`, and the dimension key of any channel
  output supplied with the job use those identifiers **verbatim**. This creates no vocabulary: it binds the
  names already required on both sides of a link the record's `passes` already treats as a join, and this
  corpus defines no channel vocabulary and does not invent one. **What is NOT structurally enforced:** the
  instrument side. Nothing here requires the instrument to be machine-readable, so a checker can compare the
  record against its passes and cannot compare either against the rubric; that link is a duty on the author,
  and this line names it as unenforced rather than letting a partial control pass for a whole one.
- **NORMATIVE — a pass that attributes to nothing is an error, not a label.** Where a filed pass names a
  dimension the record does not declare, the checker reports *evidence not attributable* and fails the
  record — the sibling of *evidence not filed*, on the same principle: the record is reported as the job's
  declaration makes it, never a defect read into a reading already taken. A declared dimension that **no**
  filed pass observed is reported as resting on **zero** passes, and that is an error: a score whose
  evidence attributes to nothing is not evidence-backed. Instrument rule 10's single-pass label is unchanged
  for a dimension observed by exactly one pass, because **zero is not one**.

---

## 6. Orchestrator contract (NORMATIVE)

**Inputs:** job id; artifact specification; standard (rubric or tests) with its version; ground
truth reference; pass rule; bounds (cap, budget, wall clock); escalation policy; the Maker (engine,
version, and the feedback forms it can consume).

**Outputs per iteration:** the artifact version, the full Evaluator record (§5), the iteration
count, cost incurred, and the current state.

**Must persist:** every iteration's artifact + verdict + state transition, so a terminal decision
can be reconstructed later without re-running the loop. Retention beyond the loop — the records of
§10 — is part of this obligation, not an optional extra.

**Must enforce:** the cap; the budget; the state machine; role separation; that no artifact
reaches a terminal `accepted` state without a version-matched Evaluator record.

**Must escalate (not decide):** values or doctrine questions; capability gaps; any verdict where
the Buyer and the Specialist conflict.

---

## 7. The three independences (NORMATIVE)

These are distinct requirements. Implementations routinely satisfy one and believe they have all
three.

### 7.1 Role independence (NORMATIVE)

**NORMATIVE:** the Evaluator is not the Maker (§4). This is the independence implementations satisfy first,
and satisfying it alone is the common error — it is one of three.

### 7.2 Ground-truth blindness for judgment (NORMATIVE)

**NORMATIVE:** two blindnesses, both required, plus one thing that must not be built. The **observation
channel must not see the answer** it is being checked against — in a translation loop the back-translator
never sees the source text, so it reconstructs from the target alone and cannot aim at the original. The
**Evaluator scores independent observations, never the Maker's self-report** — a back-translation, an externally
authored test, a measurement — not the Maker's own description of its output. What is **not**
required is an Evaluator blind to the artifact: a scorer that cannot see the work cannot score it.
Implementations must record which channel carried each dimension's observation and confirm that channel had
no access to ground truth.

### 7.3 External-state verification (NORMATIVE)

**NORMATIVE:** after any write to an external system, read the target back and assert equality. A
successful write response is not proof the write landed. Verify the record, not the reply.

   **NORMATIVE — declare what "equality" means.** State the normalization before comparing (for
   instance: compare as strings after stripping surrounding whitespace) and apply it to both sides.
   Any normalization left undeclared is drift you have chosen not to detect. What the comparison must
   reject, at minimum: a different case, a single changed character, a missing or extra cell, and an
   empty range.

   **NORMATIVE — carry a per-run value.** The record written must contain at least one value that is
   fresh on every run (a run id, a timestamp). Without it, a *skipped* write can pass verification
   whenever the target already holds the intended value — an idempotent retry is the common case, and
   equality alone cannot tell *this write landed* from *it was already there*.

---

## 8. Extensions and instances (NORMATIVE)

An implementation may add roles, dimensions, channels, or engines for its own domain, provided it:

1. labels them as instance-specific in every artifact it emits,
2. does not weaken §3, §4, or §7,
3. records them with the job, so a later reader can tell doctrine from local invention.

---

## 9. Compliance checklist (NORMATIVE)

An implementation may ship an artifact only if all are true. Each line carries a **stable identifier**,
never reused and never renumbered (§12), so a citation in a filed audit means the same thing in a
later version. `C1`–`C14` are unchanged from v1.1; `C15`–`C17` close gaps found in the coverage audit
of 2026-09-19; `C18` carries §8's extension discipline; `C19`–`C24` carry the coherence moves of v1.4;
`C25`–`C26` carry proposals 0003 and 0004, ratified by the Principal on 2026-09-19; `C27` carries proposal
0005 (v1.7); `C28`–`C30` carry proposal 0015, ratified by the Owner on 2026-09-22 — the terminal states with
their named outcomes, the readings form of the pass rule, and the instrument in force; and `C31` carries proposal 0016's
fifth clause, `no_artifact`. `C32` carries proposal 0027 (entry B labelled baseline); `C34` carries proposal 0050 as amended (v1.20.0)
— the pass vector, its kinds, and the filing check; `C35` carries proposal 0052 as amended (v1.21.0) — one
dimension, one name; `C36` carries proposal 0053 as amended (v1.22.0) — an iteration names what it sends
back, and a below-floor dimension is a violation that names it.; `C37` carries proposal 0054 (v1.23.0) — the Orchestrator routes, the Architect designs.; `C38`–`C40` carry proposal 0055 as amended (v1.24.0) — seat-to-seat communication. Addressed lines are
appended, never inserted: a line's identifier is cited in filed audits and never changes meaning.

| ID | Clause | Enforces |
|---|---|---|
| C1 | Buyer recorded with provenance on every job; Specialist recorded with provenance only when a bar is in force | §1.1 |
| C2 | ground truth named, with the channel that carries it | §1.2 |
| C3 | Evaluator written before the first generation | §1.3 |
| C4 | pass rule (average + per-dimension floor) fixed before the run and recorded | §3 |
| C5 | cap and budget set; both enforced | §3 |
| C6 | roles separate; no self-scoring anywhere in the path | §4 |
| C7 | observation channel blind to the answer it is checked against; no self-report scoring | §7.2 |
| C8 | Evaluator output validates against §5 | §5 |
| C9 | terminal state is one of accepted / needs_owner / rejected | §2 |
| C10 | external writes verified by read-back | §7.3 |
| C11 | escalation classes defined, the human seat named, and the Orchestrator escalates rather than decides on values, doctrine, capability gaps, and Buyer/Specialist conflict | §2, §4 |
| C12 | every iteration persisted, so a terminal decision is reconstructable | §6 |
| C13 | instruments retained with the artifact: §5's evaluation record (complete), plus an instrument record with the rubric (anchors and provenance), Evaluator identity, ground-truth version, and the control runs from each comparison | §10.1 |
| C14 | a revision is judged against a same-batch control: re-use of the retained instrument supplied and recorded, fresh bounds, the control's noise floor measured (N repeats, spread max−min), per-dimension deltas against that control, and regression distinguished from below-bar — never attributed from a pooled average, and a run without a same-batch control is uncontrolled | §10.2 |
| C15 | the record written on any external write carries a value fresh on every run (a run id, a timestamp), and equality is compared under a normalization declared before comparing | §7.3 |
| C16 | the Orchestrator persists each iteration's artifact, verdict and state transition; only the Orchestrator applies the pass rule, cap and escalation; and it enforces the cap, the budget, the state machine and role separation — with no artifact reaching terminal `accepted` without a version-matched Evaluator record | §6 |
| ~~C17~~ | **RETIRED** — superseded by structural enforcement in `job-packet.schema.json`: while `ratified: false` the must-ask fields must be absent, which a schema makes impossible to violate rather than merely auditable | §12 (stable IDs) |
| **C18** | instance extensions are labelled as instance-specific in every artifact they emit, do not weaken §3, §4 or §7, and are recorded with the job | §8 |
| **C19** | ground truth is recorded with its version and its hardness grade, the grade supplied per job and never defaulted, and no dimension claims ground truth harder than its channel carries | §1.6 |
| **C20** | the frame is supplied as a Principal-authored mandate with scope and exclusions; the dimension set is authorized by it, a dimension it neither authorizes nor excludes is escalated as a frame question rather than scored, and no excluded dimension is scored | §1.7 |
| **C21** | where the mandate names a source of record read-only, the artifact is submitted against it and the source is not revised by the Maker | §1.7 |
| **C22** | every observation channel declares a measured spread (N repeated passes of a fixed input, `max − min` per dimension), recorded with the job; no delta inside that spread is reported as improvement, regression or a reason for a verdict; and the spread is re-measured when a §10.3 trigger fires | §10.6 |
| **C23** | a corpus, rubric or doctrine that judges other work is scored against its own Principal-authored mandate, and while that mandate is unratified no dimension scoring it against its purpose is `pass` | §1.7, §12 |
| **C24** | a retained instrument is re-derived rather than re-used when any §10.3 trigger fires — Buyer, Specialist's standard, ground truth, Evaluator, mandate — and the instrument change is recorded with the revision | §10.3 |
| **C25** | the Maker is a supplied, recorded choice with the feedback forms it can consume named; a violation beyond its capability escalates as a capability gap rather than being iterated; and suitability is demonstrated by the next evaluation, not asserted | §4.1 |
| **C26** | every violation states the shortfall with the observation and a class; a remedy is included where the Evaluator has an insight into rectification and its absence is not a defect in the record; a fabricated remedy is itself a violation | §5 |
| **C27** | every dimension carries the observation its score rests on, produced by the channel the dimension names; an empty or missing `observation` means the dimension could not be judged — a forced `needs_owner`, never a synthesised, averaged or below-floor score | §5 |
| **C28** | the record carries a terminal state (accepted / needs_owner / rejected) **and** the outcome it exited under (accepted / rejected / needs_owner / census / no_observation / no_artifact); a `no_observation` job's terminal state is `needs_owner`; a `no_artifact` job's terminal state is `needs_owner`; a readings-only job's terminal state is `accepted` with outcome `census` | §2 |
| **C29** | a job with no Specialist named at the outset declares `mode: readings`, supplies no thresholds and may not score; its pass rule is the readings form; outcome `census` requires every readable dimension to conform and terminal `accepted`; a `does not conform` reading exits `needs_owner` with outcome `needs_owner`; and it may not produce `rejected` | §3 |
| **C30** | the record names the instrument in force — its version, and the hash of the rubric and the code that implements it — and that instrument is retained with the artifact; the manifest names it, so it is hashed like every other retained instrument | §5, §10.1 |
| **C31** | a run in which the Maker produced no artifact records outcome `no_artifact` with terminal state `needs_owner`; the test is structural, never a character count; the record names which side failed; and a null iteration is not counted against the cap and does not displace the incumbent | §2 |
| **C32** | an `entry: B` job is a labelled baseline (§1.5); it is legal only if `reads_before_freeze` names the reads that could reveal a defect and states they came after the rubric was frozen; C3 is not satisfied by the artifact already existing; a live artifact that fails is `rejected` plus an Owner disposition and is not deleted; a fix is a new job; procedure is Instrument Entry B and this line does not restate it | §1.5 |
| **C33** | a scored job carries a frame before generation: `ground_truth` rows with source, version, and hardness; `mandate_ref` as doc plus version; a non-empty `escalation` route. Readings jobs are not subject to this line. Feedback forms, the dimension set, retained-instrument reuse, task classes, and escalation classes are not structurally enforced | §1.6, §1.7, §3 |
| **C34** | a §5 record names the passes that produced it; every named pass is filed beside it with its declared shape and kind, a voided attempt is filed as `void` with its cause, and a record naming a pass that is not filed fails; a dimension observed by a single pass is labelled, not failed; and the range across an artifact's passes is **not** `spread`, which §10.6 owns as a channel property measured on one fixed input | §5, §10.1 |
| **C35** | the instrument's dimension list is the job's vocabulary: a record's `dimensions[].name`, a filed pass's `scores[].dimension` and a channel output's dimension key use those identifiers verbatim; a pass naming a dimension the record does not declare fails as *evidence not attributable*, and a declared dimension no filed pass observed fails as resting on zero passes — zero is not one, and rule 10's single-pass label is unchanged; the instrument-to-record link is a duty on the author, not structurally enforced | §5 |
| **C36** | a `regenerate` verdict carries at least one violation, because an iteration that names nothing it is tasked with is not an iteration; and a dimension scored below `T_dim` carries a violation whose class is rule 4's locator and whose `dimension` names it, while a violation whose shortfall is the pass rule's mean names no dimension and is complete without one; a `regenerate` with no violation, or a below-floor dimension with no violation naming it, fails the record | §4, §5 |
| **C37** | the job records who holds the Architect seat, and where the Orchestrator holds it the double-hat is declared; the Architect's decisions are recorded apart from the Evaluator's scores, and no score is attributed to the Architect; the artifact carried forward is the one rule 12's test selects from the scores, never the Architect's pick; readiness for the Maker is recorded as the pinned inputs, the specified fixes and the absence of any contradiction with the bar, never as a predicted pass; each iteration's input — the artifact handed over, by hash, and the defects and solutions sent with it — is recorded with the seat that decided it, and the Orchestrator verifies that what it delivered is what was decided | §4 |
| **C38** | the Maker and the Evaluator are dispatched only by the Orchestrator and return only to it; no message passes between them directly; no seat instructs the Evaluator on a score during a run, and a change to the instrument is recorded as a new instrument | §4.2 |
| **C39** | no Maker message contains held-out material, which is only material the Maker cannot see; findings reach the Maker and the Architect with every known defect and its measurement, an expected value on a fixture the Maker can see included; every built Maker message is checked against held-out material before dispatch, with the method, the result and who ran it recorded, and where the Orchestrator authored both the dimension set and the held-out material the Evaluator or the Architect also runs the check; every seat other than the Evaluator, the author and the custodian that has seen held-out material is recorded | §4.2 |
| **C40** | if the job requires approvals, each is recorded with approver, time and zone, channel, scope, words or labelled paraphrase, and whether it was direct or relayed; the form is the job's declaration (standing/kickoff grant, acting-channel yes, or allowed relay); jobs that declare no per-act approval need none beyond kickoff frame, budget and bounds; a form the job did not declare authorizes nothing | §4.2 |

**NORMATIVE — the coverage invariant.** Every NORMATIVE rule in this document has exactly one
disposition, and the disposition is published with the corpus in `EDI-RULE-INDEX.json`:

- **`LINE`** — enforced by an addressed line in §9. A deployment is audited for it.
- **`SCHEMA`** — enforced structurally by a named schema or hook. Stronger than a line: a prompted
  model promises, a configured instance enforces. A rule enforced this way does not also need a
  line, and adding one would be the weaker control wearing the stronger one's clothes.
  **NORMATIVE — a partial enforcement is not a disposition.** A rule whose structural control does not cover the rule may not carry `SCHEMA` as its disposition. The index names what is enforced and what is not. A control that covers part of a rule is a control for part of a rule.
- **`NONE`** — a rule about this corpus rather than about an implementation: a definition, a
  rationale, an interface description. Not separately enforceable, and naming it as such costs
  nothing that was ever collectable.

**A NORMATIVE rule with no disposition is a defect in this corpus**, reported as a defect rather
than absorbed. A version that does not publish its dispositions has not run the invariant.

**State at v1.27.0.** Of **86 in-scope NORMATIVE rules**:
**74 are `LINE`**, **2 are `SCHEMA`**, **10 are `NONE`**,
and **0 remain uncovered**.

An implementation that cannot tick a line must report which line it failed and why, rather than
proceed.

---

## 10. Retention and revision — the artifact's life after the loop

### 10.1 What is retained (NORMATIVE)

**NORMATIVE:** two records are retained with the artifact. They are separate objects, and they are not
merged: the **evaluation record** is §5's, and the **instrument record** holds the rest.

**NORMATIVE — the passes are retained with them.** Each pass a record names is filed beside it with its own
shape (§5). The two records below are what is retained *as records*; the passes are the observations those
records rest on, and they are retained for the same reason — a reader must be able to reconstruct which runs
produced the numbers, from which channel, and with what per-run result. A record whose named passes are not
filed reports *evidence not filed* (§5, C34).

**The evaluation record is §5's record, retained unmodified and complete** — exactly the fields §5
defines (the passes that produced it, dimensions with their scores *and observations*, violations, the pass
rule in force,
`channel_blind`, `ground_truth_access`, `ratified`), with none dropped and none added. The retention
date belongs to the instrument record, not to §5's record.

**The instrument record** — a distinct object — must contain, at the point custody is claimed:

| Contains | Detail | What breaks without it |
|----------|--------|------------------------|
| **Rubric, versioned** | dimensions, anchors, the pass rule, and its provenance (§1 step 1: Buyer, Specialist, where the standard lives) | the standard cannot be re-established or re-derived: a later reader can see that a bar was applied, but not what it was or on whose authority |
| **Evaluator identity** | provider, model id, version or date, prompt, and scoring protocol (batch composition, dimension order) | a later re-run measures a different instrument and reports the difference as a change in the artifact |
| **Ground-truth reference, versioned** | the source of record the Evaluator judged against | comparison is invalid the moment the source moves |
| **Control runs** | the fixed control input, with N and the per-dimension spread, recorded for **each comparison** — history retained, not only the latest. Required with every revision, from the first comparison onward; never a precondition of first accept | a stored number gets compared against instead of a contemporaneous one, and the instrument's drift is reported as change in the artifact |
| **The instrument in force** | the version of the instrument this scoring was made under, and the sha256 of its rubric **and of the code that implements it** — the runner is half the instrument, because a re-run holding the same rubric and a different runner is a different instrument | a reader cannot tell which instrument produced a reading, so no re-run can be attributed and no §10.3 trigger can be evaluated. Rule 10 of the operating instrument requires the code kept hashed with the rubric; the corpus's own instrument satisfied that only from v1.10 |

**NORMATIVE — the accepted-risk ledger is the violations, not the dimensions.** Because a dimension
with no observation fails (§5), every dimension on an accepted artifact was scored and its observation recorded. What an
accepted artifact genuinely carries forward is therefore its **accepted violations**: the items
knowingly shipped, with the remedy — where the Evaluator supplied one — declined or deferred, and the
reason. That is the artifact's institutional
memory of what was traded away. Dimensions the rubric never covered are a different matter entirely —
they are unknown until a real failure exposes one, and the response is a new dimension, not a ledger
entry.

### 10.2 Revision is the loop, re-run (NORMATIVE)

**NORMATIVE:** a revision runs the retained instrument on the revised artifact, and the comparison of
record is that run against a **control run of the accepted version in the same batch** — dimension by
dimension, under the role purity of §4 (the reviser does not judge). A stored score is not a comparison.

**NORMATIVE:** re-use of a retained instrument is itself a must-ask value, supplied per revision job and
recorded with it. A revision that silently inherits the instrument repeats the failure §3 forbids: the
job's inputs stop being reconstructable, and the result cannot be attributed to the artifact.

**NORMATIVE:** the revision job carries **fresh bounds**. Its iteration cap, budget, and pass rule are
supplied and recorded for the revision; the original job's cap does not extend to it.

**NORMATIVE — regression is measured against the control, not against a stored score.** A dimension that
falls below the control's contemporaneous value on that dimension, by more than the control's own spread,
is a **regression**: the change broke something the accepted version did better. A dimension below the bar
in both is merely unfinished. Both are recorded the existing way — as classified violations with observations
and, where the Evaluator has one, a remedy — on the revision's evaluation record; the verdict stays with the pass rule, which a regression
does not assign, and regression adds no terminal state: the machine of §2 is unchanged, and `rejected`
stays reserved for work below the reject floor.

**NORMATIVE — a revision carries a control in the same batch. Never compare against a stored number.**
Evaluator output is not stable across time. Measured with prompt, model id and input held identical: an
instrument that scored a document 8.64 returned 8.33, 8.14, 8.00, 7.86 and 8.39 when re-run on
byte-identical input — mean 8.14, spread 0.53, the published figure above the whole re-measured range and
the shift between sessions (0.50) nearly the whole within-session spread (0.53). Comparing against a
stored score therefore reports the instrument's drift as change in the artifact. A run that compares against a
stored score is uncontrolled: it may not serve as a revision's comparison of record. Every revision
carries a **control** — the same instrument, in the same
batch, on a fixed input that was already accepted, normally the artifact's own accepted version.

**NORMATIVE — the control is measured, not assumed.** The control is N repeated evaluations of the fixed
input, recorded with the comparison, giving N and the per-dimension spread (`max − min`). N is a supplied,
recorded value, never defaulted; the measurement behind this rule used N = 5. Increase N where the spread
is wide, and record the increase. Two batches **agree** when, on every dimension, their means differ by no more than the larger of the two
per-dimension spreads; until they agree, the larger per-dimension spread stands as the tolerance.

**NORMATIVE — a run without a same-batch control is uncontrolled, and may not attribute.** It may still be
scored and may still reach any terminal state; the pass rule does not require a control. What it may not do
is stand as a revision's comparison of record: no dimension may be reported as improved or regressed, and
no accept may cite a stored score as its reason.

**NORMATIVE — never attribute change from a pooled average.** An average may be reported as a run's
headline, but improvement or regression may not be claimed from it, because offset movements cancel: a
revision can gain three points on one dimension and lose one and a half on another and still report a
fraction of a point of gain. Attribution is per dimension against the control, plus which violation classes
appeared, disappeared, or persisted — a class present in every run of a cell is structural, not noise.

### 10.3 Revalidation triggers (NORMATIVE)

**NORMATIVE:** a retained rubric is a statement about a frame, and frames move. Re-derive the rubric —
do not re-use it — when any of these change:

- the **Buyer**, or the constraints they named;
- the **Specialist's standard** (a new regulation, a new craft consensus, a superseding reference);
- the **ground truth** (§10.1);
- the **Evaluator** (deprecated model, changed version, unavailable provider).

**NORMATIVE:** when the instrument changes, record that it changed, with the revision. A comparison
across instruments measures the instruments, not the artifact. A rubric retained past a trigger without
re-derivation stops being a standard and becomes a **drift anchor**: it holds the artifact to a frame
nobody has agreed to anymore.

### 10.4 Two governance objects (NORMATIVE)

**NORMATIVE:** the same two records govern two different things, and they fail differently.

- **Pipeline governance.** The retained Evaluator and rubric are what keep every unit judged the same way
  across runs — same dimensions, same anchors, same protocol, same versioned standard. The live risk is
  **instrument drift**; the batch's control spread is the working tolerance, and drift is monitored by
  re-running the retained instrument periodically against a fixed, known input so the pipeline's
  standard stays comparable to itself.
- **Artifact lifecycle governance.** The retained rubric and evaluation record are what let a revision
  be judged against what was accepted. The live risk is a **standard that changes without anyone
  deciding it**.

### 10.5 Minimum viable retention (NORMATIVE)

**NORMATIVE:** retention was stated permissively at first — keep the rubric *or* the Evaluator's identity, *or both*.
This section deliberately hardens that, and names the minimum instead of assuming the full set:

- **Rubric + evaluation record: indivisible and mandatory.** An Evaluator without a rubric has nothing to
  execute; a revision without the accepted version to re-run as a control cannot detect regression (§10.2).
- **Evaluator identity: required whenever the same instrument will be re-run.** Without it a re-run is a new
  instrument, and its result is not comparable to the old one.
- **Ground-truth version: required for any comparison to be valid at all.**

**NORMATIVE:** the minimum is mandatory for any job that claims custody, and no job may claim it while
retaining less. A job that retains less does not claim it: without Evaluator identity a later score is a
fresh judgment rather than a governance check, and it must be labelled as one.

### 10.6 The tolerable spread belongs to the channel, not to the artifact (NORMATIVE)

**NORMATIVE:** every observation channel declares its own **spread** — the `max − min` of N repeated
passes of one fixed input through that channel, per dimension — and the declaration, with N, is
recorded with the job. A channel's spread is a property of the channel: its instrument, its prompt,
its model version, its batch composition. It is not a property of the artifact under judgement.

**NORMATIVE:** a delta inside the channel's declared spread is **not a result**. It may not be
reported as improvement or regression, may not be cited as a reason for a verdict, and may not be
carried into a comparison of record. A channel whose spread has never been measured has no tolerance
at all: it may score, and the score stands for that run, but nothing may be **attributed** through it.

**NORMATIVE:** the spread is re-measured whenever a §10.3 trigger fires — the Buyer, the Specialist's
standard, the ground truth, or the Evaluator changes. A spread carried across a change of Evaluator is one
channel's tolerance worn by another, and the comparison it licenses is a comparison of instruments.

This is separate from §10.2 because the two measurements answer different questions. §10.2's control is
per comparison: it measures the batch a revision was judged in, so that the comparison is valid within
that batch. This section is per channel: it states what size of movement the channel produces on its
own, with nothing changing in the artifact. Both are `max − min`. A tight batch control inside a wide
channel is a precise measurement of noise, not a sign of change.

---

## 11. Related documents

- Map: `README.md` · On-ramp: `EDI-QUICKSTART.md` · Seats: `EDI-PLAYBOOK.md`
- Frame: `EDI-MANDATE.md` · Job form: `EDI-OPERATING-INSTRUMENT.md` (tier 4)
- `EDI-RULE-INDEX.json` · The doctrine, which wins any conflict: `../DOCTRINE.md` · The record: custody/v1 (https://github.com/evaluatordriven/custody). The v1.12 full text and the change history are held in the private working corpus; the short front wins.


**Implements.**

This table cites **up**, to the rules of `../DOCTRINE.md` it carries (doctrine IDs, `D…`). It belongs to this file: when an id here changes, update the table in the same commit. `../tools/check_downhill.py` checks that every id here exists, every doctrine id it names exists, and every doctrine rule is carried somewhere. Basis: *v0.1 tag* means the doctrine's own v0.1 citation named this id; *added 2026-11-02* means it was added in review and confirmed by the Owner on 2026-11-02.

| This file | Carries | Basis |
|---|---|---|
| `C1` | D2.1, D2.2, D2.3, D2.4, D2.no-provenance | added 2026-11-02 |
| `C2` | D4.4 | added 2026-11-02 |
| `C3` | D4.2, D5.step.1 | added 2026-11-02 |
| `C4` | D4.1, D4.6, D5.step.1, D5.step.5 | added 2026-11-02 |
| `C5` | D4.10, D5.step.6 | added 2026-11-02 |
| `C6` | D3.maker-never-judges, D4.3 | added 2026-11-02 |
| `C7` | D4.3, D5.step.3 | added 2026-11-02 |
| `C8` | D3.Evaluator, D5.step.4, D3.reader | added 2026-11-02 |
| `C9` | D4.10, D5.exit.accepted, D5.exit.needs-owner, D5.exit.rejected | added 2026-11-02 |
| `C11` | D4.11, D5.human | added 2026-11-02 |
| `C12` | D4.12, D5.move.4, D7.record | added 2026-11-02 |
| `C13` | D4.12, D7.record | added 2026-11-02 |
| `C16` | D3.Orchestrator | added 2026-11-02 |
| `C19` | D4.4 | added 2026-11-02 |
| `C22` | D4.5 | added 2026-11-02 |
| `C25` | D3.Maker, D4.8 | added 2026-11-02 |
| `C26` | D4.7 | added 2026-11-02 |
| `C27` | D4.7 | added 2026-11-02 |
| `C28` | D5.exit.accepted, D5.exit.rejected, D5.outcome.no-observation | added 2026-11-02 |
| `C29` | D5.outcome.census | added 2026-11-02 |
| `C30` | D4.12, D6.4 | added 2026-11-02 |
| `C31` | D5.outcome.no-artifact | added 2026-11-02 |
| `C32` | D5.entry.B | added 2026-11-02 |
| `C37` | D3.Architect, D3.Orchestrator, D3.routing, D5.step.5 | added 2026-11-02; D3.Orchestrator, D3.routing and D5.step.5 added 2026-11-02 (v0.2.1) |
| `C39` | D3.held-out, D5.step.5 | added 2026-11-02 (v0.2.1) |
| `C40` | D5.human | added 2026-11-02 (v0.2.1) |
| `§0` | D7.custody | added 2026-11-02 |
| `§1` | D4.1, D5.core-sequence | added 2026-11-02 |
| `§1.1` | D2.bar, D3.Buyer, D3.Specialist | added 2026-11-02 |
| `§1.2` | D4.4 | added 2026-11-02 |
| `§1.4` | D5.move.2 | added 2026-11-02 |
| `§1.6` | D4.4 | added 2026-11-02 |
| `§2` | D5.step.2, D5.step.6 | added 2026-11-02 |
| `§3` | D4.6, D5.step.5 | mixed: D4.6 tag, D5.step.5 added |
| `§4` | D3.maker-never-judges, D3.disposer-never-judges, D3.Owner, D3.Architect, D3.Maker, D3.Evaluator, D3.Orchestrator, D3.adjudicator, D3.test-author, D3.reader, D3.holder, D3.routing | added 2026-11-02; D3.routing added 2026-11-02 (v0.2.1) |
| `§5` | D4.7, D5.step.4 | mixed: D4.7 tag, D5.step.4 added |
| `§6` | D3.Orchestrator | added 2026-11-02 |
| `§7.1` | D5.move.3 | added 2026-11-02 |
| `§7.2` | D5.step.3 | added 2026-11-02 |
| `§10.6` | D4.5, D4.6 | v0.1 tag |
| `§12.1` | D5.entry.B | added 2026-11-02 |
---

## 12. Governance of this corpus (NORMATIVE)

Agents propose; Owner ratifies; version bump regenerates derived artifacts; superseded text stays marked. **C-line IDs are stable** — never reused or renumbered; retired lines stay reserved.

**A superseded term.** `needs_human` was renamed `needs_owner` (v1.6). Old name in filed records keeps that meaning; never reuse `needs_human` for anything else.

**A second superseded term.** `evidence` / `evidence_channel` were renamed `observation` / `observation_channel` (v1.8). Old names in filed records keep those meanings; never reuse them for the scored fields. (Corpus “evidence, not instructions” labels and ordinary English “evidence” are unchanged.)

**This corpus is a labelled baseline** unless its version header names an instrument independent of its authors that judged it; a baseline is citable as the standard and is not available as ground truth for its own successor. There is no Evaluator above this corpus and none is to be built — the regress terminates at the Principal, by declaration, because a check above the checker inherits the same problem one level up.

**The corpus has a mandate (§1.7).** `EDI-MANDATE.md` is the Owner’s frame for what this corpus must and must not do (closes the recursion). **Ratified and in force** (2026-09-20; short front Owner-ratified 2026-09-24). While a mandate is unratified, no dimension scoring a corpus against its purpose may be `pass` — that control does not apply here while ratification holds.

**The corpus has an operating instrument, and it is in force.** `EDI-OPERATING-INSTRUMENT.md` (v1.13) is tier 4 in `../AUTHORITY.json`: it **loses to this document** on roles, states, schemas, and the pass rule. Owner ratifies changes; version bumps regenerate derived artifacts in the same pass. It is retained hashed and named in the manifest (`instrument-v1.13`).

### 12.1 Entry B baseline (NORMATIVE)

**NORMATIVE — entry B is a labelled baseline (C32).** An `entry: B` job is legal only if `reads_before_freeze` names the reads that could reveal a defect and states they came after the rubric was frozen. C3 is not satisfied by the artifact already existing. A live artifact that fails is `rejected` plus an Owner disposition; the machine does not delete it. A fix is a new job. Procedure: Instrument Entry B. This line does not restate R1–R4.
