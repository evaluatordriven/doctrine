# Evaluator Driven — the doctrine

**E-DI: Evaluator-Driven Iteration. A doctrine for delegating work so that quality survives.**

Can I trust our name to this work? Evaluator Driven exists so the honest and confident answer can be yes.
Work is judged against a bar set before the work began, by a tested Evaluator who did not make it, and the
record lets anyone who needs to audit the work check it.

## What is here

| Path | What it is | For |
|---|---|---|
| [`DOCTRINE.md`](DOCTRINE.md) | The doctrine, version 0.2.1: why, and the rules in plain words; each rule has a stable id (`D4.3`) | People |
| [`contracts/`](contracts/) | The machine contracts: the load set, schemas, fixtures, rule index and checkers an implementation is tested against | Implementations and their testers |
| [`evidence/software-defect-pairs.md`](evidence/software-defect-pairs.md) | The same model, with and without the loop, on real software defects (cited in §8) | Anyone weighing the claims |
| [`evidence/lingala-reading-2026-09-06.md`](evidence/lingala-reading-2026-09-06.md) | Two Lingala speakers' reading of a loop-built translation (cited in §8) | Anyone weighing the claims |
| [`CHANGELOG.md`](CHANGELOG.md) | What changed in this repository | Everyone |
| [`LICENSE`](LICENSE) | Creative Commons Attribution 4.0 International (text) | Everyone |
| [`LICENSE-CODE`](LICENSE-CODE) | Apache License 2.0 (code: `contracts/tools/`, `contracts/schemas/`, `contracts/fixtures/`) | Implementations and their testers |
| [`NOTICE`](NOTICE) | Which licence covers which path, and the patent grant | Everyone |

## Chain of command

[`AUTHORITY.json`](AUTHORITY.json) is the chain of command for this repository. CI and implementing agents
read it. Lower tier, higher authority:

| Tier | Holder | Owns |
|---|---|---|
| 0 | The Owner | Ratifies everything; decides what no file settles |
| 1 | `DOCTRINE.md` | Everything; wins any conflict |
| 2 | `contracts/EDI-PLAYBOOK.md`, `contracts/EDI-MANDATE.md` | Purpose, values, seats, priority; the frame and failure signals |
| 3 | `contracts/EDI-MACHINE-CONTRACTS.md` | Binding behaviour, states, schemas, the pass rule |
| 4 | `contracts/EDI-OPERATING-INSTRUMENT.md` | The job form |
| 5 | `contracts/schemas/` and its fixtures | Field names; expected verdicts |
| 6 | `contracts/EDI-FOR-MACHINES.md`, `EDI-QUICKSTART.md`, `EDI-EXAMPLE.md` | Reading order and bans; teaching |

A higher tier wins, and the lower file is the defect. A disagreement on one tier is first tested against
every higher tier, nearest first; the first that answers it decides. If none does, it goes to the Owner.
custody/v1 governs the record's own terms, which the doctrine never redefines. Everything else here
(READMEs, CHANGELOG, `evidence/`, tools, indexes, manifests) has no authority.

**Citations point up.** Each rule in `DOCTRINE.md` has a stable id, such as `D4.3`. The doctrine cites
nothing below it. Instead, the Playbook, the Mandate, the Contracts and the Instrument each end with an
*Implements* table naming the doctrine rules their own ids carry. When a lower file renumbers, it updates
its own table in the same commit, and the doctrine does not change. CI fails if a doctrine rule is carried
nowhere, unless `AUTHORITY.json` declares it as a gap.

## Testing an implementation

An implementation such as Plumbline pins `contracts/` at a commit of this repository and checks the
sha256 of every file it depends on. Anyone can then re-run its corpus checks with nothing private:

```sh
git clone https://github.com/evaluatordriven/doctrine
export EDI_CORPUS=$PWD/doctrine/contracts
```

To check this repository, with Python 3.10 or newer and the standard library only:

```sh
cd doctrine
python3 tools/check_authority.py          # the chain of command holds: every file classified, headers, reading order
python3 tools/check_downhill.py --strict  # every lower tier agrees with the tiers above it; every doctrine rule is carried
python3 tools/check_authority.py --selftest && python3 tools/check_downhill.py --selftest   # each must be seen failing
(cd contracts && python3 tools/check_consistency.py && python3 tools/build_manifest.py --verify)
```

## Status

Doctrine version 0.2.1, ratified by its Owner on 2026-11-02 (v0.2 ratified 2026-11-02; v0.1 ratified 2026-10-25). Contracts v1.27.0 and Operating Instrument
v1.13, published 2026-11-02. The evidence so far is narrow, and §8 says so: what would show the doctrine
has failed, what supports it, and what would settle it. No outside adopter is known.

Facts that change as the work moves live here, not in `DOCTRINE.md`. As of 2026-11-02:

- **The smallest crew.** One person can run a job: they hold the Owner, Architect, Buyer and Specialist
  seats, disclosed, while a model makes the work and a model of another family, or a script that person did
  not write, judges it. The one seat they may not take is the Evaluator's, since whoever disposes of the work
  does not judge it (DOCTRINE §3).
- **Qualifying the seats (DOCTRINE §6).** The Architect's seat is not yet tested on planted cases; that gap
  is open.

## The custody record

The doctrine says which facts about a piece of work matter and why. The record that carries those facts
is a separate, neutral specification: the Evaluator Driven custody record, `custody/v1`, in its own
repository at <https://github.com/evaluatordriven/custody>. The doctrine and its contracts never redefine
the record's terms; where they name the same term, custody/v1 governs. The record does not depend on the
doctrine.

**Status (2026-11-10).** custody/v1 is a candidate (v0.9.8). Its stranger test has not yet passed (v0.9.4 to
v0.9.7). Known implementations: [Plumbline](https://github.com/evaluatordriven/plumbline) emits custody/v1
records for its own jobs; two are published, and both verify at CL1.

## Licence

**Text and evidence:** [CC BY 4.0](LICENSE). © 2026 Steve Moitozo II. More at <https://evaluatordriven.com>.
**Code** — `contracts/tools/`, `contracts/schemas/`, `contracts/fixtures/`: [Apache License 2.0](LICENSE-CODE).
Apache-2.0 §3 carries an express patent grant for that code; CC BY 4.0 grants none for the text.
Which path takes which licence is stated once, in [`NOTICE`](NOTICE).

The split is deliberate. An implementation copies a checker into its own tree and needs a software
licence, not a prose one; a reader quotes the doctrine and needs neither the Apache obligations nor the
implication that a document is code.
