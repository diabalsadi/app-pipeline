# App Pipeline

A Claude pipeline that takes a non-technical founder from an idea to a tested web or mobile app. It runs in 7 stages, and nothing moves forward until the founder approves. It stops when QA passes and does not deploy.

| # | Stage | Command | Output | Built |
| --- | --- | --- | --- | --- |
| 1 | Discover | `/discover` | Business plan with market research | Yes |
| 2 | Validate | `/validate` | Validated requirements and screen list | Yes |
| 3 | Design | `/design` | Personas, style guide, design tokens, clickable screen mockups | Yes |
| 4 | Architect | `/architect` | Code and cloud architecture, monthly cost estimate | Yes |
| 5 | Set up | `/setup` | GitHub repo, project scaffold, automated checks | Not yet |
| 6 | Build | `/build` | Screens built one at a time, each approved and reviewed | Not yet |
| 7 | QA | `/qa` | Test plan, bugs as GitHub issues, fix-and-retest loop | Not yet |

`/status` shows where a project is and what is waiting on the founder.

The full design is in [docs/blueprint.md](docs/blueprint.md).

## Use it in Claude Code

```
/plugin marketplace add diabalsadi/app-pipeline
/plugin install app-pipeline@app-pipeline
```

Then make an empty folder for the new app, open Claude Code in it, and run `/discover`.

## Use it in a Claude Project

1. Run `./scripts/package-skills.sh`. It writes one zip per skill to `dist/`.
2. On claude.ai, upload each zip under Settings > Capabilities > Skills.
3. Create a Project for the app and say "Start the app pipeline" (or "run the discover stage").
4. Add each document Claude hands you (business plan, requirements, style guide) to the Project's files, so later stages can read it.

## Layout

```
.claude-plugin/   plugin and marketplace manifests
commands/         one slash command per stage, plus /status
skills/
  pipeline-core/  shared rules: stage order, state file, approval gates, founder communication
  discover/       stage 1
  validate/       stage 2
  design/         stage 3
  architect/      stage 4
scripts/          packaging for claude.ai
docs/             the blueprint
```

## Key defaults

- Mobile apps are cross-platform React Native (Expo) unless the founder has a hard requirement for another stack.
- QA bugs become GitHub issues in the app's repo. The pull request that fixes a bug links its issue and closes it on merge.
