# Pull request template

## Screen pull request

Title: `S03 Sign up: <one line on what the screen does>`

```markdown
**Screen:** S03 Sign up ([mockup](docs/03-design/screens/S03-sign-up.html))
**Stories:** US-02, US-03
**Founder approval:** approved on [date] after [n] rounds of changes

## What it does
[Two or three sentences in plain language.]

## Acceptance criteria
- [x] US-02 / 1: Given …, when …, then … (`tests/sign-up.test.tsx`)
- [x] US-02 / 2: …

## Code review
- [n] findings, all fixed. [Or list each one with its outcome.]

## Security review
- [n] findings, all fixed. [Or list each one with its outcome.]

## Notes
[New dependencies, migrations, or anything a future change should know.]
```

## Bug-fix pull request (QA stage)

Title: `Fix #<issue>: <one line on the bug>`

```markdown
Fixes #<issue>

**Severity:** [critical | high | medium | low]
**Cause:** [one or two sentences]
**Fix:** [one or two sentences]
**Test:** [the test that failed before this fix and passes now]

## Code review
[results]

## Security review
[results]
```

The `Fixes #<issue>` line makes GitHub close the issue automatically when the pull request is merged into `main`.
