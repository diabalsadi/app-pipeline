# Style guide and tokens

## `style-guide.md`

```markdown
# [App name]: style guide

Direction [A, B, or C], chosen by the founder on [date]. Design persona: [one line].

## Principles
1. [principle from the persona]
2. [principle]
3. [principle]

## Typography
| Role | Font | Size / line height | Weight | Use |
| --- | --- | --- | --- | --- |
| Display | [font] | 40 / 44 | 700 | Screen titles |
| Body | [font] | 16 / 24 | 400 | Paragraphs and lists |

## Colour
| Token | Value | Role | Contrast on background |
| --- | --- | --- | --- |
| color.bg | #F4EFE6 | Page background | n/a |
| color.text | #1C1A17 | Main text | 15.2:1 |
| color.accent | #C2410C | Primary actions only | 4.8:1 |

## Signature element
[What it is, where it appears, and where it never appears.]

## Components
For each of these, note its look and its states (default, pressed, disabled, focus, error): button (primary and secondary), text input, list row, card (if used), navigation, empty state, toast or banner, modal or sheet.

## Voice
- Buttons: [examples]
- Empty states: [example]
- Errors: [example]

## Allowed exceptions to the anti-generic rules
- [rule]: [reason], or "none"
```

## `tokens.json`

Use this structure. The build stage maps it into the app's theme, so keep the names stable once the founder approves the design.

```json
{
  "color": {
    "bg": "#F4EFE6",
    "surface": "#FFFFFF",
    "text": "#1C1A17",
    "textMuted": "#6B645A",
    "accent": "#C2410C",
    "accentText": "#FFFFFF",
    "success": "#3F7D4E",
    "warning": "#B7791F",
    "danger": "#B42318",
    "border": "#DDD5C7"
  },
  "font": {
    "display": { "family": "Fraunces", "fallback": "Georgia, serif" },
    "body": { "family": "IBM Plex Sans", "fallback": "system-ui, sans-serif" }
  },
  "fontSize": { "xs": 12, "sm": 14, "md": 16, "lg": 20, "xl": 28, "xxl": 40 },
  "lineHeight": { "tight": 1.1, "normal": 1.5 },
  "space": { "1": 4, "2": 8, "3": 12, "4": 16, "6": 24, "8": 32, "12": 48 },
  "radius": { "sm": 4, "md": 8, "pill": 999 },
  "shadow": { "none": "none", "raised": "0 1px 2px rgba(28,26,23,0.12)" },
  "motion": { "fast": 120, "normal": 200, "easing": "cubic-bezier(0.2, 0, 0, 1)" }
}
```

The values above only show the format. Each product gets its own values from its chosen direction.
