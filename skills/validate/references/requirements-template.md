# Requirements template

Copy this structure into `docs/02-requirements.md`.

```markdown
# [App name]: requirements

Based on the business plan approved on [date].

## Summary
- Platform: [web, mobile, or both]
- First version: [n] stories across [n] screens
- Users at launch: [n], at 12 months: [n]

## User roles
| Role | Who they are | What they can do |
| --- | --- | --- |
| Guest | [description] | [summary] |

## User stories

### US-01: [short title]
- **Story:** As a [role], I want to [action] so that [benefit].
- **Feature:** F1
- **Priority:** Must
- **Screens:** S03, S04
- **Acceptance criteria:**
  1. Given [context], when [action], then [observable result].
  2. Given [context], when [action], then [observable result].

## Screen list
| ID | Screen | Purpose | Stories | Priority |
| --- | --- | --- | --- | --- |
| S01 | Welcome | [one line] | US-01 | Must |

## Non-functional needs
| Need | Requirement |
| --- | --- |
| Platform | [web, mobile (iPhone and Android), or both] |
| Languages | [list] |
| Accessibility | WCAG 2.1 AA |
| Data and privacy | [what personal data is stored, and which rules apply] |
| Offline | [what must work without a connection, or "not needed"] |
| Performance | [for example, "main screen usable within 2 seconds on 4G"] |

## Out of scope for the first version
- [deferred stories or features]

## Open issues
| # | Problem found | Question for the founder | Recommendation | Resolution |
| --- | --- | --- | --- | --- |
| 1 | [gap or contradiction] | [plain question] | [answer you suggest] | [filled after asking] |
```
