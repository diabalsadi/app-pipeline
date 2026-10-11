# Cost estimate template

Copy this structure into `docs/04-cost-estimate.md`.

```markdown
# [App name]: running cost estimate

Prices checked on [date]. All amounts are in [currency] per month unless marked otherwise.

## Summary
| Usage level | Users | Monthly cost |
| --- | --- | --- |
| Launch | [n] | [amount] |
| 12 months | [n] | [amount] |
| Scale (10 times the 12-month level) | [n] | [amount] |

**One-off and yearly costs:** Apple Developer Program [amount per year], Google Play registration [one-off amount], domain [amount per year].

## By service
| Service | What it is for | Plan at launch | Launch | 12 months | Scale | Pricing page |
| --- | --- | --- | --- | --- | --- | --- |
| [Supabase] | [database, sign-in, storage] | [plan name] | [amount] | [amount] | [amount] | [link] |

## Assumptions
| Assumption | Value | Why |
| --- | --- | --- |
| Monthly active users / total users | [ratio] | [reason] |
| Storage per user | [MB] | [reason] |
| Emails per user per month | [n] | [reason] |
| Push notifications per user per month | [n] | [reason] |

## What makes the cost jump
- [The first threshold where a plan upgrade is needed, and its cost]

## Not included
- [For example, the founder's time, marketing, legal advice, or payment processing fees taken per transaction]
```

## Rules

- Every price links to the provider's pricing page, checked on the date at the top.
- Prices you could not check are marked "estimate, not checked".
- Fees charged per transaction, such as card fees or app store commission, go in "Not included". Explain them in one line each, because they scale with revenue, not with users.
