# The generic test (Step 6 — Challenge)

## Why

The biggest risk is not a wrong profile — it is a profile that sounds specific but would produce the same product any AI would make. The generic test makes that visible.

## How

1. Write the product's one-sentence brief with **no** context (e.g. "a booking app for a dental clinic").
2. For each of the 16 dimensions, write in one line what a generic AI would assume from that brief alone. Typical generic defaults:
   - Audience: "busy professionals aged 25–45 on iPhones".
   - Culture: nothing stated; Western defaults (Mon–Fri week, first-name informality).
   - Language: English only, left-to-right.
   - Market: US formats (MM/DD/YYYY, $, imperial units).
   - Ecosystem: card payments via Stripe, email + password sign-in, email support.
   - Trust: "GDPR compliant" as a catch-all.
   - Visual: a single sans-serif font, purple/blue gradient, rounded cards, stock photos of smiling people.
   - Voice: "Get started", "Oops! Something went wrong".
   - Content: "John Doe", "123 Main Street", lorem ipsum.
3. Put the generic line next to the profile's line for each dimension and mark:
   - **Different** — the profile is clearly specific to this product. Nothing to do.
   - **Same → changed** — you made the profile more specific; write the new line.
   - **Same → justified** — it really is the same for a stated reason (e.g. "English only: the client is an international school whose entire staff and parents work in English — confirmed in BRD §2.1").
4. The test is **resolved** when every row is Different, Changed or Justified. Any row left as plain "Same" means rule 4 fails.

## Output

Write `generic-diff.md` from `templates/generic-diff.md`, and set `generic_diff_resolved` in `profile.json`.
