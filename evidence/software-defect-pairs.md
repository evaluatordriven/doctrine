# Evidence: the same model, with and without the loop, on real software defects

Part of the evidence for *Evaluator Driven*, §8 ("The evidence for the big bet, so far"). Version 0.1, 2026-10-24.
Licence: CC BY 4.0, granted by the Owner as publisher. *(Placement, version, date and licence are
publication details, not findings of the records.)*

## What this is

*Editorial note:* *Evaluator Driven* bets that the same job, run inside a well-judged loop, beats the same
job run without one. What follows is evidence, not editorial.

This file reports one narrow test: **fixing real defects in two web applications**, "A" and "B". The Owner
states that he owns both, and that both run in production. For each defect, the records give the outcome of
a single attempt by the model (the one-shot) and, where the one-shot missed, the outcome of the loop, run
with **the same model**. In the loop, an evaluator independent of the model judged each generation against
the defect's standard, and the model regenerated, within a cap. The separate pair's record (§3) documents
the one-shot running first and the loop after it; the rate's record gives the outcomes, not the order of
execution.

It reports every defect screened, the misses as well as the wins, and one result that cuts against a loose
reading of the bet (§4).

## 1. What the records establish about the method

| Item | Record |
|---|---|
| Maker, every row | `qwen3.6:35b-a3b-q4_K_M`, hosted locally (Qwen family) |
| Loop evaluator | DeepSeek's `deepseek-flash`, via DeepSeek's own endpoint. Not the Maker |
| Second evaluator, every row | `grok-4.3` via xAI. Not Qwen. Not shown the first verdict |
| Pass rule | An independent executable probe. Row 1 counts as a miss although its probe was clean: its held test still failed |
| Disagreement rule | A disagreement between the evaluators would have blocked the row. None did (7 agree, 0 disagree) |
| Bounds | Budget cap $3. Row 1 records a cap of 6 generations |
| Protocol | Written, and held by SHA-256 `e9f010291423d94f48c1680d2650f537c3d0470146d599392663a004e7138c34`. The rate's record reports 19 of 19 protocol gates passed when it was written. The protocol text is not published with this file |

## 2. The result

**Planned size 8, screened 7.** One queued defect depended on the hosting platform's runtime and could not
be reproduced locally. It was excluded, not simulated.

| Outcome | Rows |
|---|---|
| One-shot passed; the loop was not run | **4** |
| One-shot missed; **the loop passed** | **2** |
| One-shot missed; the loop missed | **1** |
| Second evaluator agreed / disagreed | **7 / 0** |

**The rows,** by defect class only:

| Row | App | Defect class | One-shot | Loop |
|---|---|---|---|---|
| 1 | A | Verification flow: wrong behaviour on repeated failed attempts | Missed. It also recorded a `canvas_moved` failure | **Missed.** The probe was clean by generation 4, but the held test still failed with a syntax error |
| 2 | B | Payment webhook: the signature check was referenced but never defined | Missed (crashed) | **Passed**, generation 2 |
| 3 | B | Checkout: wrong authentication scheme | Passed | Not run |
| 4 | B | Cancellation: subscription tier handled wrongly for a scheduled cancellation | Passed | Not run |
| 5 | A | Notification endpoint: sent mail without authentication | Passed | Not run |
| 6 | A | Invitation endpoint: no per-IP rate limit | Passed | Not run |
| 7 | A | Sign-in code endpoint: no rate limit (limits set by the Owner) | Missed: removed lines and added no limit | **Passed**, generation 4 |

**The model's own tests were unreliable.** The probe decided every row, which mattered:

- **Rows 3 and 7:** the test runner exited 0 while its own output reported a failing test.
- **Row 2:** the generated test never called the handler, so its clean exit tested nothing.
- **Row 4:** the generated test did not parse.
- **Row 5:** the runner wrote the test under the wrong file name. An extra authenticated case, which the
  standard did not require, failed.

A process exit of 0 is not a pass.

**Cost.**
- Known loop-evaluator spend for the rate is **$0.004104**: $0.001426 for row 2 and $0.002678 for row 7.
- Row 1's 6 evaluator calls were not costed: the provider's response carries no cost field. The recorded
  $0.00 means *unknown*, not *free*.
- On the four one-shot passes, loop judging was not run. The second evaluator did run on every row, and
  the rate's record does not report its cost.

**Exclusions** (beside the rate, not in it):
- the unreproducible runtime defect;
- two bundled side measurements: a two-file one-shot that passed both probes, and a three-file one-shot
  that failed to apply because an anchor matched twice (a delivery fault, not a behaviour miss);
- a run that died on a provider payment error.

## 3. A second pair: a very small model, and a defect with a price

A separate pair, recorded the next day, is kept outside the rate. It differs from the rate in its model,
its sampling and its pass rule:

- **Maker:** Qwen3.8 4B, hosted locally, sampling at temperature 0.6. **Evaluator:** DeepSeek's
  `deepseek-flash`. **Second evaluator:** `grok-4.3`, shown neither the probe nor the first verdict.
- **Pass rule:** the evaluator against the standard, not the probe. The Owner ruled this because the probe
  required a storage key that the standard forbade.
- **Comparability:** the pair's instrument hashes post-date earlier 4B loops on this defect, which are not
  mixed in. Those earlier loops, at temperature 0, did not reach acceptance.
- **Defect:** application B's sign-in code endpoint had no limit: the record says it mailed on every
  valid-email request. *The Owner reports* that "valid" there means the address passed the format check,
  not that it was real, and that in production an attacker used the flaw to send thousands of unsolicited
  emails, many to made-up addresses, each counted against the mail quota. The resulting charge was about
  **$20**, as reported by the Owner. Users were locked out of their sign-in codes.
- **One-shot:** missed. The evaluator's verdict was *regenerate*; the second evaluator listed every
  requirement as unmet. An earlier identical draw broke its output format, produced no file and was never
  judged. It is a delivery fault, not the miss.
- **Loop:** accepted on generation 4 (mean 10.0, floor 10.0). The second evaluator agreed.
- **Cost, all recorded evaluation:**

  | Item | Cost |
  |---|---|
  | One-shot judging | $0.000923 |
  | Loop judging | $0.003603 |
  | Second evaluator: one-shot $0.010357, loop $0.010257 | $0.020614 |
  | **All recorded evaluation for the pair** | **$0.025140** |

  The Owner books the local model's power at **$0.0022** per job, which puts the loop's judging plus power
  at **$0.005803**.

## 4. The result that cuts against a loose reading

The same defect was given to two hosted models in one pass, with the same prompt and standard:

- **`grok-4.3`:** neither of two draws produced a usable file (broken output format). These are delivery
  faults, not behaviour misses. The two draws cost $0.012527 and $0.004854 ($0.017381), recorded beside the
  comparison and in neither total below.
- **`grok-4.5`:** fixed it in one pass, accepted by the same evaluator. Model $0.013146 plus judging
  $0.000878: **$0.014024**.

What that comparison shows depends on what is counted:

| What is counted | 4B loop | grok-4.5 one-shot |
|---|---|---|
| Judging plus the local model's power | $0.005803 | $0.014024 (about 2.4× the loop) |
| Adding the loop's second-evaluator check | $0.016060 | no second check recorded |

So the evidence does **not** say a small model in a loop beats a large model. On this defect the
hosted model fixed it without a loop. What the records show is narrower: **of the three defects the rate's
model missed in one shot, the loop rescued two and missed one, and in the separate pair the loop rescued
the 4B model's miss.**

## 5. What the Owner ruled (2026-09-28, verbatim)

> "I'm comfortable naming this as A comparator for software defect resolution. I also agree, this is not
> the resolution of F2 so the hold remains."

The ruling's scope, as recorded:
- It names the **seven-row rate, with its model**, as *a* comparator for software defect resolution, not
  *the* comparator.
- It does **not** judge whether the judging was worth its cost.
- The record adds: "Fitness is not moved." The ruling does not change the corpus's own fitness reading.
- The doctrine's failure signal F2 (does judging cost more than the errors it catches?) stays open.

**Production.** The recorded runs pushed nothing to either application: an accepted experimental file is not
a deployment. *The Owner states* that every affected application has since been patched in production.

## 6. What this is not

- Not proof that the loop works in every domain. This is software defects only.
- Not proof that every small model improves inside a loop.
- Not a claim that the loop always rescues a miss: 1 of the rate's 3 misses stayed missed.
- Not a large sample: the rate has 7 rows with one model; the separate pair adds 1 defect with a second
  model.

## 7. Integrity

**Recorded standard hashes, by SHA-256.** The standards are not reproduced in this pack. The pair's standard
is recorded as frozen and hashed before its two arms; for the rate, the record gives the hashes and marks
several standards as not edited.

| Row | Standard (sha256) |
|---|---|
| 1 | `251170b4cb19ed5807a5a64ab25107071a935acddb9f111b30b8ae42a4feb8a7` |
| 2 | `7e9de3cd6c824c089ad8cf9895cceb97f71832302f70b7e7e1b6b38fc464f002` |
| 3 | `fb698d979336051963e1af1f9cca8d05f6dd57e75eaa5c909ef2fe78ab612c6d` |
| 4 | `581d681e39984d8b4b31b5cebd910d9571d9d8d8a1c6e262085a6ad9d57c1337` |
| 5 | `f2b90c54470f3e53afc52a200e8815474ac76e070a35428e48834bfbbf4c7f48` |
| 6 | `68029fdf3b3c0878a49d6afa0a1748fb6a494cdacab3e031685bcbba63a9e7c9` |
| 7 | `6bb4114775be794f610718d852fd5ba1e7e6aed4bc27abaf7f49199113add0c9` |
| §3 pair | `f4df78233373a5d494ea74030dca656a951855957751fd61ad399e48e222665d` |

**Artifacts, by SHA-256:**

| Artifact | sha256 |
|---|---|
| §3 pair: the loop's accepted file | `d7eed85afabc70d73e71fbc0f8a54c956033968bea046ae0ea4872bd4fa32252` |
| §4: `grok-4.5`'s accepted file | `88f1151abd9a12e532c2c98b8f3df6849e6f34a9da87621ef65178c8823ec30e` |

**Selection, as documented:**
- Row 1 had an earlier accepted run. It is not cited; the rate reports the later miss.
- The exclusions in §2 are listed with their reasons and kept outside the rate.
