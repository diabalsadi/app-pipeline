# Test plan template

Copy into `docs/08-qa/test-plan.md`.

```markdown
# [App name]: test plan

Based on the business documents approved on [date]. Platforms under test: [iPhone (iOS [version]) simulator, Android [version] emulator, Chrome desktop].

## Summary
| Area | Cases | Automated | Manual |
| --- | --- | --- | --- |
| Acceptance criteria | [n] | [n] | [n] |
| Journeys | [n] | [n] | [n] |
| Accessibility | [n] | [n] | [n] |
| Performance | [n] | [n] | [n] |
| Security | [n] | [n] | [n] |
| Edge cases | [n] | [n] | [n] |

## Acceptance criteria
| ID | Story / criterion | Screen | Steps | Expected result | How |
| --- | --- | --- | --- | --- | --- |
| TC-001 | US-02 / 1 | S03 | 1. Open Sign up 2. Leave email empty 3. Tap Continue | "Enter your email" appears under the field | Automated (`.maestro/sign-up.yaml`) |

## Journeys
| ID | Journey | Steps | Expected result | How |
| --- | --- | --- | --- | --- |
| TC-101 | New user to first [main task] | … | … | Automated |

## Accessibility
| ID | Check | Expected | How |
| --- | --- | --- | --- |
| TC-201 | Screen reader reads every control on S01 to S0n | Every control has a meaningful label | Manual |
| TC-202 | Text contrast on every screen | At least 4.5:1 | Automated or manual |

## Performance
| ID | Check | Target | How |
| --- | --- | --- | --- |
| TC-301 | Time from launch to first usable screen | Under [2] seconds on a mid-range phone | Manual |

## Security
| ID | Check | Expected | How |
| --- | --- | --- | --- |
| TC-401 | User B cannot read or change user A's data | Request refused | Automated |

## Edge cases
| ID | Case | Expected | How |
| --- | --- | --- | --- |
| TC-501 | Offline on [main screen] | Clear offline message; no crash; retry works | Manual |
| TC-502 | Very long name or text | Wraps or truncates cleanly | Manual |
```
