# Third-party notices

The extra plugins in `toolkit/extras.json` (installed by `app-pipeline-full`) are not copied here; they install straight from their authors' repos at pinned commits.

These skills are copied unchanged from the repositories below, at the pinned commits, with each one's license file kept in its folder. Four have a small frontmatter edit: `apple-design-system` and `software-architecture` have narrower descriptions, `bug-reproduction` has a shorter one that fits claude.ai's 1,024-character limit, so they only run where the pipeline wants them, and `drawio-skill` drops `disable-model-invocation` so the architect stage can call it. Regenerate this file with `python3 scripts/update-toolkit.py`.

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
| `brand-guidelines` | design | [inbharatai/claude-skills](https://github.com/inbharatai/claude-skills/tree/02077f8b2c05946a71fa087dee6d614c0b4e4e0d/skills/brand-guidelines) | `02077f8` | MIT |
| `software-architecture` | architect | [thangchung/agent-engineering-experiment](https://github.com/thangchung/agent-engineering-experiment/tree/2f0b7a161566755e325c5e3ceb094327aed7217c/foundry-local-agent-fx/.github/skills/software-architecture) | `2f0b7a1` | MIT |
| `code-review` | frontend, backend | [mattpocock/skills](https://github.com/mattpocock/skills/tree/b0618bc436ad893b3c5e84e55fba86586d34a404/skills/engineering/code-review) | `b0618bc` | MIT |
| `grill-me` | business | [mattpocock/skills](https://github.com/mattpocock/skills/tree/b0618bc436ad893b3c5e84e55fba86586d34a404/skills/productivity/grill-me) | `b0618bc` | MIT |
| `grilling` | business | [mattpocock/skills](https://github.com/mattpocock/skills/tree/b0618bc436ad893b3c5e84e55fba86586d34a404/skills/productivity/grilling) | `b0618bc` | MIT |
| `code-review-skill` | frontend, backend | [awesome-skills/code-review-skill](https://github.com/awesome-skills/code-review-skill/tree/4850184dfd7765ea7b3c5c4e9b6cf8e0815ee7cb/) | `4850184` | MIT |
| `react-native-expert` | frontend, backend | [jeffallan/claude-skills](https://github.com/jeffallan/claude-skills/tree/1be15d8064f88fc25216442406d40add8fd23b53/skills/react-native-expert) | `1be15d8` | MIT |
| `react-expert` | frontend, backend | [jeffallan/claude-skills](https://github.com/jeffallan/claude-skills/tree/1be15d8064f88fc25216442406d40add8fd23b53/skills/react-expert) | `1be15d8` | MIT |
| `nextjs-developer` | frontend, backend | [jeffallan/claude-skills](https://github.com/jeffallan/claude-skills/tree/1be15d8064f88fc25216442406d40add8fd23b53/skills/nextjs-developer) | `1be15d8` | MIT |
| `typescript-pro` | frontend, backend | [jeffallan/claude-skills](https://github.com/jeffallan/claude-skills/tree/1be15d8064f88fc25216442406d40add8fd23b53/skills/typescript-pro) | `1be15d8` | MIT |
| `postgres-pro` | frontend, backend | [jeffallan/claude-skills](https://github.com/jeffallan/claude-skills/tree/1be15d8064f88fc25216442406d40add8fd23b53/skills/postgres-pro) | `1be15d8` | MIT |
| `code-reviewer` | frontend, backend | [jeffallan/claude-skills](https://github.com/jeffallan/claude-skills/tree/1be15d8064f88fc25216442406d40add8fd23b53/skills/code-reviewer) | `1be15d8` | MIT |
| `security-reviewer` | frontend, backend | [jeffallan/claude-skills](https://github.com/jeffallan/claude-skills/tree/1be15d8064f88fc25216442406d40add8fd23b53/skills/security-reviewer) | `1be15d8` | MIT |
| `secure-code-guardian` | frontend, backend | [jeffallan/claude-skills](https://github.com/jeffallan/claude-skills/tree/1be15d8064f88fc25216442406d40add8fd23b53/skills/secure-code-guardian) | `1be15d8` | MIT |
| `debugging-wizard` | qa | [jeffallan/claude-skills](https://github.com/jeffallan/claude-skills/tree/1be15d8064f88fc25216442406d40add8fd23b53/skills/debugging-wizard) | `1be15d8` | MIT |
| `test-master` | qa | [jeffallan/claude-skills](https://github.com/jeffallan/claude-skills/tree/1be15d8064f88fc25216442406d40add8fd23b53/skills/test-master) | `1be15d8` | MIT |
| `playwright-expert` | qa | [jeffallan/claude-skills](https://github.com/jeffallan/claude-skills/tree/1be15d8064f88fc25216442406d40add8fd23b53/skills/playwright-expert) | `1be15d8` | MIT |
| `quality-assurance` | qa | [jasonkneen/kiro](https://github.com/jasonkneen/kiro/tree/22577b636dc3095f774ace4c846034514d9fa071/skills/quality-assurance) | `22577b6` | MIT |
| `playwright-cli` | qa | [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli/tree/b85c7a736bb473bf55b584e54a09ffa698d6d871/skills/playwright-cli) | `b85c7a7` | Apache-2.0 |
| `qa-project-context` | qa | [petrkindlmann/qa-skills](https://github.com/petrkindlmann/qa-skills/tree/b3bb61bd268b147476252c6ed5a0440c87b97441/skills/qa-project-context) | `b3bb61b` | MIT |
| `test-strategy` | qa | [petrkindlmann/qa-skills](https://github.com/petrkindlmann/qa-skills/tree/b3bb61bd268b147476252c6ed5a0440c87b97441/skills/test-strategy) | `b3bb61b` | MIT |
| `risk-based-testing` | qa | [petrkindlmann/qa-skills](https://github.com/petrkindlmann/qa-skills/tree/b3bb61bd268b147476252c6ed5a0440c87b97441/skills/risk-based-testing) | `b3bb61b` | MIT |
| `playwright-automation` | qa | [petrkindlmann/qa-skills](https://github.com/petrkindlmann/qa-skills/tree/b3bb61bd268b147476252c6ed5a0440c87b97441/skills/playwright-automation) | `b3bb61b` | MIT |
| `mobile-testing` | qa | [petrkindlmann/qa-skills](https://github.com/petrkindlmann/qa-skills/tree/b3bb61bd268b147476252c6ed5a0440c87b97441/skills/mobile-testing) | `b3bb61b` | MIT |
| `accessibility-testing` | qa | [petrkindlmann/qa-skills](https://github.com/petrkindlmann/qa-skills/tree/b3bb61bd268b147476252c6ed5a0440c87b97441/skills/accessibility-testing) | `b3bb61b` | MIT |
| `visual-testing` | qa | [petrkindlmann/qa-skills](https://github.com/petrkindlmann/qa-skills/tree/b3bb61bd268b147476252c6ed5a0440c87b97441/skills/visual-testing) | `b3bb61b` | MIT |
| `security-testing` | qa | [petrkindlmann/qa-skills](https://github.com/petrkindlmann/qa-skills/tree/b3bb61bd268b147476252c6ed5a0440c87b97441/skills/security-testing) | `b3bb61b` | MIT |
| `performance-testing` | qa | [petrkindlmann/qa-skills](https://github.com/petrkindlmann/qa-skills/tree/b3bb61bd268b147476252c6ed5a0440c87b97441/skills/performance-testing) | `b3bb61b` | MIT |
| `payment-testing` | qa | [petrkindlmann/qa-skills](https://github.com/petrkindlmann/qa-skills/tree/b3bb61bd268b147476252c6ed5a0440c87b97441/skills/payment-testing) | `b3bb61b` | MIT |
| `test-data-management` | qa | [petrkindlmann/qa-skills](https://github.com/petrkindlmann/qa-skills/tree/b3bb61bd268b147476252c6ed5a0440c87b97441/skills/test-data-management) | `b3bb61b` | MIT |
| `bug-reproduction` | qa | [petrkindlmann/qa-skills](https://github.com/petrkindlmann/qa-skills/tree/b3bb61bd268b147476252c6ed5a0440c87b97441/skills/bug-reproduction) | `b3bb61b` | MIT |
| `ai-bug-triage` | qa | [petrkindlmann/qa-skills](https://github.com/petrkindlmann/qa-skills/tree/b3bb61bd268b147476252c6ed5a0440c87b97441/skills/ai-bug-triage) | `b3bb61b` | MIT |
