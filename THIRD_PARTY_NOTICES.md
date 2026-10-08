# Third-party notices

The optional plugins in `toolkit/extras.json` are not copied here; they install straight from their authors' repos at pinned commits.

These skills are copied unchanged from the repositories below, at the pinned commits, with each one's license file kept in its folder. Three have a small frontmatter edit: `apple-design-system` and `software-architecture` have narrower descriptions so they only run where the pipeline wants them, and `drawio-skill` drops `disable-model-invocation` so the architect stage can call it. Regenerate this file with `python3 scripts/update-toolkit.py`.

| Skill | Stage | Source | Commit | License |
| --- | --- | --- | --- | --- |
| `frontend-design` | design | [anthropics/skills](https://github.com/anthropics/skills/tree/683bc88e56f3e09ba94f7055977f3d3aa499f202/skills/frontend-design) | `683bc88` | Apache-2.0 |
| `ui-ux-pro-max` | design | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/1a2c459b35f26116fd165b0a0f30597f252749ff/claude/skills/ui-ux-pro-max) | `1a2c459` | MIT |
| `apple-design-system` | design | [rukkiecodes/claude-apple-design-system](https://github.com/rukkiecodes/claude-apple-design-system/tree/a7dc95044bef9d5636bb793d76f532621a15c77e/) | `a7dc950` | MIT |
| `refactoring-ui` | design | [wondelai/skills](https://github.com/wondelai/skills/tree/c172996495bed0fcd26896a9416b2093fd7073f0/refactoring-ui) | `c172996` | MIT |
| `ux-heuristics` | design | [wondelai/skills](https://github.com/wondelai/skills/tree/c172996495bed0fcd26896a9416b2093fd7073f0/ux-heuristics) | `c172996` | MIT |
| `ios-hig-design` | design | [wondelai/skills](https://github.com/wondelai/skills/tree/c172996495bed0fcd26896a9416b2093fd7073f0/ios-hig-design) | `c172996` | MIT |
| `web-typography` | design | [wondelai/skills](https://github.com/wondelai/skills/tree/c172996495bed0fcd26896a9416b2093fd7073f0/web-typography) | `c172996` | MIT |
| `microinteractions` | design | [wondelai/skills](https://github.com/wondelai/skills/tree/c172996495bed0fcd26896a9416b2093fd7073f0/microinteractions) | `c172996` | MIT |
| `drawio-skill` | architect | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill/tree/88fd9236bc532aac4c25cb008a8bd59bc650b904/skills/drawio-skill) | `88fd923` | MIT |
| `uat-testing` | qa | [ooiyeefei/ccc](https://github.com/ooiyeefei/ccc/tree/c0fd92631a09e53eedcb9553f36c074cb0114ddd/skills/uat-testing) | `c0fd926` | MIT |
| `customer-research` | discover | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/tree/b9ba399dd88b082b926e261e8ccfb843d20aa066/skills/customer-research) | `b9ba399` | MIT |
| `competitor-profiling` | discover | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/tree/b9ba399dd88b082b926e261e8ccfb843d20aa066/skills/competitor-profiling) | `b9ba399` | MIT |
| `pricing` | discover | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/tree/b9ba399dd88b082b926e261e8ccfb843d20aa066/skills/pricing) | `b9ba399` | MIT |
| `product-marketing` | discover | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/tree/b9ba399dd88b082b926e261e8ccfb843d20aa066/skills/product-marketing) | `b9ba399` | MIT |
| `mom-test` | discover | [wondelai/skills](https://github.com/wondelai/skills/tree/c172996495bed0fcd26896a9416b2093fd7073f0/mom-test) | `c172996` | MIT |
| `jobs-to-be-done` | discover | [wondelai/skills](https://github.com/wondelai/skills/tree/c172996495bed0fcd26896a9416b2093fd7073f0/jobs-to-be-done) | `c172996` | MIT |
| `monetizing-innovation` | discover | [wondelai/skills](https://github.com/wondelai/skills/tree/c172996495bed0fcd26896a9416b2093fd7073f0/monetizing-innovation) | `c172996` | MIT |
| `lean-analytics` | discover | [wondelai/skills](https://github.com/wondelai/skills/tree/c172996495bed0fcd26896a9416b2093fd7073f0/lean-analytics) | `c172996` | MIT |
| `blue-ocean-strategy` | discover | [wondelai/skills](https://github.com/wondelai/skills/tree/c172996495bed0fcd26896a9416b2093fd7073f0/blue-ocean-strategy) | `c172996` | MIT |
| `obviously-awesome` | discover | [wondelai/skills](https://github.com/wondelai/skills/tree/c172996495bed0fcd26896a9416b2093fd7073f0/obviously-awesome) | `c172996` | MIT |
| `business-plan` | discover | [inbharatai/claude-skills](https://github.com/inbharatai/claude-skills/tree/02077f8b2c05946a71fa087dee6d614c0b4e4e0d/skills/business-plan) | `02077f8` | MIT |
| `market-researcher` | discover | [inbharatai/claude-skills](https://github.com/inbharatai/claude-skills/tree/02077f8b2c05946a71fa087dee6d614c0b4e4e0d/skills/market-researcher) | `02077f8` | MIT |
| `brand-guidelines` | design | [inbharatai/claude-skills](https://github.com/inbharatai/claude-skills/tree/02077f8b2c05946a71fa087dee6d614c0b4e4e0d/skills/brand-guidelines) | `02077f8` | MIT |
| `software-architecture` | architect | [thangchung/agent-engineering-experiment](https://github.com/thangchung/agent-engineering-experiment/tree/2f0b7a161566755e325c5e3ceb094327aed7217c/foundry-local-agent-fx/.github/skills/software-architecture) | `2f0b7a1` | MIT |
