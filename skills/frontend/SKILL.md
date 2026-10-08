---
name: frontend
description: Stage 6 of the app pipeline. Builds the app's frontend one page at a time with mocked data, in the order of the approved screen list - each page is built from its design mockup and business stories, the founder tries it and approves it, it passes code review and security review, and only then does the next page start. Use after setup is approved, or when someone runs /frontend or asks to continue building pages.
---

# Stage 6: Frontend, one page at a time, with mocked data

The frontend is finished before any backend exists. Every page runs on mocked data, and a page reaches `main` only after the founder has tried it and approved it, and after it passes code review and security review. Follow the shared rules in the `pipeline-core` skill, and the app repo's `CLAUDE.md`.

Requires `setup` to be `approved`. Works from the `screens` list in `pipeline/state.json`.

## Refer back to the business documents

Every page traces to `docs/01-business/`:

- The page's user stories and their acceptance criteria (by ID) are its test list. Cite the IDs in the page's tests and in its pull request.
- The entities, states, rules and permissions the page shows decide its mock data and its states. Use the exact names and state values from the Entities & States tab.
- The D3 moments for the page decide what the person sees and decides on it.

Also answer the authenticity guard question for each page (does it pass on language, direction, formats, tone and imagery from `docs/02-authenticity/AUTHENTICITY.md`?) and report Pass, Drift or Profile change needed.

## Mocked data

- Put all data access behind a service interface in `src/services/`, with a mock implementation in `src/services/mock/`. Pages call the interface, never the mock directly. This is what lets the backend stage swap the mocks for the real thing without touching the pages.
- Shape every mock record like the entity in the registries (same fields, same state values, same IDs where the registries define them). Use realistic local names, places, currencies and dates from the authenticity profile, in every language the product supports. Never "John Doe" or lorem ipsum.
- Mock the failures too: slow responses, empty results, errors, and a permission that is missing, so every state in the mockup can be reached.
- Record every service function in `docs/06-frontend/api-contract.md` as it is created: name, input, output, and the business IDs it serves. The backend stage builds to this file.

## Specialist skills

| Step | Skill | Use it for |
| --- | --- | --- |
| Start | `grilling` | Pinning down anything the page's stories leave open before coding. Answer from the documents where you can; ask the founder only what you cannot |
| Build | `frontend-design` | Keeping the page as distinctive as its mockup, and not drifting to generic defaults while coding |
| Build | `react-native-expert` or `nextjs-developer`, with `react-expert` and `typescript-pro` | Implementation patterns for the chosen stack |
| Build | `ui-ux-pro-max`, `microinteractions` | Stack-specific UI guidelines, and feedback on taps, saves and errors |
| Build | `threejs-skills` (extra plugin) | Only for a web page that needs a 3D scene |
| Polish | `impeccable` (extra plugin) | Its polish and audit commands before the founder sees the page |
| Code review | `code-review` | The main review: Standards against `CLAUDE.md`, and Spec against the page's stories. The spec source is the registries and D2 in `docs/01-business/` |
| Code review | `code-review-skill`, `code-reviewer` | Language guides (TypeScript, React) and the common-bugs checklist |
| Security review | `security-reviewer`, `secure-code-guardian` | The security review in step 5, with the checklist |
| Security review | `differential-review`, `insecure-defaults`, `sharp-edges`, `static-analysis`, `supply-chain-risk-auditor` (Trail of Bits extra plugins) | A deeper security pass when installed. Run `supply-chain-risk-auditor` whenever the change adds a dependency |
| Security review | `fp-check` (extra plugin) | Confirming a security finding is real before acting on it |
| Structure | `software-architecture` | Keeping logic in services and pages thin |

## The loop

Repeat for each screen in list order. A later page may depend on an earlier one, so never skip ahead unless the founder asks.

### 1. Start the page

- Pick the first screen whose status is `not_started` (or `changes_requested`), and set it to `in_progress` in the state file.
- Read its row in the screen list, its stories and acceptance criteria (by ID), and its mockup `docs/03-design/screens/<id>-<name>.html`.
- Create a branch from an up-to-date `main`: `screen/<id>-<name>`, for example `screen/S03-sign-up`.

### 2. Build it

- Match the mockup closely, using only theme tokens. Build every state the mockup shows: default, empty, loading, error, and success. Mirror correctly for right-to-left languages.
- Add the page's service functions and mocks as above, and update `api-contract.md`.
- Write tests: at least one per acceptance criterion, covering what the person sees and does, not internal details.
- Run `npm run lint`, `npm run typecheck`, and `npm test`, and fix everything until all three pass.

### 3. Let the founder try it

- Start the app (`npm start`). For mobile, show the Expo QR code so the founder can open the page in Expo Go on their phone. For web, give the local link. Say clearly that the data on screen is made up.
- Send a short "what to try" checklist built from the acceptance criteria, written as actions ("Leave the email empty and tap Continue: you should see 'Enter your email'").
- Set the screen to `awaiting_founder`, then ask: "Does this page work the way you want? Approve it, or tell me what to change."

### 4. Founder decision

- **Changes requested:** set the screen to `changes_requested`, apply the changes on the same branch (updating tests), and go back to step 3. If a change contradicts the approved business documents or design, say so and confirm before making it. A confirmed change is also written back to the business documents (through the business stage's rules) or the mockup, and the affected stages are marked `needs_reapproval`.
- **Approved:** record the approval with the date in the state file's history, then continue.

### 5. Code review and security review

Set the screen to `in_review`. Run both reviews on the branch's diff against `main`, using the checklist in [references/review-checklist.md](references/review-checklist.md):

1. **Code review** with the `code-review` skill, from `main` as the fixed point: Standards against `CLAUDE.md` and the checklist's standards section, and Spec against the page's stories.
2. **Security review** with `security-reviewer` against the checklist's security section, plus the Trail of Bits plugins if they are installed.

Fix every finding that is a real problem. If a fix changes what the founder sees or does, go back to step 3 for that part. Rerun lint, typecheck, and tests after the fixes. Record each finding and its outcome for the pull request.

### 6. Pull request and merge

- Push the branch and open a pull request with the template in [references/pr-template.md](references/pr-template.md), labelled `screen`.
- Wait for CI. If it is red, fix the cause and push again. Never skip, disable, or weaken a test to get green.
- When CI is green, squash-merge it and delete the branch.
- Set the screen to `done` in the state file with its pull request URL in `pr`, and add a history entry.

### 7. Next page

Tell the founder in one line what was merged and which page comes next, then start it. Every 3 to 4 pages, offer a short pause to try the pages together, since flows between pages matter as much as single pages.

## Finishing the stage

When every screen is `done`, ask the founder to try the whole app from start to finish once, following the D3 journeys. Collect any changes as new page rounds (back to step 1 for that page). Then set `frontend` to `awaiting_approval`, run the gate from `pipeline-core`, and once the founder approves, offer to start stage 7 (backend).

## Screen statuses

`not_started`, `in_progress`, `awaiting_founder`, `changes_requested`, `in_review` (the reviews in step 5), `done`.
