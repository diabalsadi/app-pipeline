# Review checklist

Use this for every screen pull request in the frontend stage, and every bug-fix pull request in QA. Review the diff against `main`, plus any code the diff calls into.

## Standards (code review)

- [ ] Follows every rule in the repo's `CLAUDE.md`.
- [ ] Matches the approved mockup: layout, copy, and states (default, empty, loading, error, success).
- [ ] No hard-coded colours, sizes, or fonts: all come from the theme tokens.
- [ ] Screens stay thin. Data access and business logic live in `src/services/`.
- [ ] Names say what things are. No dead code, commented-out code, or stray `console.log`.
- [ ] Errors are handled and shown to the user in plain words. No promise is left unhandled.
- [ ] Tests cover every acceptance criterion of the screen's stories, and would fail if the feature broke.
- [ ] No needless re-renders or repeated network calls, such as fetching inside a render loop.
- [ ] Accessibility: labels on touchable elements and inputs, a logical focus order, tap targets of at least 44 px, and text contrast of at least 4.5:1.
- [ ] New dependencies are well maintained, needed, and recorded in the pull request.

## Security (security review)

- [ ] **Secrets:** no keys, tokens, or passwords in code, tests, or config. Only public client keys, such as the Supabase anon key, are allowed in the app.
- [ ] **Access control:** every table touched has row level security turned on, with policies that let each role reach only its own data. Test with a second user where it matters.
- [ ] **Authentication:** protected screens and API calls check the session. Sign-out clears local session data.
- [ ] **Input:** all user input is validated on the server or database side as well as in the form. No string-built SQL, and no `dangerouslySetInnerHTML` with user content.
- [ ] **Data exposure:** responses and logs include no more personal data than the screen needs. No personal data in analytics events.
- [ ] **Storage on the device:** tokens are stored with secure storage (`expo-secure-store`), not plain async storage.
- [ ] **Links and redirects:** deep links and redirects are checked against an allow list.
- [ ] **Payments:** amounts are set on the server, never trusted from the client. Webhooks verify their signature.
- [ ] **Files:** uploads are checked for type and size, and stored with access rules.
- [ ] **Dependencies:** `npm audit` shows no high or critical advisories that this change introduced.

## Recording results

For each finding, record its severity (blocking or not), the file and line, what was wrong, and what was done about it. Blocking findings are fixed before merge. A non-blocking finding is either fixed or noted in the pull request with the reason it was left.
