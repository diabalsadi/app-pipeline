# Language pack · Arabic
Owner: Library Curator · Version 1.0 · Last reviewed: 2026-10

## Signals
- Modern Standard Arabic (MSA, الفصحى) is the written standard for formal UI, documents and government. Dialects (Levantine, Gulf, Egyptian, Maghrebi) are spoken and used in marketing and chat.
- Many users read Arabic but type in English or Arabizi; professionals often expect technical terms in English.
- Arabic is right-to-left; numbers, Latin words and code run left-to-right inside RTL text (bidirectional text).
- Arabic text is often 20–30% longer or shorter than English, and taller (ascenders/descenders and diacritics).
- Names: given name + father's name + grandfather's name + family name is common; "Abu/Umm + child's name" is a respectful form of address.

## Do
- Design RTL first, not as a flipped afterthought: mirror navigation, back arrows, progress, carousels, chevrons and alignment.
- Do NOT mirror: logos, media play buttons, clocks, numbers, phone numbers, Latin brand names, checkmarks in some icon sets (test each).
- Choose fonts with real Arabic support and matching Latin, e.g. IBM Plex Sans Arabic, Noto Sans Arabic / Noto Kufi Arabic, Cairo, Tajawal, Almarai, Readex Pro. Pair the Arabic and Latin fonts deliberately.
- Increase line height for Arabic (about 1.6–1.8) and avoid all-caps-style letter spacing (Arabic letters must connect; never add letter-spacing).
- Pick one digit style per product (Western 0–9 or Arabic-Indic ٠–٩) and use it consistently.
- Use a dialect/register decision from the profile: MSA in UI, dialect only where the brand voice says so and for the right country.
- Store names in Arabic and Latin where documents need both; allow long names and four-part names.

## Don't
- Machine-translated microcopy without native review.
- Letter-spaced or italic Arabic; fonts without Arabic glyphs (browsers fall back to mismatched system fonts).
- Mixing dialects of different countries in one product.
- Truncating Arabic text mid-word in fixed-width components.

## Tokens
dir rtl · line-height 1.7 · letter-spacing 0 for Arabic · digits: western (default) or arabic-indic (state it) · font stack example: "IBM Plex Sans Arabic", "IBM Plex Sans", "Noto Sans Arabic", Tahoma, sans-serif.

## Checks
- RTL mirror test on every screen (navigation, icons, charts, progress).
- Long Arabic strings and four-part names don't break layouts.
- Mixed Arabic/English/number strings render in the correct order (e.g. "طلب رقم 1045").
- Native-speaker review of all copy before sign-off.
