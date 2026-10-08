---
name: setup
description: Stage 5 of the app pipeline. Creates the app's GitHub repo on the founder's account, scaffolds the project from the approved architecture (React Native with Expo by default), wires in the design tokens, and adds automated checks, branch protection, severity labels, and a CLAUDE.md of coding standards. Use after the architecture is approved, or when someone runs /setup.
---

# Stage 5: Set up

Give the app a repo and a skeleton that builds, so every later change is checked automatically. Follow the shared rules in the `pipeline-core` skill.

Requires `architect` to be `approved`. Reads `docs/04-architecture.md`, the decision records, and `docs/03-design/tokens.json`.

**Stages 5 to 8 need Claude Code** (in the terminal, the desktop app, or on the web), because they run commands and push code. In a Claude Project, explain this to the founder and hand over: the `docs/` files they have collected become the starting point of a Claude Code session.

## Steps

### 1. Check the tools

Confirm that `git`, `node` (the current LTS release), and `gh` are available, and that `gh auth status` shows the founder's account. If `gh` is missing or signed out, ask the founder to sign in with `gh auth login` and walk them through it one step at a time. This is the only command they ever run themselves.

### 2. Scaffold the project

Follow [references/scaffold.md](references/scaffold.md) for the stack the architecture chose. In short:

- Create the app with the framework's official generator, in TypeScript strict mode.
- Lay out folders as the reference shows: screens, components, theme, services, and tests.
- Generate the theme module from `docs/03-design/tokens.json`. Every colour, size, and font in the app comes from it.
- Add the test runner, the linter, and a `typecheck` script, so `npm run lint`, `npm run typecheck`, and `npm test` all work.
- Copy the pipeline's `docs/` and `pipeline/` folders into the repo (the business documents, the authenticity profile and `AUTHENTICITY.md` included, so every later stage and every reviewer can read them).
- Add `.env.example` with the name of every secret the architecture needs. Real values go only into `.env` (ignored by git) and the hosting provider's secret store.

### 3. Write the project rules

Create `CLAUDE.md` from [references/claude-md-template.md](references/claude-md-template.md). It holds the coding standards that every build and QA change is reviewed against. Fill it in from the architecture, the authenticity profile's always and never rules, the `software-architecture` skill's principles, and the fixed engineering defaults in the architect stage's `default-stack.md`.

### 4. Create the repo and protect it

Follow [references/github-setup.md](references/github-setup.md):

1. Create a private repo on the founder's account and push the scaffold to `main`.
2. Add the CI workflow from [references/ci.yml](references/ci.yml), adjusted to the stack's scripts.
3. Protect `main` so changes only arrive through a pull request with green checks.
4. Create the severity labels the QA stage uses.

### 5. Prove it runs

- Run lint, typecheck, and tests locally, and wait for the first CI run to pass on GitHub.
- Start the app and show the founder the empty shell: an Expo QR code for their phone (mobile), or a local browser link (web). It should already use the chosen fonts and colours.

### 6. Approval gate

Record the repo URL in `pipeline/state.json`, set `setup` to `awaiting_approval`, and run the gate from `pipeline-core`. In the summary, give the repo link, what runs on every change (in plain words), and how the founder will try screens during the build. Once the founder approves, offer to start stage 6 (build).
