---
name: validate
description: Stage 2 of the app pipeline. Turns an approved business plan into validated requirements (user roles, user stories with acceptance criteria, a screen list, platform and data needs), finds gaps and contradictions, and asks the founder to resolve them. Use after the business plan is approved, or when someone runs /validate.
---

# Stage 2: Validate

Turn the approved business plan into requirements with no gaps. The screen list produced here drives design, build, and QA. Follow the shared rules in the `pipeline-core` skill.

Requires the `discover` stage to be `approved`, and reads `docs/01-business-plan.md`.

## Steps

### 1. Draft the requirements

Write `docs/02-requirements.md` from the template in [references/requirements-template.md](references/requirements-template.md):

- **User roles:** everyone who uses the app, such as a guest, a signed-in user, or an admin.
- **User stories:** one per thing a role needs to do, written as "As a [role], I want to [action] so that [benefit]". Give each one an ID (US-01) and tie it to a feature (F1).
- **Acceptance criteria:** 2 to 5 per story, each in Given / When / Then form, concrete enough to test. QA turns each criterion into a test case later.
- **Screen list:** every screen with an ID (S01), its purpose, the stories it serves, and its priority. Include the screens founders tend to forget: welcome, sign up, sign in, password reset, settings, and an error or offline state.
- **Non-functional needs:** platform (web, mobile, or both), languages, expected users at launch and at 12 months, data and privacy rules, accessibility (WCAG 2.1 AA by default), and offline needs.

### 2. Validate

Run every check in [references/validation-checklist.md](references/validation-checklist.md). Record each problem in the document's "Open issues" table, with a plain-language question for the founder and your recommended answer.

### 3. Resolve with the founder

Go through the open issues one at a time, most important first. For each one, ask the question, give your recommendation, and apply the answer. When the founder says "use your recommendation" for the rest, apply them all and list what you chose.

### 4. Prioritise

Mark each story **Must**, **Should**, **Could**, or **Later**. The first version is the Must stories, plus the Should stories the founder explicitly keeps. If the Must list has grown past the business plan's first-version features, point that out and ask whether to cut it back or accept the larger scope.

### 5. Update the state and run the gate

- Set `platform` in the state file, and fill `screens` from the screen list with every screen at `not_started`.
- Set `validate` to `awaiting_approval` and run the gate from `pipeline-core`. In the summary, give the number of stories, the screen list by name, the platform, and any scope change since the business plan.
- Once the founder approves, offer to start stage 3 (design).
