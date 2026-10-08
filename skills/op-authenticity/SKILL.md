---
name: op-authenticity
description: Optimum Partners' mandatory Stage 0 before any product is designed or built. Reads the client's business files and requirements, maps them onto the OP Authenticity Compass (4 lenses, 16 dimensions), asks only about the gaps, and produces a scored Authenticity Profile, a one-page Authenticity Card and a Design Brief that must pass the OP pass rules before design starts. Use this skill whenever someone at OP starts a new product, uploads business files, BRDs or requirements and wants to begin designing, says "authenticate", "authenticity", "Stage 0", "profile" or "Authenticity Card", or asks to design screens, write UI copy or build a product without an approved AUTHENTICITY.md yet. Also use it to guard later work ("check this against the profile").
---

# OP Authenticity — Stage 0

AI tools make every product look and sound the same. This skill makes sure each Optimum Partners product is defined by its real people, place, purpose and presence **before** anyone designs or builds it. The rule the team works by: **no profile, no pixels; no profile, no code.**

The person using this skill is usually **not technical**. They already have business files (requirements, BRDs, proposals, decks, notes) and want to start designing in Claude. Your job is to do the heavy lifting: read their files, work out what is already known, ask only for what is missing, and hand back a profile they can get signed.

## How to talk to the user

- Plain words. No jargon; if a term is unavoidable, explain it in one short sentence.
- Keep chat messages short. Long material goes into the output files.
- When you ask something, ask **one question at a time** and say in a few words why it matters.
- "I don't know" is always an acceptable answer. Never make the user feel they failed; record it and move on.
- Never invent facts about the client, their users or their market. A guess is labelled as a guess (score 1).

## The compass (summary)

Four lenses, sixteen dimensions. Full definitions, what to look for in business files, and the gap question for each are in `references/compass.md` — read it before Step 1.

| Lens | Question | Dimensions |
| --- | --- | --- |
| PEOPLE | Who is it for? | 01 Audience · 02 Persona · 03 Culture & Values · 04 Accessibility & Inclusion |
| PLACE | Where does it live? | 05 Market & Region · 06 Language & Script · 07 Context of Use · 08 Local Ecosystem |
| PURPOSE | What does it stand for? | 09 Industry & Domain · 10 Brand DNA · 11 Business Model · 12 Trust & Compliance |
| PRESENCE | How does it look, sound and behave? | 13 Visual Identity · 14 Interaction Patterns · 15 Voice & Tone · 16 Content & Imagery |

## The process

Follow these steps in order. Tell the user at the start, in three short lines, what is about to happen (read files → ask about gaps → draft and score the profile → they get it signed).

### Step 0 — Get the inputs

You need the business files and the product name. If no files are attached, ask for them (any format: Word, PDF, slides, spreadsheets, notes, links). If the user truly has none, you can still run the process, but every dimension starts as Missing and the interview will be longer — say so.

### Step 1 — Capture: read the files and build the coverage map

Read **every** file fully before asking anything. For each of the 16 dimensions, extract what the files say, with a short quote or paraphrase and where it came from (file name + section or page). Then mark each dimension:

- **Found** — the files answer it specifically enough to act on.
- **Partial** — something is there but it is vague, generic or incomplete.
- **Missing** — nothing usable.

Business files are often written from the client's point of view ("the system shall…"). Read between the lines: a requirement for "SMS OTP login" tells you about the local ecosystem; "reports in Arabic and English" tells you about language; a list of user roles tells you about audience. Specific beats vague: "users" is Partial, "front-desk receptionists aged 25–45 using shared desktop PCs" is Found.

Show the user the coverage map (use `templates/coverage-map.md`) — a compact view, not a wall of text — and say how many dimensions are Found, Partial and Missing.

### Step 2 — Match: pick packs from the OP Library

Read `library/README.md`, then open only the packs that fit the product's **region**, **industry** and **language** (for example `regions/jordan-levant.md` + `industries/healthcare.md` + `languages/arabic.md`). Tell the user in one line which packs you are using and ask them to correct you if one does not fit. Packs give you local signals, do's and don'ts, tokens and checks; use them to enrich the profile, to sharpen your gap questions, and as evidence.

Pack facts about laws, prices and services can change. If you can search the web, verify any pack fact you rely on for Trust & Compliance or Local Ecosystem; if you cannot, say which facts come from the library and its review date.

### Step 3 — Fill the gaps

Ask about **Partial and Missing dimensions only** — never re-ask what the files already answer. Use the gap questions in `references/compass.md`, adapted to the product. Order:

1. The **critical four** first (they block the gate): 01 Audience, 03 Culture & Values, 06 Language & Script, 12 Trust & Compliance.
2. Then the rest, People → Place → Purpose → Presence.

One question per message. If more than about six questions are needed, offer the user a choice: answer one at a time, or get the full list in one message and reply in one go. If the user says they are busy or cannot answer now, do not stall: record each open question, treat the dimension as Assumed (score 1) using your best reasoned guess from the files and packs, label it clearly, and continue.

### Step 4 — Ground: add real evidence

Where you can browse, look for real evidence for weak dimensions: local competitors and the apps users already trust, local payment and sign-in habits, the regulations that apply, cultural references. Cite every source with a link. Never present research from memory as fact. If you cannot browse, rely on the files, the user's answers and the packs, and say so.

### Step 5 — Define: write the Authenticity Profile

Create the profile folder `00-authenticity/` using the templates:

| File | Template | What it holds |
| --- | --- | --- |
| `AUTHENTICITY.md` | `templates/authenticity-profile.md` | All 16 dimensions: what is true, rules (always / never), evidence, score |
| `coverage-map.md` | `templates/coverage-map.md` | Found / Partial / Missing per dimension, with sources, before and after the interview |
| `authenticity-card.html` | `assets/card-template.html` via `scripts/render_card.py` | The one-page Authenticity Card |
| `scorecard.md` | `templates/scorecard.md` | Scores, radar, pass-rule results, sign-off block |
| `generic-diff.md` | `templates/generic-diff.md` | The generic test (Step 6) |
| `design-brief.md` | `templates/design-brief.md` | The hand-off into design: personas, palette direction, type, voice, do / don't, signature element |
| `open-questions.md` | — | Anything Assumed or unanswered, who can answer it, and which dimension it would lift |
| `profile.json` | `templates/profile.schema.md` | The structured data behind the card and the scorecard |

The card is meant to be read in one glance, so keep each dimension's `summary` in `profile.json` under about 120 characters; the detail belongs in `AUTHENTICITY.md`.

Write rules that a designer or builder can act on. "Arabic-first, right-to-left by design; English as a second language toggle" is useful. "Culturally appropriate" is not.

### Step 6 — Challenge: the generic test

Read `references/generic-test.md`. Write, in one line per dimension, the version of this product that a generic AI would produce from a one-sentence brief with no context. Compare it with the profile. Every place where the two are the same must be **changed** (make the profile more specific) or **justified** (it is the same for a real, stated reason). The test is resolved only when no unexplained overlap remains.

### Step 7 — Score and run the gate

Score each dimension 0–3 using `references/rubric.md`:

- **0 Generic** — could describe any product. **1 Assumed** — a reasoned guess, no evidence. **2 Evidenced** — backed by a citable source. **3 Validated** — confirmed by real users.

Then apply the **pass rules** exactly (details in `references/rubric.md`):

1. No dimension at 0.
2. Average of all 16 is 2.0 or higher.
3. The critical four (01 Audience, 03 Culture & Values, 06 Language & Script, 12 Trust & Compliance) are each 2 or higher.
4. The generic diff is resolved.
5. Two signatures: the OP Authenticity Lead and the founder / client.

Run `python scripts/check_gate.py 00-authenticity/profile.json` to compute rules 1–4 and render the radar, then `python scripts/render_card.py 00-authenticity/profile.json 00-authenticity/authenticity-card.html`. If scripts cannot run, compute the rules by hand and write the card as Markdown instead.

**You never sign or approve the profile yourself.** Rule 5 can only be met when the user tells you both people approved, with their names and the date. Until then the status is one of:

- **Not yet** — a rule in 1–4 fails. Say which dimensions to lift and the fastest way to lift each (a question for the client, a source to find, three real users to ask). At the end of `open-questions.md`, write a short, ready-to-send message to the client that asks only the questions needed to pass, grouped by who should answer them — so the user can unblock the gate with one email. Then loop back to Step 3 or 4 when answers arrive.
- **Ready for sign-off** — rules 1–4 pass. Produce the approval summary (`templates/approval-summary.md`) for the user to send to the Authenticity Lead and the client.
- **Approved v1.0** — only after the user reports both approvals. Record names and dates in `profile.json` and `scorecard.md`, set the version, and re-render the card.

### Step 8 — Hand off

Give the user the folder (zip it if you can) and tell them, in plain words, what to do next:

1. Save the folder in the product's shared folder.
2. Add `AUTHENTICITY.md` and `design-brief.md` to the Claude Project's files, so every later chat follows them.
3. When the profile is approved, start design. Every design and build request is now checked against the profile.

Close with the question: "Do you want me to change anything before you send it for sign-off?"

## After approval: guard mode

When an approved `AUTHENTICITY.md` is available (attached or in the Project files) and the user asks to design, write copy, build a screen, or "check this against the profile", read `references/guard.md` and apply it. Follow the profile's rules in everything you produce, and when asked to check work, answer **Pass**, **Drift** (what does not fit, which dimension, how to fix it) or **Profile change needed** (the profile itself is out of date; it must be re-approved by the same two people).

If someone asks to design or build and there is **no** profile, explain briefly that OP's Stage 0 comes first, offer to start it with their business files, and do not skip it — even for a quick demo. A partial profile scored honestly is fine; no profile is not.

## Quality bar

- Every Found dimension cites where it came from. Every score of 2 or 3 points to its evidence.
- Gap questions only for Partial or Missing dimensions.
- Rules are specific enough to design from (formats, languages, payment methods, tone examples, things to avoid).
- The pass rules are shown one by one with a clear verdict, and the status never says "Approved" without two named signatures.
