---
description: Show where the app project stands and what is waiting on the founder
---

Load the `pipeline-core` skill. Read `pipeline/state.json` in the current folder. If it does not exist, say that no app project has started here and offer to begin with `/discover`.

Otherwise reply in plain language, in 8 lines or fewer:

1. The app's name, and the current stage with its status.
2. Every stage that is approved, with its date.
3. What is waiting on the founder right now, if anything.
4. Any stage marked `needs_reapproval`, and why.
5. During the build stage, how many screens are done out of the total.
6. The next step, written as the command to run.
