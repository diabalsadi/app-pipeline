---
name: qa
description: Stage 8 of the app pipeline. Writes a test plan from the business documentation, runs automated end-to-end and exploratory tests, files every bug as a GitHub issue with a severity label, fixes bugs highest severity first through reviewed pull requests that close their issues on merge, and reruns the whole plan until a full run is clean. Use after the backend is approved, or when someone runs /qa.
---

# Stage 8: QA

The app is finished only after a full test run finds no open bugs. Follow the shared rules in the `pipeline-core` skill, and the app repo's `CLAUDE.md`. The pipeline ends here and does not deploy.

Requires `backend` to be `approved`. The test plan comes from the business documents in `docs/01-business/` and the authenticity profile in `docs/02-authenticity/`, and every test and bug cites the business IDs it concerns.

## Specialist skills

| Step | Skill | Use it for |
| --- | --- | --- |
| Context | `qa-project-context` | Writing `.agents/qa-project-context.md` from the business documents and architecture, so the QA skills below share the same facts |
| Test plan | `quality-assurance`, `test-strategy`, `risk-based-testing` | Quality gates, choosing what to test hardest, and the right mix of unit, integration, and end-to-end tests |
| Test plan | `uat-testing`, `test-master` | Turning acceptance criteria into exhaustive test cases |
| Test data | `test-data-management` | Seed users and data for repeatable runs |
| Web end-to-end | `playwright-cli`, `playwright-automation`, `playwright-expert` | Driving the browser, and writing stable Playwright tests. `webapp-testing` (extra `example-skills` plugin) also works |
| Mobile end-to-end | `mobile-testing` | Maestro flows on simulators and emulators |
| Specialised passes | `accessibility-testing`, `visual-testing`, `performance-testing`, `security-testing`, `payment-testing` | One pass each, where the app needs it |
| Bugs | `bug-reproduction`, `ai-bug-triage` | Minimal reproduction steps, duplicate detection, and severity ranking (map the result onto `severity.md`) |
| Fixing | `debugging-wizard` | Finding the root cause before fixing |
| Compliance | `spec-to-code-compliance` (Trail of Bits extra plugin) | Checking the code against every requirement before the final run |
| Polish | `impeccable` (extra plugin) | Its audit command as an extra pass on visual and UX quality |
| Fix review | `code-review`, `security-reviewer` | Reviewing every fix, as in the frontend stage |

The whole `qa-skills` collection is also installed by `app-pipeline-full` as an extra plugin.

## Steps

### 1. Write the test plan

Create `docs/08-qa/test-plan.md` from [references/test-plan-template.md](references/test-plan-template.md):

- Every acceptance criterion in the business registries (user stories, or activities and scenarios for engine-driven products) becomes at least one test case (TC-001 and on), linked to its business ID. Every business rule, transition guard and permission gets a case too, including a denied case.
- Add end-to-end journeys for the main task, sign-up to first success, and payment if the app takes money.
- Add an accessibility pass, a basic performance check (time to first usable screen, scrolling long lists), a security pass using the frontend stage's checklist, and an edge-case pass (offline, slow network, long text, empty data, a second user), and a locale pass from the authenticity profile (right-to-left mirroring, long text in each language, date, currency and phone formats), walked as the profile's personas.
- Mark each case as automated or manual.

Show the founder a short summary: how many cases there are, what is automated, and what will be checked by hand.

### 2. Automate what can be automated

- **Mobile:** Maestro flows in `.maestro/`, one per journey, run on an iOS simulator or Android emulator.
- **Web:** Playwright tests in `e2e/`. Use the project's own Playwright (`npx playwright`) for `playwright-cli` commands; install the global CLI (`npm install -g @playwright/cli`) only if the project has none.
- Unit and component tests already exist from the frontend stage. Add any acceptance criterion that is still missing.
- Add the end-to-end run to CI if it can run there. If it needs a device, run it locally and attach the results to the test run file.

### 3. Run the full plan

Run every case, automated and manual, on the current `main`. Record the results in `docs/08-qa/runs/run-<n>.md`: the date, the commit, and passed, failed, or blocked for each case, with evidence (a log, screenshot, or recording) for every failure.

### 4. File each bug as an issue

For each failure, first search the open issues for a duplicate (`gh issue list --label bug --search "<words>"`). If there is none, create one using [references/bug-issue-template.md](references/bug-issue-template.md):

```bash
gh issue create --title "<what is wrong, where>" --label bug --label "severity: <level>" --body-file <file>
```

Rank the severity with [references/severity.md](references/severity.md). Tell the founder the counts by severity in one line, and describe any critical bug in plain words.

### 5. Fix, highest severity first

Fix open bugs in order: critical, high, medium, then low. For each bug:

1. Create a branch from up-to-date `main`: `fix/<issue>-<short-name>`.
2. Write a test that reproduces the bug and fails, then fix the cause until it passes.
3. Run lint, typecheck, and tests.
4. Run the code review and security review from the frontend stage's checklist on the diff, and fix the findings.
5. If the fix changes something the founder sees or does, show them and get their approval first.
6. Open a pull request with the bug-fix template from the frontend stage. The body must contain `Fixes #<issue>`, so the issue closes when the pull request merges.
7. When CI is green, squash-merge it. Confirm the issue closed; if it did not, close it with a comment linking the pull request.

Group fixes only when they share one cause, with one `Fixes #` line per issue.

### 6. Rerun everything

After a batch of fixes (at least every critical or high fix), rerun the whole test plan on the new `main` as a new run file, not only the fixed cases, since a fix can break something else. New failures go back to step 4.

### 7. Exit

QA is done when one full run passes with no failures and no open `bug` issues remain. Write `docs/08-qa/report.md`: the number of runs, bugs found and fixed by severity, the final run's results, and anything the founder chose to accept. Set `qa` to `awaiting_approval` and run the gate from `pipeline-core`. When the founder approves, the pipeline is complete. Tell them the app is tested and ready for a release, which is outside this pipeline.

## Rules

- Never skip, disable, or weaken a test to make a run pass.
- A bug the founder decides not to fix is closed as "not planned" with their reason in a comment, and listed in the report.
