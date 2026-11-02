# E-DI machine contracts

The rules an implementation of Evaluator Driven obeys, in a form a program can be checked against.
`../DOCTRINE.md` is the doctrine, and it wins any conflict with this folder.

If you build an E-DI loop, pin this folder by commit, and check every file you depend on by its sha256.
A version number cannot be checked. A commit can.

## The load set

An agent reads in the order **`EDI-FOR-MACHINES.md`** sets: `../DOCTRINE.md` first, then these seven files. That is a reading order; authority is `../AUTHORITY.json`.

| File | Role |
|---|---|
| `EDI-PLAYBOOK.md` | Purpose, values, seats, priority. Changes least. |
| `EDI-QUICKSTART.md` | Plain on-ramp. |
| `EDI-OPERATING-INSTRUMENT.md` | The handoff form: Entry A and B, rules 1–12, I1–I24. |
| `EDI-MACHINE-CONTRACTS.md` | NORMATIVE machine law: roles, states, schemas, pass rule, C-lines. |
| `EDI-MANDATE.md` | The Owner's frame: P, M, X and F lines. |
| `EDI-EXAMPLE.md` | One worked job. |
| `EDI-FOR-MACHINES.md` | Load order and hard bans. |

## The machine layer

| Path | What it is |
|---|---|
| `schemas/job-packet.schema.json` | The job packet. Draft 2020-12. |
| `schemas/evaluator-record.schema.json`, `schemas/pass.schema.json` | The scored evaluator record and each filed pass. |
| `schemas/fixtures/` | Passing and failing packets, records and passes, each with a named reason. |
| `schemas/templates/` | A mandate skeleton. |
| `EDI-RULE-INDEX.json` | Every NORMATIVE rule in the Contracts and its disposition: a C-line, a schema rule, or none. Generated. |
| `tools/validate_job_packet.py` | Validates a packet. Standard library; also runs Draft 2020-12 when `jsonschema` is installed. |
| `tools/validate_evaluator_record.py` | Validates a scored evaluator record and the passes it names. |
| `tools/check_role_separation.py`, `check_terminal_state.py`, `check_best_artifact_handoff.py` | Single-rule gates. |
| `tools/extract_rules.py`, `classify_rules.py` | Regenerate `EDI-RULE-INDEX.json` and §9's state block from the Contracts. |
| `tools/check_consistency.py`, `build_manifest.py` | This folder's own gate, and its `MANIFEST.sha256`. |

Passing a checker is not passing a job. A checker shows the shape is right, not that the work is good.

## Verify this folder

Python 3.10 or newer, standard library only:

```sh
cd contracts
python3 tools/check_consistency.py      # structure, references, regeneration byte-identical, manifest
python3 tools/build_manifest.py --verify
```

## What wins

`../AUTHORITY.json` is the chain of command, and every load-bearing file here names its tier in its header.
The Owner (0), `../DOCTRINE.md` (1), the Playbook and the Mandate (2), the Contracts (3), the Operating
Instrument (4), the schemas and fixtures (5), and For Machines, the Quickstart and the Example (6). A higher
tier wins. A same-tier disagreement is first tested against the tiers above, then goes to the Owner. The
terms of the retained record belong to custody/v1, <https://github.com/evaluatordriven/custody>.

## Where this came from

This folder is a public derivative of the Owner's private working corpus, at Contracts v1.24.0 and Operating
Instrument v1.10. The changes are recorded in each file's version line and in `../CHANGELOG.md`. Proposals,
evaluation records, the change history and teaching documents stay private. They are lineage, not law, and
nothing here depends on them.
