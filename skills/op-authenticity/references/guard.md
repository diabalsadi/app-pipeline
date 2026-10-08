# Guard mode — after the profile exists

Use this when an approved (or ready-for-sign-off) `AUTHENTICITY.md` is available and the user asks you to design, write copy, build a screen, or check a piece of work.

## While producing work

Treat the profile as the brief. Before producing a design, copy or a screen:
- Re-read the profile's ALWAYS / NEVER rules and the Design Brief.
- Use the profile's language, direction (RTL/LTR), formats (dates, currency, phone, addresses), payment and sign-in methods, tone examples and real content.
- Use fonts that support every script in the profile.
- Use real-looking local names, places and data from dimension 16 — never "John Doe" or placeholder text.

After producing it, run the check below on your own output and fix any Drift before showing it.

## The check

Answer one verdict:

- **Pass** — it fits the profile. Say so in one line.
- **Drift** — something does not fit. For each issue: what it is, which dimension (number and name) it breaks, and the fix. Example: "Drift · 05 Market & Region: price shown as $12.99; profile requires JOD with three decimals → '3.250 JD'."
- **Profile change needed** — the work is right but the profile is out of date (e.g. the client added a new country). Say what should change in the profile and that it needs re-approval by the same two people before work continues.

## Checklist by stage

| Stage | Question to answer |
| --- | --- |
| Discover / research | Is the research looking at the right market, people and region from the profile? |
| Requirements | Do the requirements include the local flows the profile demands (local payment, sign-in, formats, language, consent)? |
| Design | Could this screen belong to any other product or market? If yes, it goes back. Do fonts support the scripts? Do colours avoid meanings the profile forbids? |
| Architecture | Are the local services and data rules from the profile respected (payments, SMS/OTP, maps, hosting location)? |
| Set up | Is the profile saved with the project and wired into its rules and design tokens? |
| Build | Does every screen pass: copy in the right language and tone, formats, imagery, direction, tokens? |
| QA | Did walkthroughs as the profile's personas pass, and did locale tests pass (RTL mirroring, long Arabic text, dates, currency, phone numbers)? |

## No profile?

If someone asks for design or build work and there is no profile, say briefly that OP's Stage 0 comes first and offer to run it with their business files now.
