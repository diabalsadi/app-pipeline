---
name: design
description: Stage 3 of the app pipeline. Builds the screen list from the business documentation, writes a user persona and a design persona from the authenticity profile, offers distinct style directions, then designs every screen as clickable HTML mockups with a style guide and design tokens, using the frontend skills and avoiding generic AI-looking UI. Use after authenticity is approved, or when someone runs /design.
---

# Stage 3: Design

Design every screen of the product in one distinctive style the founder chose. Follow the shared rules in the `pipeline-core` skill.

Requires `authenticity` to be `approved`. Reads `docs/01-business/` (stories, journeys and entities), and `docs/02-authenticity/AUTHENTICITY.md` and `design-brief.md`.

## Refer back to the business documents and the authenticity profile

- The screen list is made here, from the business documents: every moment in the D3 journeys that needs a screen, and every story that needs one, with the business IDs it serves. Nothing is designed that no story or journey asks for, and no Phase 1 story is left without a screen. Include the screens founders tend to forget: welcome, sign up, sign in, password reset, settings, and an error or offline state.
- The personas start from the authenticity `design-brief.md` and the business users in the Shared D1. Do not invent a second audience.
- Language, direction (right-to-left or left-to-right), formats, palette direction, type, voice and the signature element come from the authenticity profile. Every screen answers the guard question: could this screen belong to any other product or market? If yes, it goes back.
- Mockup data uses the entity names and state values from the registries, and the real-looking local content from the profile.

## Outputs (in `docs/03-design/`)

| File | What it is |
| --- | --- |
| `screen-list.md` | Every screen with an ID (S01), its purpose, the business IDs it serves, its priority, and the platform versions it needs |
| `personas.md` | The user persona and the design persona |
| `directions/A.html`, `B.html`, `C.html` | 2 or 3 style directions, each a sample screen |
| `style-guide.md` | The chosen direction written down as rules |
| `tokens.json` | Colours, type, spacing, radii, and shadows as design tokens |
| `screens/S01-<name>.html` … | One mockup per screen, with its states |
| `index.html` | A clickable hub that links every screen in order |

## Specialist skills

The frontend skills are required for this stage, not optional: load `frontend-design` and `ui-ux-pro-max` before step 2 and use them for every direction and every mockup, and run `refactoring-ui` and `web-typography` on the style guide. They are bundled with the plugin. If one is missing (for example in a Claude Project where it was not uploaded), say so to the founder before carrying on without it.

| Step | Skill | Use it for |
| --- | --- | --- |
| Directions and mockups | `frontend-design` (required) | Committing to a bold, specific aesthetic direction for each option, and keeping every mockup as distinctive as its direction |
| Directions and mockups | `ui-ux-pro-max` (required) | Searching its catalogue of styles, palettes, and font pairings for starting points, and its React Native guidelines. Treat results as raw material that must still pass the anti-generic rules |
| Directions | `apple-design-system` | Only when the founder picks an Apple-style direction |
| Style guide | `brand-guidelines` | Writing the brand section: logo use, colour, type, and tone of voice |
| Style guide | `refactoring-ui`, `web-typography` (required) | Hierarchy, spacing, colour, and type scales |
| Mockups | `ios-hig-design` | iPhone conventions (navigation, safe areas, tap targets) for mobile apps |
| Mockups | `microinteractions` | Feedback, transitions, and small moments of delight on key actions |
| Mockups | `threejs-skills` (extra plugin) | Only when a web app needs a 3D scene, such as a product viewer |
| Review | `impeccable` (extra plugin) | Its critique, audit, and polish commands on each mockup, if installed |
| Review | `ux-heuristics` | A usability pass against Nielsen's heuristics, alongside the critique and accessibility checks |

When a specialist skill and `anti-generic-rules.md` disagree, the anti-generic rules win.

## Steps

### 1. Screen list and personas

First write `screen-list.md` from the business documents, as above, and note which screens need a phone version, a web version, or both, from the platform in the business profile.

Then write `personas.md` using [references/personas.md](references/personas.md). The user persona comes from the business documents and the authenticity brief. The design persona is the designer you act as for the rest of this stage, and every visual decision should trace back to it.

### 2. Style directions

Create 2 or 3 directions that are clearly different from each other, not three shades of one idea. Each direction is:

- a design persona variant (one line),
- a font pairing, a palette of 5 to 7 colours, and one signature element,
- the product's most important screen (the main task from the Shared D1 and D3) rendered as a self-contained HTML page. When the platform is "both", render it at phone width (390 px) and at desktop width. When the platform is mobile or web only, render just that one.

Every direction must pass the rules in [references/anti-generic-rules.md](references/anti-generic-rules.md). Use real copy from the business documents, never placeholder text.

Tell the founder up front that each direction shows one screen only, and that after they pick, every screen on the list (and both phone and web versions) follows in that style. Then show the directions side by side. For each one, give one line on how it feels and who it suits. Mark your recommendation and ask them to pick one or mix them ("A's colours with B's fonts").

### 3. Style guide and tokens

Turn the chosen direction into `style-guide.md` and `tokens.json`, using the format in [references/style-guide-template.md](references/style-guide-template.md). The tokens are the single source of truth: the build stage reads them, so every colour and size in the mockups must come from them.

### 4. Screen mockups

For each screen on the list, in order:

- Build `screens/S01-<name>.html` as a self-contained HTML page that uses only values from `tokens.json`.
- Show its default state, plus each state that applies to it: empty, loading, error, and success. Put them on the same page as labelled variants.
- Use realistic data and copy, written in the brand's voice.
- Link buttons and navigation to the right next screen, so `index.html` works as a clickable prototype.
- When the platform is "both", build every screen at phone and desktop width (one page, two labelled layouts), not only the one the directions used.
- For mobile, respect safe areas and 44 px minimum tap targets, and design for one-handed use where it matters. Where a dense visual (a heat map, a chart, a long grid) makes some items too small to tap, design a list or grouped fallback for them instead of shrinking the target.

### 5. Review pass

Before showing the founder, review every screen and fix what you find:

- **Design critique** (use the `design:design-critique` skill if available): hierarchy, consistency with the style guide, and whether the main action is obvious.
- **UX copy** (use `design:ux-copy` if available): buttons, empty states, and error messages are specific and in the brand voice.
- **Accessibility** (use `design:accessibility-review` if available): colour contrast at least 4.5:1 for text, visible focus states, labels on every input, and nothing that relies on colour alone.
- **Anti-generic check:** run the full checklist in `anti-generic-rules.md` again on the finished screens.

### 6. Approval gate

Set `design` to `awaiting_approval`, fill `screens` in the state file from `screen-list.md` (every screen at `not_started`), and run the gate from `pipeline-core`. In the summary, say that every screen traces to a business ID and report the authenticity check (Pass, Drift or Profile change needed). Send the founder `index.html` (or the published prototype), and ask them to click through it on the device they expect users to use. Collect change requests per screen, apply them, and ask again. Once the founder approves, offer to start stage 4 (architect).

## In a Claude Project

Publish the directions and the clickable prototype as artifacts so the founder can open them in the browser. Give them `style-guide.md` and `tokens.json` as files to add to the Project.
