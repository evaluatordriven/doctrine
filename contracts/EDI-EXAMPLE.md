# E-DI — Worked example

**Authority:** tier 6 in `../AUTHORITY.json` — outranked by tiers 0–5; conflicts follow its conflict rule.

**Weight-bearing.** One job, plain English. Copy this shape; do not copy the product unless you are doing the same work.  
**Owner ratification:** **2026-09-24** — the Owner ratified this worked example as weight-bearing.

---

## The job in one sentence

Build a small **skill file** so an agent can use a vendor’s docs correctly — without inventing steps.

---

## Sheet (filled)

| Field | Value |
|-------|--------|
| **Entry** | A — commissioned (skill did not exist yet) |
| **Job** | One skill package: `SKILL.md` + one reference page |
| **Artifact under test** | `artifact/iter-2/SKILL.md` (+ `reference.md`) |
| **Maker** | `deepseek/deepseek-v4.1-flash` (writing seat) |
| **Buyer** | Owner — needs agents to follow vendor docs without guessing |
| **Specialist** | Vendor documentation (staged as ground truth) |
| **Ground truth** | Vendor docs snapshot, version pinned for the job |
| **Instrument** | Rubric + runner, frozen and hashed **before** judging |
| **Evaluator** | `z-ai/glm-5.3-flash`, 3 readings per iteration |
| **Bounds** | `T_accept` 8.5 · `T_dim` 7.0 · `T_reject` 6.0 · `cap` 3 iterations · `budget` $2 USD (unit stated) |
| **Human seat** | Owner on override; escalation model named but not used |
| **Level** | Decide within bounds; Owner hears terminal result |

*(Full field list lives on `EDI-OPERATING-INSTRUMENT.md`. This table is the example fill.)*

---

## What happened (short)

| Iteration | Result (plain) | Verdict |
|-----------|----------------|---------|
| 1 | Skill existed but was hard to use; below the accept bar, at or above the reject floor — the loop continues | `regenerate` |
| 2 | Same goals, clearer steps and checks; all dimensions at or above bar | `accept` → terminal `accepted` |

*`rejected` is terminal (below the reject floor; discard). A run that continues was never rejected — its verdict was `regenerate`.*

**Terminal state:** `accepted`  
**Why accepted:** Three Evaluator readings agreed the second artifact met the frozen standard.  
**Owner disposition:** none required (verdict stood). Installing the skill in a live agent profile was a **separate** Owner choice after acceptance.

---

## Job record (minimum copy-paste shape; treat these values as examples)

Machine shape: `schemas/fixtures/example-job-packet.json`. If this page and that file disagree, the fixture wins. Do not repair a failing copy by hand.

---

## What a Delegator should notice

- Done was defined **before** the Maker wrote.  
- Evaluator ≠ Maker.  
- Feedback changed the **next** version.  
- The loop **stopped** with a named exit.  
- “Accepted” meant “met the standard,” not “already installed everywhere.”
- Verdict words (`accept` / `regenerate` / `needs_owner` / `reject`) are the **Evaluator's**; terminal words (`accepted` / `needs_owner` / `rejected`) are the **job's**. The pairing is Contracts §2.

---

## Source

Condensed from a real Entry A job filed under the operating instrument (JEV skill, 2026-09-22). Details stripped so the **pattern** is obvious. Authority for how to run jobs remains the Instrument + Playbook, not this story.
