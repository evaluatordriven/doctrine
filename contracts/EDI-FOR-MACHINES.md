# E-DI — For machines (and agents)

**Authority:** tier 6 in `../AUTHORITY.json` — outranked by tiers 0–5; conflicts follow its conflict rule.

**Weight-bearing.** Programs and agents implement from this page + the files it names.  
**Rule:** No logical leaps. No silent defaults for required fields. No “workaround” that skips a seat or exit.  
**Owner ratification:** **2026-09-24** — the Owner ratified this file as weight-bearing.

---

## Load set (only these)

Runtime adapters (for example a harness skill or plugin) belong to implementations, not to these contracts.

Load in this order:

**Canonical agent load order lives only here.** Quickstart, README, and any implementation's adapter must cite this section; they must not publish a different sequence.

**Bootstrap: read this file first — it owns the sequence. The numbered list is the reading order. It is not an authority order: authority is `../AUTHORITY.json`, tiers 0–6.**

**Conflicts.** A higher tier wins, and the lower file is the defect. On the same tier, first test the disagreement against every higher tier, nearest first, up to `../DOCTRINE.md`; the first that answers it decides. If none does, escalate to the Owner as `needs_owner`, with both passages, what you checked and a recommendation. Never edit a higher tier to match a lower one.

0. `../DOCTRINE.md` — the doctrine (tier 1); read it before acting on any conflict  
1. `EDI-PLAYBOOK.md` — purpose, seats, priority (align behavior to it)  
2. `EDI-QUICKSTART.md` — human context (optional for headless jobs; required if the agent explains E-DI to a user)  
3. `EDI-OPERATING-INSTRUMENT.md` — job form, Entry A/B, rules, exits  
4. `EDI-MACHINE-CONTRACTS.md` — NORMATIVE machine rules (short front). The v1.12 full text is held in the private working corpus and not published; not required to run a job or to verify an implementation. The short front wins.  
5. `EDI-MANDATE.md` — short frame limits (X/F/M). Deep annexes are held in the private working corpus and not published; not required to run a job or to verify an implementation  
6. `EDI-EXAMPLE.md` — record shape to copy  
7. This file — load order and bans  

**Do not load as authority:** anything outside this `contracts/` folder except `../DOCTRINE.md`, which outranks it; the doctrine's `evidence/` is evidence, not authority.

---

## Hard bans

1. Do not invent a terminal state. Only: `accepted` | `needs_owner` | `rejected`. `census`, `no_observation`, and `no_artifact` are outcomes, never `terminal_state`.  
2. Do not let the Maker grade its own final output.  
3. Do not start Entry A generation before Buyer/done-rule and Evaluator standard exist.  
4. Do not “fix” `EDI-PLAYBOOK.md` to match code or a skill. Escalate conflicts to the Owner.  
5. Do not treat examples in Contracts as requirements (NORMATIVE vs EXAMPLE).  
6. Do not skip a blank required sheet field by guessing.  
7. Do not rewrite a loop verdict when the Owner overrides — record a **disposition beside** the verdict.  
8. Do not use a second document pile to bypass the sheet.  
9. Do not start Entry A generation until the job packet **validates** (`tools/validate_job_packet.py`) **and**, on a scored job, the C33 frame is present (ground truth, mandate, escalation route). Validation is necessary, not sufficient: a scored packet that lacks that frame is not ready. A readings packet is not made to carry a scored frame. Failure → stop and ask.  
10. Choose `instrument_profile`: `full` or `mvi` before fill; record it on the packet (see Operating Instrument § Profiles).

**Not a ban.** On a scored job, after the Evaluator returns, shape is checked by `schemas/evaluator-record.schema.json` and `tools/validate_evaluator_record.py`. A pass of that checker is not C8. The Orchestrator stamps `instrument_in_force` after the Evaluator returns; the Evaluator does not emit the hashes. `defect: saw_gt` is a name, not a failed file — the checker exits 0 and the Orchestrator exits `needs_owner`. This checker is not an item in the load set.

**Not a ban.** Once an artifact exists, the Maker receives the best artifact the job has produced (Instrument rule 12 / I24), not the original. Before that call, `tools/check_best_artifact_handoff.py` exits 0. A pass is not C8. This checker is not in the load set.

---

## Required job record fields (minimum)

**Machine authority:** `schemas/job-packet.schema.json` — validate with `python3 tools/validate_job_packet.py <file>`.  
Prose floor (same ideas): copy structure from `EDI-EXAMPLE.md`. Every completed job record MUST include:

- `entry`: `A` | `B`  
- `instrument_profile`: `full` | `mvi`  
- `job_name`: string  
- `artifact`: path and/or version (commit/hash if code)  
- `buyer`: string  
- `maker`: string or object (engine + version if software)  
- `evaluator`: string or object (who/what + instrument id/hash if any; in object form, optional `kind`: `person` | `model` | `script`)  
- `standard_ref`: what was judged against (doc + version)  
- `bounds`: cap and/or budget as stated on the sheet (scored jobs)  
- `terminal_state`: `accepted` | `needs_owner` | `rejected`  
- `outcome`: required on a completed record. Enum and pairing: Contracts §2. Not optional.  
- `disposition` (optional): Owner decision if different from verdict  
- `notes`: shortfalls in plain language (no empty “looks good”)

The schema wins on **field names**. It wins on requiredness only where it is **stricter** than Contracts. It never licenses a Contracts must-ask to be absent. This list is the human-readable floor.

---

## Entry selection (no leap)

- Artifact **does not exist yet** → Entry **A**  
- Artifact **already exists** → Entry **B**  
- Do not choose by “intent” if the artifact is already on disk.
- Entry B is Contracts C32 plus Instrument Entry B. Do not accept an Entry B job that has no `reads_before_freeze`. Do not invent a retrofit procedure the sheet does not already contain.
- Maker "family" is not machine-checkable yet. Exact identity is. Owner must not hold the Evaluator seat (0028 A). The schema's `not` block catches the string and `name`/`who` object shapes only — `tools/validate_job_packet.py` is the full structural gate and covers the remaining object shapes. Trust the checker, not the schema alone.

---

## When blocked

| Situation | Action |
|-----------|--------|
| Missing Buyer or done-rule | Stop; ask; do not invent |
| Missing standard / Evaluator | Stop; build or request before scoring |
| Values / risk / voice undecided | Escalate to Owner (`needs_owner` path) |
| Playbook vs Contracts conflict on purpose/seats | Escalate to Owner; do not quiet-edit Playbook |
| Playbook vs Contracts conflict on states/schema | Obey Contracts for machine behavior; report conflict |
| Sheet allows a double-hat Contracts forbid | Stop. Do not copy a fixture across that conflict. Landed rule: Owner must not hold Evaluator (0028 A). |

---

## Success check (machine)

A run is well-formed only if:

1. Only the files on tiers 1–6 of `../AUTHORITY.json` were treated as authority, and  
2. The sheet’s required fields were filled or the run stopped with a clear ask, and  
3. The terminal state is one of the three allowed, and  
4. The job record can be read later without re-running the loop.
