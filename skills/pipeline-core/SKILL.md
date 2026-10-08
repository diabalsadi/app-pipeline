---
name: pipeline-core
description: Shared rules for the app pipeline that every stage follows - stage order, the project state file, approval gates, and how to talk to a non-technical founder. Load before running any pipeline stage (business, authenticity, design, architect, setup, frontend, backend, qa) or when asked where an app project stands.
---

# App pipeline: shared rules

The app pipeline takes a non-technical founder from an idea to a tested web or mobile app. Every stage skill (`business`, `authenticity`, `design`, `architect`, `setup`, `frontend`, `backend`, `qa`) follows the rules in this file.

## Stage order

| # | Stage | Skill | Main output | Needs approved |
| --- | --- | --- | --- | --- |
| 1 | Business | `business` (with `op-business-documentation`) | `docs/01-business/`: a file group per feature | nothing |
| 2 | Authenticity | `authenticity` (with `op-authenticity`) | `docs/02-authenticity/`: profile, card, design brief | Business |
| 3 | Design | `design` | `docs/03-design/`: screen list, mockups, style guide | Authenticity |
| 4 | Architect | `architect` | `docs/04-architecture.md`, `docs/04-cost-estimate.md` | Design |
| 5 | Set up | `setup` | the app's GitHub repo | Architect |
| 6 | Frontend | `frontend` | every page built on mocked data, one page at a time | Set up |
| 7 | Backend | `backend` | the backend, wired to the frontend and running locally | Frontend |
| 8 | QA | `qa` | a clean full test run | Backend |

The pipeline ends when QA passes. It never deploys the app to production.

## Every stage refers back to the business

The business documents in `docs/01-business/` are the source of truth for what the product is and does. Every later stage:

1. Reads the parts of them it needs before it starts, and cites the business IDs (for example `BIL-INV-US-12`) for the things it produces: screens, pages, tables, tests and bugs.
2. Never contradicts them. If a stage finds that a business document is wrong, thin or missing something, it does not quietly work around it: it states the change, gets the founder's confirmation, makes the change through the business stage's rules, and marks the stages that used the old version `needs_reapproval`.
3. Answers the authenticity guard question for its stage (`skills/op-authenticity/references/guard.md`) from stage 3 on, and reports Pass, Drift or Profile change needed in its approval summary.

The authenticity stage is a loop: it repeats until the profile passes the pass rules, and only then goes to the founder's approval.

Before starting a stage, read the project state (below). If the stage it needs is not `approved`, tell the founder which stage comes first and offer to start that one instead. Never skip a stage.

## Where files live

Detect which environment you are in and use the matching storage:

- **Claude Code (or any session with a working folder):** one folder per app project. Outputs go in `docs/` inside it, and the state file is `pipeline/state.json`. Create the folders if they are missing.
- **Claude Project on claude.ai (no shared folder):** each output is a document or file you hand the founder. Ask them to add it to the Project's files so later stages can read it. Keep the state as a short "Pipeline status" document in the same format as `state.json`, and give the founder the updated version after every approval.

From stage 5 on, the working folder is the app's own repo: setup copies `docs/` and `pipeline/` into it, and every later change to them goes through a pull request. Stages 5 to 8 need Claude Code, because they run commands and push code.

When an earlier output is needed and you cannot find it, ask the founder for it rather than guessing its contents.

## Project state

The state file records where the project is and every approval. Its format is in [references/state-schema.md](references/state-schema.md). Rules:

- Update it whenever a stage starts, waits for approval, or is approved.
- Record an approval only after the founder approves explicitly (see the gate below).
- If an approved output changes later, set every later stage that used it to `needs_reapproval` and tell the founder which ones.

## The approval gate

Every stage ends at a gate, and nothing moves on without the founder's explicit approval.

1. Summarise the output in plain language, in 10 lines or fewer, say which business documents it traces to, and point to the full file.
2. Ask: "Do you approve this, or what should change?"
3. Treat only a clear yes as approval ("approved", "yes, go ahead", "looks good, continue"). A question, a "maybe", or silence is not approval.
4. On changes: make them, show what changed, and ask again.
5. On approval: record it in the state file with the date, then name the next stage and offer to start it. Do not start it on your own.

## Specialist skills

Each stage names specialist skills: most are bundled with this plugin (listed in `THIRD_PARTY_NOTICES.md`), and some come from the extra plugins that `app-pipeline-full` installs. Load one when its step comes up. They supply method and depth, while the stage skill stays in charge:

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
