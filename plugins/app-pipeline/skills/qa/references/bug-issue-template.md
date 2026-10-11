# Bug issue template

Write the body to a temporary file and pass it to `gh issue create --body-file`. Labels: `bug` plus one `severity: <level>` label.

Title: what is wrong, and where. For example: "Sign up accepts an email without a domain".

```markdown
**Test case:** TC-001 (run 2, commit `abc1234`)
**Screen:** S03 Sign up
**Story:** US-02
**Severity:** high. [One line on why, using severity.md]
**Platform:** [iOS simulator 18 / Android emulator 15 / Chrome 130 desktop]

## Steps to reproduce
1. …
2. …

## Expected
…

## Actual
…

## Evidence
[A screenshot, a log excerpt, or a recording link]

## Notes
[Anything that narrows the cause, such as "only on Android" or "only after sign-out".]
```
