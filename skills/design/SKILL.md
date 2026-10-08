---
name: design
description: Stage 3 of the app pipeline. Writes a user persona and a design persona, offers distinct style directions, then designs every screen from the approved requirements as clickable HTML mockups with a style guide and design tokens, avoiding generic AI-looking UI. Use after requirements are approved, or when someone runs /design.
---

# Stage 3: Design

Design every screen on the approved screen list in one distinctive style the founder chose. Follow the shared rules in the `pipeline-core` skill.

Requires `validate` to be `approved`. Reads `docs/01-business-plan.md` and `docs/02-requirements.md`.

## Outputs (in `docs/03-design/`)

| File | What it is |
| --- | --- |
| `personas.md` | The user persona and the design persona |
| `directions/A.html`, `B.html`, `C.html` | 2 or 3 style directions, each a sample screen |
| `style-guide.md` | The chosen direction written down as rules |
| `tokens.json` | Colours, type, spacing, radii, and shadows as design tokens |
| `screens/S01-<name>.html` … | One mockup per screen, with its states |
| `index.html` | A clickable hub that links every screen in order |

## Steps

### 1. Personas

Write `personas.md` using [references/personas.md](references/personas.md). The user persona comes from the business plan. The design persona is the designer you act as for the rest of this stage, and every visual decision should trace back to it.

### 2. Style directions

Create 2 or 3 directions that are clearly different from each other, not three shades of one idea. Each direction is:

- a design persona variant (one line),
- a font pairing, a palette of 5 to 7 colours, and one signature element,
- the product's most important screen (the main task from the business plan) rendered as a self-contained HTML page at phone width (390 px) for mobile, or desktop width for web.

Every direction must pass the rules in [references/anti-generic-rules.md](references/anti-generic-rules.md). Use real copy from the business plan, never placeholder text.

Show the founder the directions side by side. For each one, give one line on how it feels and who it suits. Mark your recommendation and ask them to pick one or mix them ("A's colours with B's fonts").

### 3. Style guide and tokens

Turn the chosen direction into `style-guide.md` and `tokens.json`, using the format in [references/style-guide-template.md](references/style-guide-template.md). The tokens are the single source of truth: the build stage reads them, so every colour and size in the mockups must come from them.

### 4. Screen mockups

For each screen on the list, in order:

- Build `screens/S01-<name>.html` as a self-contained HTML page that uses only values from `tokens.json`.
- Show its default state, plus each state that applies to it: empty, loading, error, and success. Put them on the same page as labelled variants.
- Use realistic data and copy, written in the brand's voice.
- Link buttons and navigation to the right next screen, so `index.html` works as a clickable prototype.
- For mobile, respect safe areas and 44 px minimum tap targets, and design for one-handed use where it matters.

### 5. Review pass

Before showing the founder, review every screen and fix what you find:

- **Design critique** (use the `design:design-critique` skill if available): hierarchy, consistency with the style guide, and whether the main action is obvious.
- **UX copy** (use `design:ux-copy` if available): buttons, empty states, and error messages are specific and in the brand voice.
- **Accessibility** (use `design:accessibility-review` if available): colour contrast at least 4.5:1 for text, visible focus states, labels on every input, and nothing that relies on colour alone.
- **Anti-generic check:** run the full checklist in `anti-generic-rules.md` again on the finished screens.

### 6. Approval gate

Set `design` to `awaiting_approval` and run the gate from `pipeline-core`. Send the founder `index.html` (or the published prototype), and ask them to click through it on the device they expect users to use. Collect change requests per screen, apply them, and ask again. Once the founder approves, offer to start stage 4 (architect).

## In a Claude Project

Publish the directions and the clickable prototype as artifacts so the founder can open them in the browser. Give them `style-guide.md` and `tokens.json` as files to add to the Project.
