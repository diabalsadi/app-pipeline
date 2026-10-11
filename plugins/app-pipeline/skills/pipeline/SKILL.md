---
name: pipeline
description: Front door of the app pipeline. Starts or continues an app project by stage - say "pipeline business", "pipeline design", "pipeline next" or "pipeline status" (stages: business, authenticity, design, architect, setup, frontend, backend, qa) - and runs that stage's skill with the shared rules. Use when someone says "start the app pipeline", "run the next stage", "continue my app", or names a pipeline stage.
---

# Pipeline: run a stage by name

One entry point for the eight stages, for places where slash commands are not available (such as claude.ai). Follow the shared rules in the `pipeline-core` skill: load it first.

## What to do

1. Read what the founder asked for. It is one of:
   - a stage name: `business`, `authenticity`, `design`, `architect`, `setup`, `frontend`, `backend`, `qa`
   - `next` (or nothing, or "continue"): the first stage that is not `approved`, in this order
   - `status`: report where the project stands (see below)
2. Read the project state (`pipeline/state.json`, or the "Pipeline status" document in a Claude Project). If there is none, the project has not started: the only stage that can run is `business`, so start it.
3. Check the stage's prerequisite from the stage table in `pipeline-core`. If the stage before it is not `approved`, say which stage comes first and offer to start that one instead. Never skip a stage.
4. Run the stage: load the skill of the same name (`business`, `authenticity`, `design`, `architect`, `setup`, `frontend`, `backend`, `qa`) and follow it exactly, including its approval gate. Pass along any notes the founder gave after the stage name.
5. When the stage is approved, name the next stage and offer to start it. Do not start it on your own.

## Where each stage can run

- `business`, `authenticity`, `design` and `architect` run anywhere, including a Claude Project on claude.ai.
- `setup`, `frontend`, `backend` and `qa` run commands and push code, so they need Claude Code. If asked for one of them elsewhere, say so in one line and tell the founder to continue in Claude Code in the app's folder with `/pipeline <stage>`.

## Status

For `status`, reply in 8 lines or fewer, in plain words:

1. The app's name, and the current stage with its status.
2. Every approved stage, with its date.
3. What is waiting on the founder right now, if anything.
4. Any stage marked `needs_reapproval`, and why.
5. During the frontend stage, how many pages are done out of the total. During authenticity, the round and the latest score.
6. The next step, written as `pipeline <stage>`.

## Not a stage

This skill adds no rules of its own. Specialist skills, templates, outputs and approval gates all come from the stage skills and `pipeline-core`.
