# Scoring rubric and pass rules

Use this in Step 7. Score honestly: a lower true score is more useful than a flattering one, because the gate exists to show where the product would otherwise go generic.

## The 0–3 scale

| Score | Name | Meaning | Typical evidence |
| --- | --- | --- | --- |
| 0 | Generic | Nothing specific. The statement could describe any product. | "Modern, user-friendly design." "Users are customers." |
| 1 | Assumed | A reasoned guess, not yet backed by anything citable. | Your inference from indirect signals; "I think so" from the user; a pack default not confirmed for this client. |
| 2 | Evidenced | Backed by a source you can point to. | A specific statement in the client's business files; a sourced web reference; an OP Library pack entry that applies directly and has been checked; a concrete answer from the client or founder about their own business. |
| 3 | Validated | Confirmed by real users or real usage data. | User interviews, surveys, usability tests, analytics, support tickets, or the client's own user research included in the files. |

### Scoring guidance

- **Business files are evidence (2)** when they state something specific about the client's own users, market or rules. Vague aspirations in the files ("world-class experience") are 0.
- **The user's answer in chat** is 2 when it is a specific fact about their own client or business ("all payments go through CliQ"), and 1 when it is a guess ("probably mostly Android?").
- **A library pack** supports a 2 only when the pack entry clearly applies to this product. Mark which facts came from the pack.
- **3 needs real users.** Say exactly what the validation was (e.g. "5 receptionist interviews, March 2026"). Do not give 3 for stakeholder opinion.
- When unsure between two scores, choose the lower and say what would lift it.

## The pass rules

All five must be true for the profile to be approved. Show each rule with ✅ or ❌ and one line of explanation.

1. **No dimension at 0.** Nothing is left generic.
2. **Average of all 16 is 2.0 or higher.** Compute to one decimal place.
3. **Critical four at 2 or higher:** 01 Audience, 03 Culture & Values, 06 Language & Script, 12 Trust & Compliance.
4. **Generic diff resolved:** every overlap with the "any-product" version has been changed or justified (see `generic-test.md`).
5. **Two signatures:** the OP Authenticity Lead and the founder / client, each with a name and a date.

Rules 1–4 can be computed. Rule 5 is only met when the user tells you both approvals happened. You never sign or approve on anyone's behalf.

## Status

| Status | When |
| --- | --- |
| **Not yet** | Any of rules 1–4 fails. |
| **Ready for sign-off** | Rules 1–4 pass; rule 5 pending. |
| **Approved v1.0** | All five pass. Later approved changes become v1.1, v1.2… |

## When the gate is "Not yet"

List the failing rules, then for each weak dimension give the **fastest way to lift it**:

- Missing fact → one specific question for the client (who should answer it).
- Assumed → one source to find, or one document to request.
- Want to reach 3 → which real users to talk to (3–5 is enough) and what to ask them.

Then return to Step 3 (gaps) or Step 4 (evidence). Do not loosen the rules to pass.

## Radar

The scorecard shows the 16 scores as a radar (spokes 01–16, rings 1–3, the pass line at 2 drawn dashed). `scripts/check_gate.py` produces it as `radar.svg`; if scripts cannot run, describe the shape in words (which lens is strongest and weakest).
