# App Pipeline

A Claude pipeline that takes a non-technical founder from an idea to a tested web or mobile app. It runs in 8 stages, and nothing moves forward until the founder approves. It stops when QA passes and does not deploy.

| # | Stage | Command | Output | Built |
| --- | --- | --- | --- | --- |
| 1 | Business | `/business` | Business documentation to the OP standard: a file group per feature | Yes |
| 2 | Authenticity | `/authenticity` | Authenticity profile, card and design brief, looped until it passes | Yes |
| 3 | Design | `/design` | Screen list, personas, style guide, design tokens, clickable mockups | Yes |
| 4 | Architect | `/architect` | Code and cloud architecture, monthly cost estimate | Yes |
| 5 | Set up | `/setup` | GitHub repo, project scaffold, automated checks | Yes |
| 6 | Frontend | `/frontend` | Every page built on mocked data, one page at a time, each approved and reviewed | Yes |
| 7 | Backend | `/backend` | Backend built or connected, wired to the frontend, running locally for you to test | Yes |
| 8 | QA | `/qa` | Test plan, bugs as GitHub issues, fix-and-retest loop | Yes |

Every stage refers back to the business documents and ends with your approval.

`/status` shows where a project is and what is waiting on the founder.

The full design is in [docs/blueprint.md](docs/blueprint.md).

## Install it as a Claude Code plugin

### What you need first

- [Claude Code](https://code.claude.com/docs/en/setup), signed in.
- `git`, Node.js (the current LTS release), and the GitHub CLI `gh`, signed in with `gh auth login`. Stages 5 to 8 use them to create the app's repo and push code. The pipeline checks for them at stage 5 and walks you through anything missing.
- To try a mobile app on your phone during the frontend stage, the free Expo Go app (iOS or Android).

### Add the marketplace and install

This repo is its own plugin marketplace. In Claude Code, run:

```
/plugin marketplace add diabalsadi/app-pipeline
/plugin install app-pipeline-full@app-pipeline
```

Or from a terminal:

```bash
claude plugin marketplace add diabalsadi/app-pipeline
claude plugin install app-pipeline-full@app-pipeline
```

Restart Claude Code afterwards so the new commands and skills load.

The repo is private, so adding the marketplace needs a GitHub login that can read it: `gh auth login` is enough, or set `GITHUB_TOKEN` to a token with read access.

### Pick what to install

| Plugin | What you get | Always-on context |
| --- | --- | --- |
| `app-pipeline-full` (recommended) | The pipeline, its 54 bundled skills, and all 26 extra plugins listed below | about 86,000 tokens |
| `app-pipeline` | The pipeline and its 54 bundled skills only | about 12,000 tokens |

"Always-on context" is the skill descriptions Claude reads at the start of every session, measured with `claude plugin details`. Every stage works with either install; the extras add depth where a stage names them.

To drop extras you don't use from the full install, turn off the bundle first (that keeps everything installed), then turn off the ones you don't want:

```bash
claude plugin disable app-pipeline-full@app-pipeline
claude plugin disable team-motivation@app-pipeline
```

### Update or remove

```bash
claude plugin marketplace update app-pipeline   # fetch the latest version
claude plugin uninstall app-pipeline-full@app-pipeline
```

## How to use it

Each app gets its own folder. Make an empty folder, open Claude Code in it, and run `/business`. From there, Claude leads and you answer.

1. **Business (`/business`).** Claude interviews you one question at a time, then writes the business documentation with the OP method in `docs/01-business/`: it divides the product into features and writes, for each one, a concept, a features list and journeys (Word) plus a registries workbook (Excel), and one Shared group for the whole product. Every fact has one home and one ID. Delivery to Google Drive is optional.
2. **Authenticity (`/authenticity`).** Claude reads those documents, scores who the app is for, where it lives, what it stands for and how it must feel, and asks only about the gaps. If the profile does not pass, it asks more and tries again, until it does. You then approve it. The result is `docs/02-authenticity/`.
3. **Design (`/design`).** Claude lists every screen the business documents call for, writes the personas, offers style directions, and mocks up every screen (phone and web when you need both) in `docs/03-design/`. It uses the frontend design skills for this. Open the `.html` mockups in a browser.
4. **Architect (`/architect`).** Claude picks the stack (React Native with Expo for mobile unless you need something else), draws the architecture, and estimates the monthly cloud cost from current prices.
5. **Set up (`/setup`).** Claude creates a private GitHub repo for the app, scaffolds the project, and adds automated checks. If `gh` is not signed in, it asks you to run `gh auth login`, which is the only command you ever run yourself.
6. **Frontend (`/frontend`).** Claude builds the app one page at a time, on made-up data. For each page you get a QR code (mobile, scan it with Expo Go) or a local link (web), and a short "what to try" list. Approve it or say what to change, and only then does the next page start. Approved pages pass a code review and a security review before they are merged.
7. **Backend (`/backend`).** Claude first asks whether you already have a backend or want one built from scratch. Then it builds or connects it (with the same two reviews), wires it to the frontend in place of the made-up data, runs the whole app on your machine, and gives you the links and test accounts. You try it and approve it.
8. **QA (`/qa`).** Claude writes a test plan from the business documents, runs it, files each bug as a GitHub issue with a severity, fixes them from most to least severe, and reruns everything until a full run is clean.

Every stage ends with a short summary and the question "Do you approve this, or what should change?". Only a clear yes moves the project on, and Claude never starts the next stage on its own; it offers to.

Useful to know:

- **`/status`** shows where the project stands and what is waiting on you. Run it when you come back after a break.
- **You can stop anytime.** Progress is saved in `pipeline/state.json`, so open Claude Code in the same folder later and run `/status` or the next stage's command.
- **Changing your mind** about an earlier stage is fine: run that stage's command again. Later stages that depended on it are marked for re-approval.
- **Notes for a stage** go after the command, for example `/design make it feel calm, like a paper notebook`.
- **Name clashes:** if another plugin also has a `/frontend` or `/design` command, use the full name, such as `/app-pipeline:frontend`.
- The pipeline stops when QA passes. It does not publish the app to the app stores or the web.

## Use it in a Claude Project

Stages 1 to 4 also run in a Claude Project on claude.ai, as uploaded skills.

1. Run `./scripts/package-skills.sh`. It writes one zip per bundled skill to `dist/`. Add `--extras` to also zip the skills of all 26 extra plugins into `dist/extras/<plugin>/`, fetched from each author's repo at the pinned commit.
2. On claude.ai, upload the zips you need under Settings > Capabilities > Skills: at least `pipeline-core` and the stage skills, plus the specialist skills for the stages you will run.
3. Create a Project for the app and say "Start the app pipeline" (or "run the business stage").
4. Add each document Claude hands you (business documents, authenticity profile, style guide) to the Project's files, so later stages can read it.
5. Stages 5 to 8 (setup, frontend, backend, QA) run commands and push code, so they need Claude Code. Take the collected documents into a `docs/` folder and continue there with `/setup`.

The `dist/` folder is not committed. Some extras (`threejs-skills`, which publishes no license, and the Trail of Bits plugins, under CC BY-SA 4.0) can't be copied into this repo, so the zips are for uploading to your own account only.

## Layout

```
.claude-plugin/   plugin and marketplace manifests
commands/         one slash command per stage, plus /status
skills/
  pipeline-core/  shared rules: stage order, state file, approval gates, founder communication
  business/       stage 1 (runs op-business-documentation)
  authenticity/   stage 2 (runs op-authenticity)
  design/         stage 3
  architect/      stage 4
  setup/          stage 5
  frontend/       stage 6
  backend/        stage 7
  qa/             stage 8
  op-business-documentation/  the OP business documentation standard
  op-authenticity/            the OP Authenticity process, library and scripts
  <others>/       bundled third-party skills (see THIRD_PARTY_NOTICES.md)
bundles/          app-pipeline-full, which installs the pipeline plus every extra plugin
toolkit/          pinned sources for the bundled skills and the extra plugins
scripts/          packaging for claude.ai, and the toolkit updater
docs/             the blueprint
```

## Bundled specialist skills

The stages call on 42 third-party skills that ship inside this plugin, each pinned to a reviewed commit. `THIRD_PARTY_NOTICES.md` lists each one with its source and license. `op-business-documentation` and `op-authenticity` are the OP method's own skills and are maintained in this repo.

| Stage | Skills |
| --- | --- |
| Business | `op-business-documentation`, `grilling`, `grill-me` |
| Authenticity | `op-authenticity` |
| Design | `frontend-design`, `ui-ux-pro-max` (both required), `apple-design-system`, `brand-guidelines`, `refactoring-ui`, `web-typography`, `ios-hig-design`, `microinteractions`, `ux-heuristics` |
| Architect | `drawio-skill`, `software-architecture` |
| Frontend and backend | `react-native-expert`, `react-expert`, `nextjs-developer`, `typescript-pro`, `postgres-pro`, `code-review`, `code-review-skill`, `code-reviewer`, `security-reviewer`, `secure-code-guardian` |
| QA | `uat-testing`, `quality-assurance`, `qa-project-context`, `test-strategy`, `risk-based-testing`, `test-master`, `test-data-management`, `playwright-cli`, `playwright-automation`, `playwright-expert`, `mobile-testing`, `accessibility-testing`, `visual-testing`, `performance-testing`, `security-testing`, `payment-testing`, `bug-reproduction`, `ai-bug-triage`, `debugging-wizard` |

The earlier market-research and positioning skills (`mom-test`, `jobs-to-be-done`, `competitor-profiling`, `pricing` and the rest) are no longer bundled, since the business stage now follows the OP standard. `app-pipeline-full` still installs the extra plugins that include some of them.

To update one, change its commit in `toolkit/sources.json`, run `python3 scripts/update-toolkit.py`, and review the diff. The same script regenerates the marketplace and the full bundle's dependency list from `toolkit/extras.json`.

## Extra plugins

`app-pipeline-full` installs these 26 plugins along with the pipeline. They install straight from each author's repo at a pinned commit (`toolkit/extras.json`) and are not copied here. With the lean install, add any of them on its own, for example `/plugin install impeccable@app-pipeline`.

| Plugin | What it adds | Source |
| --- | --- | --- |
| `impeccable` | Design polish, audits, and critique commands. Its hooks run after every file edit and download a native binary from the project's releases | pbakaus/impeccable |
| `threejs-skills` | 10 Three.js skills for 3D on the web. No license is published | CloudAI-X/threejs-skills |
| `marketing-skills` | 40+ marketing skills: SEO, copy, launch, ads, onboarding, pricing | coreyhaines31/marketingskills |
| `ccc-skills` | 15 skills: Excalidraw, landing pages, UAT testing, pitch decks, analytics setup | ooiyeefei/ccc |
| `example-skills`, `document-skills` | Anthropic's skills: frontend design, web app testing, theme factory, Word, Excel, PowerPoint, PDF | anthropics/skills |
| `differential-review`, `insecure-defaults`, `static-analysis`, `supply-chain-risk-auditor`, `sharp-edges`, `fp-check`, `spec-to-code-compliance` | Trail of Bits security review tools (CC BY-SA 4.0). `fp-check` adds a completeness check at the end of every turn | trailofbits/skills |
| `fullstack-dev-skills` | All 67 full-stack skills and workflow commands | jeffallan/claude-skills |
| `mattpocock-skills` | All of Matt Pocock's engineering skills: TDD, specs, tickets, domain modelling | mattpocock/skills |
| `qa-skills` | All 40+ QA skills, including contract, chaos, and synthetic monitoring | petrkindlmann/qa-skills |
| `product-strategy`, `ux-design`, `marketing-cro`, `sales-influence`, `product-innovation`, `strategy-growth`, `team-motivation`, `code-craftsmanship`, `systems-architecture`, `metaskills` | 10 book-based collections, about 70 skills in all | wondelai/skills |

Each plugin adds its skill descriptions to every session (about 73,000 tokens for all 26 together). In a Claude Project, `package-skills.sh --extras` packages their skills as zips.

## Key defaults

- Mobile apps are cross-platform React Native (Expo) unless the founder has a hard requirement for another stack.
- QA bugs become GitHub issues in the app's repo. The pull request that fixes a bug links its issue and closes it on merge.
