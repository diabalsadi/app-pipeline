# App Pipeline

A Claude Code plugin that takes a non-technical founder from an idea to a tested web or mobile app. It runs in 7 stages, and nothing moves forward until the founder approves.

| # | Stage | Command | Output |
| --- | --- | --- | --- |
| 1 | Discover | `/discover` | Business plan with market research |
| 2 | Validate | `/validate` | Validated requirements and screen list |
| 3 | Design | `/design` | Design persona, style guide, screen mockups |
| 4 | Architect | `/architect` | Code and cloud architecture, monthly cost estimate |
| 5 | Set up | `/setup` | GitHub repo, project scaffold, automated checks |
| 6 | Build | `/build` | Screens built one at a time, each approved and reviewed |
| 7 | QA | `/qa` | Test plan, severity-ranked bugs, fix-and-retest loop |

`/status` shows where a project is and what is waiting on the founder.

The full design is in [docs/blueprint.md](docs/blueprint.md).

## Status

Blueprint drafted and under review. No stages are built yet.
