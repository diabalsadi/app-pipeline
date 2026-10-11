# Bug severity

Pick the highest level that fits. When unsure between two levels, pick the higher one and say why in the issue.

| Severity | Label | Meaning | Examples |
| --- | --- | --- | --- |
| Critical | `severity: critical` | Crash, data loss, a security hole, or money handled wrongly | App crashes on launch; payment charged twice; user B can see user A's messages |
| High | `severity: high` | A core feature is broken with no workaround, or a must-have story fails | Cannot sign in on Android; saving a listing silently fails |
| Medium | `severity: medium` | A feature works with a workaround, or fails in an edge case | Search ignores accented letters; the list does not refresh until the app restarts |
| Low | `severity: low` | Cosmetic, wording, or minor layout | Button text cut off on small phones; a typo in an empty state |

## Rules

- Fix in severity order. All bugs are fixed before QA can finish, unless the founder explicitly decides not to fix one.
- A critical bug pauses other work: fix it next.
- An accessibility failure that blocks a user from finishing a task is at least high.
- A failed security check is at least high, and critical if real user data or money is exposed.
