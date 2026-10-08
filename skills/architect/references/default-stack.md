# Default stack

These are the starting points. Each one can be changed by a hard requirement from the founder, or by a reason in the requirements that you write down in a decision record.

| Area | Default | Common alternative | Switch when |
| --- | --- | --- | --- |
| Mobile app | React Native with Expo, in TypeScript, using Expo Router | Native Swift and Kotlin | The founder requires it, or the app needs deep device features that Expo cannot reach |
| Web app | Next.js, in TypeScript | Expo web (React Native Web) | The product is mobile-first and its web version is a light companion |
| Mobile and web | One Expo app for iPhone, Android, and web | An Expo app plus a Next.js site in one repo | The web side needs search-engine visibility or a very different layout |
| Backend and database | Supabase (Postgres, sign-in, storage, edge functions) | Firebase; a custom API on a managed host | The data is document-shaped and real-time (Firebase), or the logic is too heavy for edge functions |
| Sign-in | Supabase Auth: email link, Apple, and Google | Clerk; Firebase Auth | The founder needs organisations and teams out of the box (Clerk) |
| File storage | Supabase Storage | Cloudflare R2; Amazon S3 | Heavy media or high download volume |
| Web hosting | Vercel | Netlify; Cloudflare Pages | The cost at the scale level is clearly lower elsewhere |
| Mobile builds | Expo EAS Build and Submit | Local builds | The founder wants no build service subscription |
| Payments, physical goods and services | Stripe | Lemon Squeezy; Paddle | The founder wants a merchant of record to handle sales tax |
| Payments, digital goods in a mobile app | In-app purchases through RevenueCat | Store purchases implemented directly | App Store and Google Play rules require in-app purchase for digital goods |
| Email | Resend | Postmark | The app sends mostly transactional email and needs top delivery rates (Postmark) |
| Push notifications | Expo Notifications | OneSignal | Marketing campaigns and audience segments are needed |
| Error monitoring | Sentry | Expo's own crash reports | Never: some form of crash reporting is always on |
| Product analytics | PostHog | Firebase Analytics | The founder already uses Google's tools |

## Fixed engineering defaults

These apply to every project and are carried into the setup stage:

- TypeScript in strict mode.
- One repo per app, with `main` protected so changes only arrive through pull requests.
- Automated checks on every pull request: lint, type check, unit tests, dependency audit, and secret scanning.
- Secrets live in the hosting provider's secret store and are never committed. A `.env.example` lists their names.
- Design tokens from `docs/03-design/tokens.json` are loaded into a single theme module, and no colour or size is hard-coded in screens.
- Accessibility target: WCAG 2.1 AA.
