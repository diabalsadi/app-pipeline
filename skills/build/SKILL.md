---
name: build
description: Stage 6 of the app pipeline. Builds the app one screen at a time in the order of the approved screen list - each screen gets its own branch and tests, the founder tries it and approves it, it passes code review and security review, then its pull request is merged. Use after setup is approved, or when someone runs /build or asks to continue building screens.
---

# Stage 6: Build, one screen at a time

A screen reaches `main` only after the founder has tried it and approved it, and after it passes both code review and security review. Follow the shared rules in the `pipeline-core` skill, and the app repo's `CLAUDE.md`.

Requires `setup` to be `approved`. Works from the `screens` list in `pipeline/state.json`.

## Specialist skills

| Step | Skill | Use it for |
| --- | --- | --- |
| Build | `ui-ux-pro-max` | React Native and web implementation guidelines for the chosen stack |
| Build | `microinteractions` | Feedback on taps, saves, and errors |
| Build | `threejs-skills` (optional plugin) | Only for a web screen that needs a 3D scene |
| Polish | `impeccable` (optional plugin) | Its polish and audit commands before the founder sees the screen |
| Code review | `code-review` or `engineering:code-review` | The standards review in step 5 |
| Security review | `security-review` | The security review in step 5 |
| Structure | `software-architecture` | Keeping logic in services and screens thin |

## The loop

Repeat for each screen in list order. A later screen may depend on an earlier one, so never skip ahead unless the founder asks.

### 1. Start the screen

- Pick the first screen whose status is `not_started` (or `changes_requested`), and set it to `in_progress` in the state file.
- Read its row in the screen list, its user stories and acceptance criteria, and its mockup `docs/03-design/screens/<id>-<name>.html`.
- Create a branch from an up-to-date `main`: `screen/<id>-<name>`, for example `screen/S03-sign-up`.

### 2. Build it

- Match the mockup closely, using only theme tokens. Build every state the mockup shows: default, empty, loading, error, and success.
- Put data access and business logic in `src/services/`. If the screen needs new tables, add a migration with row level security policies.
- Write tests: at least one per acceptance criterion, covering what the user sees and does, not internal details.
- Run `npm run lint`, `npm run typecheck`, and `npm test`, and fix everything until all three pass.

### 3. Let the founder try it

- Start the app (`npm start`). For mobile, show the Expo QR code so the founder can open the screen in Expo Go on their phone. For web, give the local link.
- Send a short "what to try" checklist built from the acceptance criteria, written as actions ("Leave the email empty and tap Continue: you should see 'Enter your email'").
- Set the screen to `awaiting_founder`, then ask: "Does this screen work the way you want? Approve it, or tell me what to change."

### 4. Founder decision

- **Changes requested:** set the screen to `changes_requested`, apply the changes on the same branch (updating tests), and go back to step 3. If a change contradicts the approved requirements or design, say so and confirm before making it. Accepted changes are also written back into `docs/02-requirements.md` or the mockup.
- **Approved:** record the approval with the date in the state file's history, then continue.

### 5. Code review and security review

Set the screen to `in_review`. Run both reviews on the branch's diff against `main`, using the checklist in [references/review-checklist.md](references/review-checklist.md):

1. **Code review** against `CLAUDE.md` and the checklist's standards section.
2. **Security review** against the checklist's security section.

Fix every finding that is a real problem. If a fix changes what the founder sees or does, go back to step 3 for that part. Rerun lint, typecheck, and tests after the fixes. Record each finding and its outcome for the pull request.

### 6. Pull request and merge

- Push the branch and open a pull request with the template in [references/pr-template.md](references/pr-template.md), labelled `screen`.
- Wait for CI. If it is red, fix the cause and push again. Never skip, disable, or weaken a test to get green.
- When CI is green, squash-merge it and delete the branch.
- Set the screen to `done` in the state file with its pull request URL in `pr`, and add a history entry.

### 7. Next screen

Tell the founder in one line what was merged and which screen comes next, then start it. Every 3 to 4 screens, offer a short pause to try the screens together, since flows between screens matter as much as single screens.

## Finishing the stage

When every screen is `done`, ask the founder to try the whole app from start to finish once. Collect any changes as new screen rounds (back to step 1 for that screen). Then set `build` to `awaiting_approval`, run the gate from `pipeline-core`, and once the founder approves, offer to start stage 7 (QA).

## Screen statuses

`not_started`, `in_progress`, `awaiting_founder`, `changes_requested`, `in_review` (the reviews in step 5), `done`.
