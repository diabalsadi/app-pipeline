# Scaffolding by stack

Use the official generator at its current version, then check the generated `package.json` scripts against the list at the end. Prefer the framework's own defaults over custom configuration.

## Mobile (default): React Native with Expo

```bash
npx create-expo-app@latest <app-name>
cd <app-name>
npx expo install expo-font
npm install --save-dev jest-expo jest @testing-library/react-native @types/jest
```

- The default template uses Expo Router (file-based navigation) and TypeScript. Turn on `"strict": true` in `tsconfig.json`.
- Run `npx expo lint` once to set up ESLint, and use it as the `lint` script.
- Set Jest's `preset` to `jest-expo` in `package.json`.
- For end-to-end tests in QA, plan on [Maestro](https://maestro.mobile.dev) flows in `.maestro/`.

## Web: Next.js

```bash
npx create-next-app@latest <app-name> --typescript --eslint --app --src-dir --import-alias "@/*"
cd <app-name>
npm install --save-dev vitest @testing-library/react @testing-library/jest-dom jsdom @playwright/test
```

- Use Vitest for unit and component tests, and Playwright for end-to-end tests in QA.

## Mobile and web from one codebase

Use the Expo setup above. Expo Router renders the same screens on the web through React Native Web. Check each screen at desktop width as well as phone width during the build.

## Folder layout

```
app/ (or src/app/)   screens and routes, one file per screen on the screen list
src/components/      shared building blocks (Button, TextField, ListRow, EmptyState)
src/theme/           tokens.ts generated from tokens.json, plus helpers
src/services/        backend calls (Supabase client, payments, analytics)
src/lib/             small pure helpers
tests/ or __tests__/ unit and component tests, named after what they test
docs/                business documents, authenticity, design, architecture, frontend, backend, QA
pipeline/state.json  pipeline state
```

## Theme from tokens

Write `src/theme/tokens.ts` as a typed copy of `docs/03-design/tokens.json` (`export const tokens = { ... } as const`), and load the fonts it names with `expo-font` or `next/font`. Screens import values from the theme and never hard-code a colour, size, or font. If `tokens.json` changes, regenerate `tokens.ts` in the same pull request.

## Backend

If the architecture chose Supabase, create `src/services/supabase.ts` with the client, reading the URL and the public anon key from environment variables (`EXPO_PUBLIC_SUPABASE_URL` and `EXPO_PUBLIC_SUPABASE_ANON_KEY` for Expo). Database tables are created through migration files in `supabase/migrations/`, with row level security turned on for every table from the start.

## Scripts every project must have

| Script | Does |
| --- | --- |
| `npm run lint` | Lint the whole project |
| `npm run typecheck` | `tsc --noEmit` |
| `npm test` | Unit and component tests, non-interactive |
| `npm start` | Start the app for the founder to try |
