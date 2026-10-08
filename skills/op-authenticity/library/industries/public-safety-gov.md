# Industry pack · Government & public safety (gov services, police SaaS)
Owner: Library Curator · Version 1.0 · Last reviewed: 2026-10 · Verify legal facts before relying on them.

## Signals
- Two audiences: officers/staff (operational, time-critical, often mobile, in vehicles or on foot) and administrators (configuration, oversight, reports).
- Hierarchy, ranks and permissions are central; who can see what is a core requirement, not a detail.
- Data is highly sensitive (identities, incidents, evidence); auditability and chain of custody matter.
- Jurisdiction defines the rules: national data-sovereignty rules in the Gulf; in the US, criminal justice information falls under the FBI CJIS Security Policy.
- Formal, neutral tone; accessibility is often mandatory for public-facing services.

## Do
- Model ranks, units and permission levels exactly as the client's organisation works; make visibility rules explicit.
- Log every access and change (audit trail); show "last updated by / when".
- Design for interruption and speed in the field: large controls, minimal steps, offline capability where operations need it.
- State the jurisdiction and the rules that apply (data hosting location, retention, records law).
- For public services: national digital identity sign-in where available; bilingual where required.

## Don't
- Playful tone, gamification or decorative visuals in operational screens.
- Show sensitive personal data to roles that don't need it.
- Assume cloud region or hosting location without checking jurisdiction rules.

## References
- Jordan: Sanad (government digital services). Saudi Arabia: Absher, Nafath. UAE: UAE Pass, TAMM, DubaiNow.
- United States: FBI CJIS Security Policy for criminal justice information; state public-records laws.
- Accessibility: WCAG 2.1 AA (often mandated for public services).

## Tokens
Roles and ranks: from client org chart · audit trail: required · data class: highly sensitive · hosting: per jurisdiction.

## Checks
- Every role sees only what the visibility rules allow (test each rank).
- Audit log records views and edits of sensitive records.
- Field flows usable one-handed and offline where operations require.
