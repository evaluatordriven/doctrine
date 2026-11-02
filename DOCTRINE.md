# Evaluator Driven

**E-DI: Evaluator-Driven Iteration. A doctrine for delegating work so that quality survives.**

Version 0.2.1 · candidate 2026-11-02 (v0.2 ratified 2026-11-02; v0.1 ratified 2026-10-25) · Steve Moitozo II · Licence: CC BY 4.0

---

## 0. In one paragraph

**Can I trust our name to this work?** A decision-maker asks that before the company's name goes on work an AI agent produced. A practitioner asks the same of their own name. Evaluator Driven exists so the honest and confident answer
can be yes.

Work made by an agent, a model or a person is trusted only as far as it has been judged. Evaluator-Driven work is assessed against a standard that was set before the work began: the bar.
It's judged by a qualified Evaluator whose ability to properly judge work has been tested AND who did not
produce the work itself. And the record of the work can be checked by anyone who needs to audit it. The evaluation drives the
work. It’s not simply paperwork after the fact.
When the work falls short, the Evaluator reports the deficiencies, with proof. The Maker then revises
against exactly that. The Orchestrator ensures the loop stops in a named way, within bounds set in advance, and that the person accountable for the outcome
keeps the decisions only they can make. And their decision gets written beside the verdict, never over it.

---

## 1. Why this exists

**Who it is for.** Three readers:

- the **decision-maker**, who sanctions handing a kind of work to AI and must put the company's name on the result;
- the **practitioner**, who already uses AI and must put their own name on what it helped make;
- **the practitioner's AI agent**, which needs a published standard to work to, not its own improvisation.

Two parties are not readers but **authorities**: the **Buyer**, whose fitness test the work must pass,
and the **Subject-matter Expert**, whose quality test it must pass.
Their standard of “well done” is the one that counts.

**The pain is one defect with three faces: quality that cannot be accounted for.**

- **The signature.** You cannot put a name on work whose quality you cannot account for.
- **Guilt.** The practitioner got a good result and cannot say what they did to get it. It feels as if the
  AI produced quality by accident, so they keep quiet about how the work was made.
- **Delegation that does not survive.** A method that lives in one person's head dies when it is handed
  to a colleague, a team or an agent. Nobody needs a standard to do their own work; you need one the
  moment somebody else has to do it too.

**The decision-maker's question is a comparison.** Not "is AI good?" but "will the result be at least as
acceptable as what it replaces?" And the decision-maker wants to see that for themselves, not take it on faith.
Evaluator Driven answers it the only honest way. Hold the work to the bar you would hold your people's
work to: the same Subject-matter Expert's standard, the same Buyer's test. Set that bar before the work begins and have the work judged by an Evaluator who did not make it. Work that passes has been judged to meet that bar, and the record lets
you check it yourself. Work that does not goes back to the Maker or comes to you, the Owner.

**The acceptance principle.** In the Owner's words:

> If the work passes the quality test of a subject matter expert and the fitness test of an end-user,
> shouldn't it be acceptable regardless of the tools used to produce it?

That is the stricter claim, not the softer one. A standard that judged only methods could be satisfied by
using approved tools badly. A standard that judges the work against named tests leaves nothing to
hide behind, and makes admitting the tool a detail rather than a confession.

**The big bet.** The same job, run inside a well-managed and well-judged loop, beats the same job run without one. The corollary, if the bet holds, is what makes it matter: quality comes from the judging and detailed feedback more than from the size of the Maker.
So, a modest, cheap, even locally hosted model inside the loop can produce work that passes the bar. This
is why Evaluator Driven exists. §8 sets out the evidence so far, and what would settle it.

**Why now.** Generation used to be the expensive step, so outputs were checked carefully. Now producing work is close to free, and the binding constraint is the judging. The work is still checked. What changes is that the checking itself can now be delegated with confidence, once it meets a standard of its own: a bar set first, an Evaluator tested before it serves, and a record anyone can audit. The person who gets quality from agents is the one who
invests more in the Evaluator and loop discipline than in the Maker. Delegation fails in known ways. When "done" and "good" are unclear, even human delegation suffers. The work cannot be checked fairly. The worker lacks the skill. The feedback is late or useless.
Or the work is graded by its Maker, or by judges who know neither the Buyer's need nor what masterful
work looks like.

**The practice is old; the name is new.** Good editors, managers and craftsmen have always defined done
before handing off. They checked the work against the standard, not the worker's account of it. They sent
it back with specific feedback, and kept the final call with the person whose name is on it. Agents work
without you in the room, so your standards survive your absence only if they are written down.

**Neighbouring methods cover part of the ground.** A specification tells an agent what to build; it does
not show that the agent built it. A proof covers what a formal specification can state; most work (prose,
translation, design, data, judgement calls) cannot be proved. Evaluator Driven is for the rest.

---

## 2. The grounding axiom: the Evaluator is a proxy, never a principal

Before any mechanics, one question governs everything:

> **Who is buying this output, and which master of the craft approved the bar?**

Quality is not a platonic property a rubric can point at. It lives with two authorities, and the bar sits
where they meet:

- the **Buyer** defines fitness for purpose: does this solve my problem, within my constraints?
- the **Specialist**, the subject-matter expert, defines excellence: would a master of the craft accept
  this?

<a id="D2.bar"></a>They can pull against each other, and judgement must hold both. **The bar is the intersection of the Buyer's need and
the Specialist's standard.**

So an Evaluator holds authority on loan. Its standard must carry provenance to both, written down as four
facts:

1. <a id="D2.1"></a>who the Buyer is;
2. <a id="D2.2"></a>what they need, and which constraints they named;
3. <a id="D2.3"></a>whose standard of excellence is borrowed;
4. <a id="D2.4"></a>where that standard lives, versioned.

<a id="D2.no-provenance"></a>A rubric that cannot answer those four is a preference wearing a score. **No provenance, no authority.**

<a id="D2.frame"></a>Two consequences follow. **You can delegate the doing; you can never delegate responsibility for the
standard.** And **the doctrine improves how well work meets its frame; it does not set the frame.** Values,
priorities, risk appetite and taste belong to the Owner.

---

## 3. The seats

<a id="D3.maker-never-judges"></a>A seat is a responsibility, not a person. One person or model may hold several seats if that is
disclosed, with two exceptions that are never waived: **the Maker never judges its own work**, and
<a id="D3.disposer-never-judges"></a>**whoever disposes of the work does not judge it.**

| Seat | Does | Never does |
|---|---|---|
| <a id="D3.Owner"></a>**Owner** | Owns the outcome. Ratifies the frame. Sets values, priority and risk appetite. Decides what the loop cannot. May override a verdict, recorded as a disposition beside it. | Rewrites a verdict. |
| <a id="D3.Architect"></a>**Architect** | Defines done and good, writes the standard, sets the thresholds and bounds, and builds the instruments. Decides what gets built next, what the next round is handed, and whether a job is ready to go to the Maker. | Writes or tunes the standard after seeing a draft. Scores the work, or picks which version carries forward by preference. |
| <a id="D3.Buyer"></a>**Buyer** | Is the one whose problem is being solved. States the need and the constraints. | — |
| <a id="D3.Specialist"></a>**Specialist** | Supplies the standard of excellence for the craft. | — |
| <a id="D3.Maker"></a>**Maker** | Produces the work and revises it against classified feedback. | Judges its own output, or produces the observation it is judged by. |
| <a id="D3.Evaluator"></a>**Evaluator** | Alone scores the work against the frozen standard, through a channel the Maker did not produce, and returns a structured verdict. | Produces or repairs the work. |
| <a id="D3.Orchestrator"></a>**Orchestrator** | Runs the loop: assembles, delivers and checks the Maker's input, applies the pass rule, enforces the cap, escalates, and keeps the record. | Writes the work or scores it. Chooses what an iteration receives, or rules on readiness. |

<a id="D3.routing"></a>**The Architect designs; the Orchestrator routes; the Evaluator alone scores.** Three decisions belong to the Architect: what to build next, what goes into the next round's packet, and whether a job is ready to hand to the Maker. Readiness is a design check with three conditions: every required input file is pinned, the fixes are specified, and nothing requested contradicts the bar. Readiness is never a prediction that the draft will pass; predicting a pass is scoring, and scoring belongs only to the Evaluator. Which version carries forward is determined by the carry-forward rule (§4, rule 9) from the Evaluator's scores, never by the Architect's preference. The Orchestrator puts the packet together, delivers it, and verifies that what was delivered matches what was decided; it neither chooses the packet's contents nor rules on readiness, while retaining the pass rule, the cap, escalation, and the record.

<a id="D3.held-out"></a>**Held-out material.** Held-out material means only material the Maker cannot see: control and planted cases kept outside the Maker's reach, the expected answers on them, and the Evaluator's raw evidence from them. Something the Maker can already see is not held-out merely because the instrument also checks it; an expected value on a fixture in the Maker's own repository is not held-out. Held-out material never goes to the Maker from any seat.

**An Evaluator seat is described by what it does and what holds it.** What it does:

- <a id="D3.reader"></a>**The reader** scores or reads each dimension against the frozen bar, through a channel the Maker
  did not produce. This is the usual form.
- <a id="D3.adjudicator"></a>**The adjudicator** is an Evaluator who rules on a disagreement between Evaluators. It reads the work
  itself (the code, the text). An adjudicator never resolves a split by averaging.
- <a id="D3.test-author"></a>**The test author** writes an independent channel: a test, a planted case, a task for a reader who has
  never seen the work. The test author is not the Maker and does not see the Maker's reasoning.

<a id="D3.holder"></a>What holds it: a **person**, a **model** or a **script**. Each is tested the same way (principle 5): in every
batch it reads a case that should pass and one that should fail. A model is disclosed with its family (below). A
script is the cheapest Evaluator; put it in front of the others.

<a id="D3.family"></a>**On families of models.** Seats may share an engine, a vendor or a model family. What may not happen is
an Evaluator seat biased toward the Maker's family. Two models from one family tend to share blind spots, and an Evaluator that shares the Maker's blind spots is the Maker grading itself by another route. So:

- at least one Evaluator differs from the Maker in model family;
- on every dimension, the Maker's family holds no more than half of the Evaluators;
- every seat's holder is disclosed, and an undisclosed model family is read the least favourable way: as the Maker's.

---

## 4. Principles

1. <a id="D4.1"></a>**The bar comes first.** Done and good exist before the first draft. A definition written after seeing a draft is an anchor on the draft, not a standard. For existing work (Entry B), the bar comes before the judging instead, and declaration order stands in for blindness.

2. <a id="D4.2"></a>**Build the Evaluator before the Maker produces, and show it catching a bad case.** Write the instrument, run it on a case it must fail (the work's own real failure if there is one, otherwise a deliberately bad case), then freeze and hash it. If you have never seen the instrument say no, its yes means nothing.

3. <a id="D4.3"></a>**The Maker never grades its own work, and never produces the observation it's graded on.** The
   Evaluator sees the work. The observation comes through a channel the Maker did not produce and cannot
   easily fake. Examples: tests the author did not write; a back-translation by a reader who never saw the
   source; a stranger following the instructions cold.

4. <a id="D4.4"></a>**Anchor to ground truth, and name how hard it is.** Judge against the source and known-good
   references, never the Maker's working copy. Ground truth comes in kinds: an invariant, a document of
   record, a prior. No dimension may claim more certainty than the channel that carries it.

5. <a id="D4.5"></a>**Judges are tested too.** Every Evaluator, in every batch, reads at least one case that should pass and
   one that should fail. The model serving a seat is part of the instrument, and its strictness,
   stability and cost are measured, not assumed. A verdict rests on at least two scored runs; one run is a
   sample. A judge that is never tested can name a defect and then excuse it, or report checking text that is not there; planted cases are how you find out. Put cheap deterministic checks (length,
   structure, required elements) in front of the judge: they catch what a lenient judge waves through.
   And measure each Evaluator's spread on identical input: a reading that changes between identical runs is
   the instrument's noise, so only what holds across runs counts as a finding.

6. <a id="D4.6"></a>**Disagreement is information; never average it away.** A scored pass needs both an average threshold and a floor on every dimension, because an average alone lets a fatal defect hide. Readings from
   different Evaluators are never averaged: where they agree within the channel's measured spread, the
   agreement is the reading; where they split, the split is shown and adjudicated. A disagreement between
   the work and the standard is traced to its cause, never written off as a bad Maker. Either the work missed the
   standard, the standard moved, the dimension was never authorized, or the frame itself is at fault.

7. <a id="D4.7"></a>**Feedback carries the shortfall, always; a remedy only with real insight.** Say how the work falls
   short and quote the evidence. Offer a remedy where the Evaluator genuinely sees one. An invented remedy is
   worse than none; a measured remedy withheld is also a defect. A remedy points the way; it is never the fix. The Evaluator does not write the revision, and the Maker owns how the shortfall is fixed. An Evaluator that writes the fix grades its own work on the next round. A score with no observation behind it is not
   a score. And "could not observe" is a different fact from "found missing": what an Evaluator cannot see
   is recorded as unobserved, never as absent.

8. <a id="D4.8"></a>**Feedback must be able to change the next version, or do not loop.** If the Maker cannot act on the
   judgement, iteration is theatre. Identical outputs mean the influence channel is dormant, not weak. A
   capability gap escalates; it is not retried.

9. <a id="D4.9"></a>**Inside a loop, a change answers only what the Evaluator reported.** Everything else waits for the next
   bar. Carry the best work forward: a revision replaces the incumbent only if it is better on at least one
   dimension and worse on none. That mechanical test on the Evaluator's scores, never the Architect's preference, selects which version carries forward. When the loop continues, the next round is handed the best artifact produced so far, every known defect with its measurement, and every known workable solution with the measurement that establishes it, all filtered so held-out material never reaches the Maker. A trade between dimensions is the Owner's call, never the loop's.

10. <a id="D4.10"></a>**Bound the loop, and name every exit.** A cap, a budget and a time limit are supplied, never defaulted,
    and bind while the run proceeds. Every path ends in a named state.

11. <a id="D4.11"></a>**Escalate without interrogation.** What can be found out, the agents find out. Values, priority, risk
    and the Buyer's intent go to the Owner, with what was tried, why no observable answer exists, and the
    options with a recommendation. A bare question is work pushed back, not an escalation. **The Owner's
    attention is a budget, and it is measured.** There are three signals, each with a target of zero. The
    same kind of approval asked again and again. Choices put without a recommendation. Answers the Owner has
    to ask to have re-explained. A system that leaves its Owner feeling worked by the machine has failed, however good
    its output.

12. <a id="D4.12"></a>**Evidence or it did not happen.** Every claim cites a file, kept by its content hash. Notes are written
    from what the instruments produced, never from what someone intended. Keep the instrument that
    accepted the work, and the record, with the work: committed beside it, not in local scratch. Pin every
    standard by hash or commit, never by a version name alone; a version number cannot be checked. Figures,
    hashes and record fields are printed by the tool that produced them, never retyped by hand.

13. <a id="D4.13"></a>**Proportion.** The instrument is as heavy as the risk and no heavier. A smaller instrument is a recorded
    choice. It is never partial: it may not skip a must-ask value, a terminal state or a checked line.

14. <a id="D4.14"></a>**The level of delegation changes who decides, never what must be supplied.** Declare the rung (do
    exactly this; research and report; research and recommend; decide and inform; act). No rung waives a
    must-ask.

---

## 5. The loop

**Four moves, each one an answer for the person who signs:**

| Move | What it lets the signer say |
|---|---|
| <a id="D5.move.1"></a>**Set the bar** | I decided what "good" and "done" would mean before I saw the result. |
| <a id="D5.move.2"></a>**Produce against it** | The method is written down, so it can happen again, in someone else's hands. |
| <a id="D5.move.3"></a>**Evaluate independently** | Somebody who did not make the output checked it. |
| <a id="D5.move.4"></a>**Keep the record** | My name is attached, and so is everything it rests on. |

<a id="D5.core-sequence"></a>Behind them sits the core sequence: define quality and done, have the Evaluator in place before the Maker produces, then run the loop. Every loop that works runs in that order. You cannot evaluate what you have not defined. And a
definition written after seeing a draft is anchored on the draft.

### Two entries

<a id="D5.entry.A"></a>**Commissioned work (Entry A)** does not exist yet. The standard is written first, so it cannot have been
tuned to the artifact. Before generating, the Maker states the win and the done rule back in its own
words: the cheapest defect filter there is.

<a id="D5.entry.B"></a>**Existing work (Entry B, retrofit)** is already made, perhaps already in use. You cannot be blind to an
answer that exists, so declaration order substitutes for blindness. First collect the work's own standard:
its docs, tests and claims. Then declare the frame you would hold it to now, and freeze the instrument.
Only then read anything that could reveal a defect. The record says which reads came before the freeze.
The past gets a census, not a verdict, and thresholds apply forward. The richest finding is usually the
work contradicting itself: claims made but not implemented, and behaviour implemented but not claimed.

### One turn of the loop

1. <a id="D5.step.1"></a>**Freeze.** The bar, the instruments and the bounds are fixed and hashed. The work starts after.
2. <a id="D5.step.2"></a>**Make.** The Maker produces a version.
3. <a id="D5.step.3"></a>**Observe.** Independent channels produce observations the Maker did not touch.
4. <a id="D5.step.4"></a>**Judge.** Evaluator(s) score or read each dimension, each score with its quoted observation, alongside
   their controls. The verdict is a structure, not prose: dimensions, violations (each classified, each
   quoting its evidence), and a recommendation of accept, regenerate, needs owner, or reject.
5. <a id="D5.step.5"></a>**Decide the step.** Pass the rule: stop. Fall short: the next round receives four things—(1) the best artifact produced so far, (2) every known defect with its measurement, (3) every known workable solution with the measurement that establishes it, and (4) the held-out exclusion applied across all of that input so held-out material never reaches the Maker.
6. <a id="D5.step.6"></a>**Revise and repeat**, within the bounds, answering only what the Evaluator reported.

### The exits

A job ends in one of three states: **accepted**, **needs owner**, or **rejected**.

- <a id="D5.exit.accepted"></a>**Accepted:** the work passed the rule fixed before it began.
- <a id="D5.exit.needs-owner"></a>**Needs owner:** the cap was reached without a pass while the work stayed above the reject floor, or an escalation fired, or the instrument failed. Below the cap, such work goes back to the Maker. The **best version** the job produced goes to the Owner, never to the bin.
- <a id="D5.exit.rejected"></a>**Rejected:** below the reject floor. Work not yet in use is discarded. Work already in use is never
  discarded by the loop; the verdict stands and what to do is the Owner's call.

Beside the state, the record carries the outcome that explains it. For example:

- <a id="D5.outcome.census"></a>*census*: readings only, because no Specialist was named when the job began, so there is no bar to score against; every readable dimension must conform, or the job goes to the Owner;
- <a id="D5.outcome.no-observation"></a>*no observation*: the instrument failed. That is a finding about the instrument, never a zero for the
  work;
- <a id="D5.outcome.no-artifact"></a>*no artifact*: the Maker produced nothing.

There is no state in which a loop quietly ends.

<a id="D5.disposition"></a>**Verdict and disposition are separate acts.** The Owner may ship a rejected piece or shelve an accepted
one. The verdict stays as the loop produced it; the decision is written beside it.

### Where the human sits

<a id="D5.human"></a>Per-act approval is not required by default: ratifying the frame, the budget and the bounds at kickoff is enough for the Orchestrator to dispatch within them unless the job declares that specific acts need a separate human yes. When a job does declare per-act approval, it also declares which form counts: a standing grant recorded in the Owner's or Orchestrator's channel, a direct yes in the acting seat's own channel, or a relayed yes where the job's declared form permits relay and the record labels it as relayed. Any form the job did not declare authorizes nothing, and repeated requests for the same kind of approval remain a failure signal (§4 rule 11, §8 F5). On well-trodden ground, where an Evaluator has a validation record and calibrated thresholds, the loop
runs within its kickoff bounds without per-turn intervention and exceptions surface as *needs owner*. On novel ground (a new domain, new stakes, a
first run), a job may declare closer oversight until the proxy earns trust. The mistake is not keeping a human too
long; it is removing one before the proxy has proved itself. This is human-at-the-helm, not just human-in-the-loop: the person sets the bar before the work begins, keeps the decisions only they can make, and decides when the loop has earned the right to run without them.

---

## 6. Qualifying the seats

Seat no one on reputation, including the Architect.

- <a id="D6.1"></a>**Test every seat on planted cases before it serves.** A Maker shows it can generate and, separately,
  revise; an Evaluator shows it can fail what it judges; an Orchestrator shows it stops when the runbook
  says stop.
- <a id="D6.2"></a>**Check every instrument against a valid alternative.** Before an instrument scores anything, run it on a
  correct solution built differently from the one its author had in mind. An instrument that fails a valid
  alternative is measuring the author's design, not the bar.
- <a id="D6.3"></a>**Have someone independent pre-read the instruments.** The Architect writes the runbook and the scorer;
  an adjudicator reads both against the bar before any work starts. Where the instrument and the bar
  differ, the bar governs.
- <a id="D6.4"></a>**Pin instruments before use**, and keep them by hash. A rerun with the same rubric and a different
  runner is a different instrument.

[Building the custody record](https://github.com/evaluatordriven/custody/tree/main/record) showed why. In v0.9.5, two of the Architect's scoring tools scored a preferred design rather than the rules. In v0.9.6 it happened again: the Orchestrator found a tool that would have failed a valid design the brief allowed, and the work was scored again with a corrected tool, both scorings kept. The rules on valid alternatives and independent pre-reads exist to catch that before anything is scored.

---

## 7. The record

<a id="D7.record"></a>The record is what lets a person sign with integrity and confidence: it shows what the work was measured against, who checked it
independently, and who accepted it. A loop that leaves no record cannot be trusted by anyone who was not in the room when it was made. The record is how the doctrine reaches someone who wasn’t there to witness the work. It shows what the bar was and who held which seat. It
shows what each Evaluator saw, how they disagreed, what the Maker changed, and how the job ended. Accepted work that cannot be reconstructed from
its records counts as a failure of the doctrine (§8, F6).

<a id="D7.custody"></a>The interoperable form of that record is the **Evaluator Driven custody record**, `custody/v1`: a
hash-chained log and an in-toto predicate, with conformance levels a checker can verify. It is a separate,
neutral specification with its own repository. The record states facts; this doctrine says
which facts matter and why. **The doctrine never redefines the record's terms**, and the record never
depends on the doctrine. A job run under another method can still produce a valid record. The record will
show how far that job met the practices above.

---

## 8. How you would know it failed

The doctrine names its own failure signals, so it can be judged by them.

- <a id="D8.F1"></a>**F1.** Work ships with no Buyer in the record who asked for it.
- <a id="D8.F2"></a>**F2.** Judging costs more than the errors it catches (on a fair comparison).
- <a id="D8.F3"></a>**F3.** Work scored above the bar is later rejected by the named Buyer or Specialist, and the record
  cannot say which dimension failed.
- <a id="D8.F4"></a>**F4.** Two honest runs of the same setup disagree by more than the instrument's normal variation.
- <a id="D8.F5"></a>**F5.** The Owner is asked questions the system could have answered itself. Or the Owner is forced to carry an attention cost the system could have spared: repeated approvals of the same kind, choices without a
  recommendation, answers that need re-explaining.
- <a id="D8.F6"></a>**F6.** Accepted work cannot be reconstructed from its records.

**What is claimed is repeatability, not scale.** The bar, the instruments and the record exist so a result
can be reproduced by someone else. Nothing yet supports a claim that the method scales, so none is made. Repeatability is designed in, not yet shown: no result here is known to have been reproduced by someone else.

**The evidence for the big bet, so far.**

| Case | Maker | What was compared | Result |
|---|---|---|---|
| A translation system for low-resource languages | Code: a 9B model, hosted locally, writing to tests written first by a cloud-hosted model. Translation: a 1.3B model, hosted locally | The build: the loop only. The judging: an audit against planted defects, run independently of the judges under test | 900 of 911 tests pass offline with a dummy key set; 10 of the 11 failures are a real broken integrity gate. Spanish content made in one pass, outside the loop, carried real grammar errors in 3 of 100 units, which its review missed. The production judge, tested on planted defects, accepted 9 of 9 in its production mode; a simple structure check caught 6 of the 9, and one escaped every automated check. On 2026-09-06, two Lingala speakers read the Lingala output and accepted it: a first-language speaker reviewed 10 days of devotional content, and a second-language speaker read 5 (a retrospective report: which days, and how they read, are not recorded). One project, not a paired comparison |
| Seven real software defects in two web applications | One locally hosted 35B-class model, the same on both arms | One pass on all seven; the loop only on the 3 the pass missed. An executable probe as the pass rule (in one row a failing held test also counted as a miss), and a second Evaluator from another family agreeing on all seven | One pass fixed 4. Of the 3 it missed, the loop fixed 2 and missed 1. The Owner named this *a* comparator for software defect resolution, not *the* comparator |
| One live defect in a sign-in code endpoint | A 4B model, hosted locally | One pass versus the loop, with a second Evaluator agreeing | One pass missed; the loop was accepted on its fourth generation. Earlier loops on this defect, at temperature 0, did not reach acceptance and are not counted. Loop judging cost under half a cent, or $0.0139 with the second Evaluator's check. A hosted model fixed the same defect in one pass for $0.0140, with no second check: which is cheaper depends on what is counted. The Owner reports the defect cost about $20 in production; whether judging pays for itself (F2) is still open |
| A mobile devotional app (Android) | A 9B model, hosted locally, writing code to failing tests written first by the Evaluator; a cloud-hosted model from another family reviewed the diffs | The loop only; no run without it | A signed Android release build, with the unit, contract and browser suites recorded green (2026-08-29). The outside review caught 4 serious defects the tests had missed, and each was fixed through the loop. Files were later changed outside the loop, with no gate, and the archived source now fails its own tests: the loop protects only what passes through it. No device test was run, iOS was never built, and the release APK probably lacks its privacy policy. One project, not a paired comparison |

**Three conditions on the bet. The first two were learned the hard way in the translation work, the third in the mobile app.**

1. **The feedback must be able to change the work.** The first translation loop (2026-09-03) gave its
   translation model feedback that model could not act on. Of 25 jobs, 1 was accepted. Seven Lingala jobs never produced a score; the rest wandered, mostly between 1 and 4, without converging. Nine of 12 Swahili jobs scored exactly 7.8 on both iterations, with the same one-line feedback: consistent with a dormant influence channel. The next day a step was added that rewrote the source in
   response to the Evaluator's complaints. A different 20-row batch then passed 17 of 20 at a threshold of 7.5, under the same loop's own judge. The main change was a way to act on the judgement. That judge was later found to pass planted defects (condition 2), so the rise shows the loop could act on its judge, not how far quality rose.
2. **The judge must be qualified.** The later audit shows the second: a loop with an untested Evaluator
   passes defects with confidence. Well-judged is something you measure with planted cases (§6), not something you assume.
3. **The work must stay inside the loop.** Changes made outside it are neither judged nor recorded. In the
   mobile app, files were later changed with no gate, and the archived source now fails its own tests.

Only the [software-defect pair](evidence/software-defect-pairs.md) and the [Lingala reading](evidence/lingala-reading-2026-09-06.md) are published. The other translation and mobile-app records are the Owner's and not yet published; read those rows as his report.

The bet is on a loop that meets all three.

**What would settle it:** paired jobs in more than one domain. Each pair keeps the same Buyer, the same
standard and the same class of work, and runs once with the loop and once without. Each is published with
its record, and the results are reported as a rate that counts the misses as well as the wins, with outcomes beyond the pass: use, early detection and cost. Until then the bet is supported in software, shown working but not compared in translation, and not yet established across domains. This document says so rather than borrowing
authority it has not earned.

---

## 9. What this doctrine is not

- **Not a method for making things.** Make whatever products you like with whatever tools you like: by specification, by proof, by hand, by agent. Evaluator Driven governs how the work is judged, fed back and carried, and so it shapes the loop the Maker works in.
- **Not a source of values.** It does not set values, priorities, risk appetite or taste; the Owner does,
  and the doctrine then scores against that standard.
- **Not a replacement for the Owner's override**, which is recorded beside the verdict, never over it.
- **Not a product.** It is a set of rules you adopt, not a product you buy.
- **Not certification.** A record shows how a judgement was made, not that the work is correct.
- **Not finished.** It is versioned, and it changes when a job shows that it must, not before. No rule
  without a job that needed it.

---

## 10. Lineage

**Origin.** The doctrine was first written down on 2026-08-31 as "Evaluator Driven Iteration": define
quality first, build the evaluator before the generator, close the loop. It grew into seven weight-bearing
documents: a quickstart, a playbook, an operating instrument, machine contracts, a mandate, a worked example
and a guide for machines. The Owner ratified each document and its later amendments. They are published in
`contracts/`, below this doctrine in the chain of command (`AUTHORITY.json`).

**This articulation.** The doctrine restates the contracts for readers who will never open them. Version 0.1 added the
lessons of the custody-record releases v0.9.4 to v0.9.6. Its rules: test Evaluators with planted cases in every batch; never average disagreements; check instruments against valid alternatives and pre-read them before use; keep evidence by hash, and write notes from output, not intent. Those
releases were themselves run under this doctrine, and their records are public: https://github.com/evaluatordriven/custody, tags v0.9.4 to v0.9.6. One rule departed from the
corpus on purpose. The corpus barred the Maker's family from the Evaluator seat outright. Version 0.1 adopted the custody record's principle: the seat must not be biased toward the Maker's family (§3). Since v0.2 the contracts follow it. The record's rule, CL2-3, also requires a different endpoint.

**What it stands on.** Covey's stewardship delegation (desired results, guidelines, resources,
accountability, consequences). Hyatt's five levels of delegation. The writer–reviewer split in agent
workflows. The finding that models correcting themselves with only internal reasoning improve little or
get worse, while structured external feedback helps (Gou et al., *CRITIC*, 2023). The constitutional
form: a written, versioned standard, critiques that cite the clause they enforce, and revisions that
answer the citation. Evaluation-driven development: a scorecard before optimization, dimensions rather
than a pooled average. Teach-back from clinical practice: the person repeats the instruction in their own
words, because "do you understand?" reliably gets a yes.

**Applied to itself.** This document had to pass the gate it describes. The Architect drafted v0.1 for the Owner's edit; a reader from another model family checked it for claims its evidence does not support; the Owner ratified it on 2026-10-25. The Architect drafted v0.2; this repository's checkers verified that every rule is cited below it and that its text is v0.1 word for word apart from the recorded changes; the Owner ratified it on 2026-11-02. A citation is not agreement: v0.2 kept rules the contracts had already replaced, on the Orchestrator's seat and on what the next round is given. Version 0.2.1 takes the contracts' rules in the custody maintainers' wording, and its checkers now compare the wording of those rules, not only the citation. Neither version has had a reader from another model family.

---

*Evaluator Driven, v0.2.1. © 2026 Steve Moitozo II. Licensed under CC BY 4.0.
evaluatordriven.com*
