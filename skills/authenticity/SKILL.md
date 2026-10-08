---
name: authenticity
description: Stage 2 of the app pipeline. Reads the approved business documentation, runs the OP Authenticity process (op-authenticity) to define who the product is for, where it lives, what it stands for and how it must feel, scores it against the pass rules, and loops until it passes. Use after the business documents are approved, or when someone runs /authenticity.
---

# Stage 2: Authenticity

Make sure the product is defined by its real people, place, purpose and presence before anyone designs it. No profile, no pixels. Follow the shared rules in the `pipeline-core` skill.

Requires `business` to be `approved`. Reads everything in `docs/01-business/`. The process itself is the `op-authenticity` skill (the OP Authenticity Compass: 4 lenses, 16 dimensions): load it and follow its steps 0 to 8. This file says how it fits the pipeline.

## How it fits

- **Inputs are the business documents.** Step 0 of the skill asks for business files: use `docs/01-business/` (Shared D1, the feature D1s and D3s, and the registries) and `docs/01-interview-notes.md`. Cite document, section or ID for every Found dimension, using the business IDs.
- **Outputs go in `docs/02-authenticity/`** instead of the skill's `00-authenticity/`: `AUTHENTICITY.md`, `coverage-map.md`, `authenticity-card.html`, `scorecard.md`, `generic-diff.md`, `design-brief.md`, `open-questions.md`, `profile.json`. Run the skill's scripts with those paths.
- **One question at a time**, a recommendation with each, plain words. The skill already says this.
- **A gap in the business documents is a business change.** If an answer shows a business document is wrong or thin, record it as a change request, make the change in `docs/01-business/` through the business stage's rules, and tell the founder that `business` needs re-approval.

- **Stage names in the skill's guard checklist** map to this pipeline: Discover / research and Requirements are the business stage, Set up is setup, and Build is frontend and backend.

## The loop

The stage repeats until the profile passes. Do not skip or loosen a rule.

1. Capture, match, fill the gaps, ground, define, challenge (skill steps 1 to 6).
2. Score and run the gate (step 7): `python skills/op-authenticity/scripts/check_gate.py docs/02-authenticity/profile.json`.
3. **Not yet** (a rule in 1 to 4 fails): tell the founder in plain words which dimensions are weak and the fastest way to lift each, ask the questions, update the profile, and go back to 1. Record each pass in the state file's history with the score.
4. **Ready for sign-off** (rules 1 to 4 pass): go to the approval gate.

## Approval gate

The skill's rule 5 asks for two signatures: the OP Authenticity Lead and the founder. You never sign for anyone.

- Set `authenticity` to `awaiting_approval` and run the gate from `pipeline-core`, with the skill's approval summary as the 10-line summary.
- Ask the founder for their approval and, if the project has an Authenticity Lead, whether that person has approved. Record both names and the date in `profile.json` and `scorecard.md` only when the founder tells you so. If the project has no Authenticity Lead, ask the founder to say so explicitly and record that, instead of leaving the signature blank.
- Once approved, offer to start stage 3 (design).

## Guard mode in every later stage

From here on, the approved `AUTHENTICITY.md` and `design-brief.md` are part of the brief for every stage. Each later stage skill names the one question from `skills/op-authenticity/references/guard.md` that it must answer (Design: could this screen belong to any other product? Frontend: does every page pass on language, direction, formats, tone? and so on). Answer **Pass**, **Drift** or **Profile change needed** before asking for approval. A profile change needs the same approvals again and sends the later stages to `needs_reapproval`.
