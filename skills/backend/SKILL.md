---
name: backend
description: Stage 7 of the app pipeline. First asks whether a backend already exists or should be built from scratch, then builds the whole backend from the business documentation and the frontend's API contract (with code review and security review), wires it to the approved frontend in place of the mocked data, runs the full app locally, gives the founder the links to test, and waits for approval. Use after the frontend is approved, or when someone runs /backend.
---

# Stage 7: Backend

The frontend already works on mocked data and the founder has approved every page. This stage makes the data real. Follow the shared rules in the `pipeline-core` skill, and the app repo's `CLAUDE.md`.

Requires `frontend` to be `approved`. Reads `docs/06-frontend/api-contract.md` (what the frontend needs), `docs/04-architecture.md` and its decision records, and `docs/01-business/`.

## Refer back to the business documents

The registries are the specification of the backend:

- **Entities & States** become tables and their state columns. **Transitions** become the only way a state changes, with the guard checked on the server and the performer recorded.
- **Rules** are enforced on the server. Fixed rules are code, Governed rules read their configuration from stored settings, Contextual rules are evaluated per request.
- **Permissions** become access control (for Supabase, row level security policies). Every permission ID has a test that proves it allows and denies correctly, with a second user.
- **Attention** tasks and **Notifications** are created by the transitions that the registries name.
- Cite business IDs in migrations, function names and tests (as comments), so a reviewer can trace each piece back. Never show them in the app's text.

Also answer the authenticity guard question for the stage: are the local services and data rules from `AUTHENTICITY.md` respected (payments, sign-in, SMS or OTP, hosting region)? Report Pass, Drift or Profile change needed.

## Specialist skills

| Step | Skill | Use it for |
| --- | --- | --- |
| Start | `grilling` | Pinning down open decisions about data and rules. Answer from the documents where you can; ask the founder only what you cannot |
| Build | `postgres-pro` | Tables, migrations, indexes and row level security policies |
| Build | `typescript-pro`, `software-architecture` | Typed service code, with logic in services and the domain separate from infrastructure |
| Build | `nextjs-developer` | Only when the architecture puts the API in a Next.js app |
| Code review | `code-review`, `code-review-skill`, `code-reviewer` | Standards against `CLAUDE.md`, and Spec against the business rows the code serves |
| Security review | `security-reviewer`, `secure-code-guardian` | The security review, with the checklist |
| Security review | `differential-review`, `insecure-defaults`, `sharp-edges`, `static-analysis`, `supply-chain-risk-auditor`, `fp-check` (extra plugins) | A deeper security pass when installed |
| Testing | `test-master`, `security-testing` | API and integration tests, and authorisation tests |

## Steps

### 1. Ask: existing backend or from scratch?

Ask this first, as a single question with two options and a recommendation, in plain words:

> Do you already have a backend for this app, or should I build one from scratch?
> **A. Build from scratch** (recommended unless you have one): I build it to the architecture you approved.
> **B. I already have one**: I connect the app to it.

Record the answer and the reason in `pipeline/state.json` (`backend.mode`: `"new"` or `"existing"`).

**If it already exists**, ask one question at a time for what you need: where it lives (a repo link, or an API address), what documents its API (OpenAPI file, Postman collection, or docs link), how a test account signs in, and which environment is safe to use for testing. Never ask the founder to paste a secret into chat: have them put values in `.env` (you name the variables), or in the provider's secret store. Then:

1. Read its API and compare it with `docs/06-frontend/api-contract.md`, and with the business registries.
2. Write `docs/07-backend/gap-report.md`: what already matches, what differs (names, shapes, states), what is missing, and what the existing backend does that the business documents do not mention. Mark each gap as **adapt the frontend service layer** (default, since the pages stay untouched), **change the backend** (only if the founder owns it and agrees), or **change the business documents** (a business change, through the business stage's rules).
3. The founder decides each gap that changes cost, scope or what people see. Then continue at step 4 with only the work the gaps require.

**If from scratch**, continue at step 2.

### 2. Plan the backend

Write `docs/07-backend/backend-plan.md`: the data model (tables from the Entities & States rows), the transitions and rules to enforce, the permissions and their policies, the functions or endpoints from `api-contract.md`, and the build order by feature (Shared first, then each feature in the register's order). Map each item to its business IDs. Keep it to what the founder can skim in 10 minutes, and run the gate-sized summary by them only if the plan changes the approved architecture or cost; otherwise continue.

### 3. Build it, feature by feature

For each feature in the order of the plan, on its own branch `backend/<feature-code>-<name>` from an up-to-date `main`:

- Write the migrations, row level security policies, services and functions. Seed data for local use comes from the same realistic records as the frontend mocks.
- Write tests: one per business rule, transition guard and permission the feature owns, plus one per acceptance criterion that depends on the backend.
- Run lint, typecheck and tests until they pass.
- Run the **code review** (`code-review`, Spec against the feature's registries rows) and the **security review** (`security-reviewer`) from [../frontend/references/review-checklist.md](../frontend/references/review-checklist.md). Fix every real finding and rerun.
- Open a pull request with the frontend's PR template, labelled `backend`, wait for green CI, squash-merge. Never skip, disable or weaken a test to get green.

The founder is not asked to approve each feature here, because backend work has nothing to try on its own. They approve the working whole in step 6.

### 4. Wire it to the frontend

When the whole backend is merged, on a branch `wire/backend`:

- Add the real implementations behind the same service interfaces in `src/services/`, and switch the app from `src/services/mock/` to them by configuration. Keep the mocks for tests.
- Read every address and key from `.env` (add the names to `.env.example`). No secret in code.
- Run the frontend's tests against the real services where they apply, and fix mismatches in the service layer, not by editing the pages.
- Review the wiring diff with both reviews, then merge as in step 3.

### 5. Run it locally

Start the whole app on the founder's machine: the backend (for Supabase, the local stack), the database with seed data, and the app. Check yourself first that a person can sign up, sign in, and complete the main journey from the D3 documents. Then give the founder **the full links**, in one short list:

- the app (web link, and for mobile the Expo QR code for Expo Go),
- the backend's admin or API address, if there is something for them to look at (for example the local database dashboard),
- the test accounts, one per role, with their passwords for this local run only.

Add a "what to try" checklist built from the Phase 1 stories, written as actions, covering at least one journey per feature. Say clearly that this is a local copy with test data, and that nothing is deployed.

### 6. Approval gate

Set `backend` to `awaiting_approval` and ask: "Does the app work end to end the way you want? Approve it, or tell me what to change." Do not move on until the founder says yes after trying it.

- **Changes requested:** fix on a new branch with the same reviews, rerun step 5, and ask again. If a change contradicts the business documents, confirm it first and update them through the business stage's rules.
- **Approved:** record it in the state file with the date and offer to start stage 8 (QA).
