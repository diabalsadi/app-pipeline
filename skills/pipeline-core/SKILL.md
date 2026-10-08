---
name: pipeline-core
description: Shared rules for the app pipeline that every stage follows - stage order, the project state file, approval gates, and how to talk to a non-technical founder. Load before running any pipeline stage (discover, validate, design, architect, setup, build, qa) or when asked where an app project stands.
---

# App pipeline: shared rules

The app pipeline takes a non-technical founder from an idea to a tested web or mobile app. Every stage skill (`discover`, `validate`, `design`, `architect`, and later `setup`, `build`, `qa`) follows the rules in this file.

## Stage order

| # | Stage | Skill | Main output | Needs approved |
| --- | --- | --- | --- | --- |
| 1 | Discover | `discover` | `docs/01-business-plan.md` | nothing |
| 2 | Validate | `validate` | `docs/02-requirements.md` | Discover |
| 3 | Design | `design` | `docs/03-design/` | Validate |
| 4 | Architect | `architect` | `docs/04-architecture.md`, `docs/04-cost-estimate.md` | Design |
| 5 | Set up | `setup` | the app's GitHub repo | Architect |
| 6 | Build | `build` | screens merged one at a time | Set up |
| 7 | QA | `qa` | a clean full test run | Build |

The pipeline ends when QA passes. It never deploys the app to production.

Before starting a stage, read the project state (below). If the stage it needs is not `approved`, tell the founder which stage comes first and offer to start that one instead. Never skip a stage.

## Where files live

Detect which environment you are in and use the matching storage:

- **Claude Code (or any session with a working folder):** one folder per app project. Outputs go in `docs/` inside it, and the state file is `pipeline/state.json`. Create the folders if they are missing.
- **Claude Project on claude.ai (no shared folder):** each output is a document or file you hand the founder. Ask them to add it to the Project's files so later stages can read it. Keep the state as a short "Pipeline status" document in the same format as `state.json`, and give the founder the updated version after every approval.

From stage 5 on, the working folder is the app's own repo: setup copies `docs/` and `pipeline/` into it, and every later change to them goes through a pull request. Stages 5 to 7 need Claude Code, because they run commands and push code.

When an earlier output is needed and you cannot find it, ask the founder for it rather than guessing its contents.

## Project state

The state file records where the project is and every approval. Its format is in [references/state-schema.md](references/state-schema.md). Rules:

- Update it whenever a stage starts, waits for approval, or is approved.
- Record an approval only after the founder approves explicitly (see the gate below).
- If an approved output changes later, set every later stage that used it to `needs_reapproval` and tell the founder which ones.

## The approval gate

Every stage ends at a gate, and nothing moves on without the founder's explicit approval.

1. Summarise the output in plain language, in 10 lines or fewer, and point to the full file.
2. Ask: "Do you approve this, or what should change?"
3. Treat only a clear yes as approval ("approved", "yes, go ahead", "looks good, continue"). A question, a "maybe", or silence is not approval.
4. On changes: make them, show what changed, and ask again.
5. On approval: record it in the state file with the date, then name the next stage and offer to start it. Do not start it on your own.

## Specialist skills

Each stage names specialist skills bundled with this plugin (listed in `THIRD_PARTY_NOTICES.md`). Load one when its step comes up. They supply method and depth, while the stage skill stays in charge:

- The stage's templates, file locations, and approval gate always win. A specialist skill's output is folded into the stage's own files, not saved somewhere else.
- The founder rules below still apply, so translate a specialist skill's jargon before it reaches the founder.
- If a specialist skill is not installed (for example in a Claude Project where it was not uploaded), carry on with the stage skill alone.

## Talking to the founder

The founder is not technical. Every stage follows these rules:

- Use plain words. When a technical term is unavoidable, explain it in one short sentence the first time.
- Ask one question at a time in interviews, and say why you are asking when it is not obvious.
- When there is a choice, give 2 or 3 options with one line each on what changes, and mark your recommendation.
- Never ask the founder to read code, edit files, or run commands.
- Back every claim about the market, prices, or competitors with a link to the page it came from. If you cannot look something up, say so and label the figure as an estimate.
- Keep messages short. Put long material in the output files, not in chat.
