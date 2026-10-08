# CLAUDE.md template

Write this into the app repo's root as `CLAUDE.md`, filling in the brackets. Keep it short: it is read at the start of every session and used as the standard in every code review.

```markdown
# [App name]

[One sentence on what the app does and for whom.] Built with the app pipeline: product docs live in `docs/` and pipeline state in `pipeline/state.json`.

## Stack
- [Expo (React Native) with Expo Router, TypeScript strict] / [Next.js App Router, TypeScript strict]
- Backend: [Supabase: Postgres, Auth, Storage]
- Tests: [Jest with React Native Testing Library] / [Vitest]; end-to-end: [Maestro] / [Playwright]

## Commands
- `npm start`: run the app
- `npm run lint`, `npm run typecheck`, `npm test`: must all pass before any pull request

## Rules
- Work on a branch, and merge to `main` only through a pull request with green checks.
- One screen or one bug fix per pull request.
- Every colour, size, and font comes from `src/theme/tokens.ts`. Never hard-code them.
- Screens match their approved mockup in `docs/03-design/screens/`. Any visible change needs the founder's approval.
- Every user story's acceptance criteria have tests. A bug fix starts with a test that fails.
- Prefer a well-maintained library to custom code for solved problems (dates, forms, validation).
- Keep business logic out of screens: screens call `src/services/`, and services hold the logic.
- Keep functions under about 50 lines and files under about 200. Split by responsibility.
- Use early returns instead of deep nesting.
- Handle loading, empty, and error states on every screen that fetches data.
- Never commit secrets. New secrets are added to `.env.example` by name only.
- Every database table has row level security, with a policy per role.
- Validate all user input on the server side as well as in the form.
- Accessibility: every touchable element has an accessible label, and text contrast is at least 4.5:1.

## Pull request description
Link the screen ID or the issue (`Fixes #12`), list the acceptance criteria covered, and summarise the code review and security review results.
```
