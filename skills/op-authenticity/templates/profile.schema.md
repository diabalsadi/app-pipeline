# profile.json — the structured data behind the card and the scorecard

Write `00-authenticity/profile.json` in this shape. `scripts/check_gate.py` and `scripts/render_card.py` read it.

```json
{
  "product": "Dawa",
  "client": "Dawa Pharmacies",
  "tagline": "Pharmacy delivery · Amman",
  "date": "2026-10-08",
  "version": "v0.3",
  "status": "Ready for sign-off",
  "feels_like": "The neighbourhood pharmacist who knows your family: calm, warm and precise.",
  "always": ["Arabic-first, right-to-left by design", "Pay with CliQ or cash on delivery", "Sign in with a mobile number", "Prices in JOD with three decimals"],
  "never": ["Imported stock photography", "Month-first date formats", "Health advice without a pharmacist", "Gulf or Egyptian dialect copy"],
  "signature": "A handwritten note from the pharmacist on every order.",
  "packs": ["regions/jordan-levant", "industries/healthcare", "languages/arabic"],
  "dimensions": [
    {"id": "01", "name": "Audience", "lens": "people", "status": "found", "score": 2,
     "summary": "Mothers 28–50 ordering for the family on mid-range Android phones", "evidence": "BRD §2.1"}
  ],
  "generic_diff_resolved": true,
  "signatures": {
    "authenticity_lead": {"name": null, "date": null},
    "client": {"name": null, "date": null}
  }
}
```

Rules:
- `dimensions` must contain all 16 entries, ids "01"–"16", with `lens` one of people / place / purpose / presence.
- `status` per dimension: found / partial / missing (after the interview).
- `score`: integer 0–3.
- `summary`: one line for the card, under about 120 characters (the card trims anything longer).
- Only fill `signatures` when the user reports a real approval with a name and date.
