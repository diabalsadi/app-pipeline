---
name: architect
description: Stage 4 of the app pipeline. Chooses the code and cloud architecture for the approved product (React Native by default for mobile), explains each choice in plain language as a short decision record, and estimates the monthly cloud cost at launch, growth, and scale using current published prices. Use after designs are approved, or when someone runs /architect.
---

# Stage 4: Architect

Choose how the app will be built and hosted, and what it will cost to run, in terms the founder can approve. Follow the shared rules in the `pipeline-core` skill.

Requires `design` to be `approved`. Reads the business plan (constraints, budget, hard requirements), the requirements (platform, users, data rules), and `docs/03-design/tokens.json`.

## Steps

### 1. Start from the defaults

Use the default stack in [references/default-stack.md](references/default-stack.md). Mobile apps are cross-platform React Native unless the founder stated a hard requirement for another stack. Depart from a default only for a reason you can point to in the business plan or requirements, such as a hard requirement, a data rule, offline needs, or scale.

### 2. Decide

Cover each decision below and write a short decision record for each one, using [references/decision-record-template.md](references/decision-record-template.md). Skip a decision only when it does not apply, for example payments in a free app.

1. Platform and app framework
2. Backend and database
3. Sign-in
4. File and image storage
5. Hosting and app delivery (web hosting, App Store and Google Play builds)
6. Payments, if the app takes money
7. Email and push notifications
8. Error monitoring and product analytics, enough to measure the success metrics
9. Third-party services the requirements need, such as maps, search, or AI

Each record gives 2 or 3 real options, the trade-offs in plain language, and a recommendation. Use the `engineering:architecture` skill if it is available. Use `software-architecture` for the code structure principles that the setup and build stages will follow (library-first, domain separate from infrastructure, small modules), translating its .NET examples to the chosen stack.

Also write a one-page overview in `docs/04-architecture.md`: a diagram of the parts and what talks to what (draw it with the `drawio-skill` as `docs/04-architecture.drawio`, export a PNG for the founder if draw.io is installed, and fall back to a Mermaid diagram otherwise), the list of decisions with links to their records, and the data model (main entities and how they relate, in plain words).

### 3. Estimate the cost

Write `docs/04-cost-estimate.md` from [references/cost-estimate-template.md](references/cost-estimate-template.md):

- Take the three usage levels from the requirements: users at launch, at 12 months, and a "scale" level of 10 times the 12-month figure.
- For every paid service, open its current pricing page and work out the monthly cost at each level. Link each price to its pricing page and record the date you checked it.
- Never price from memory. If you cannot open a pricing page, mark the figure as "estimate, not checked" and say so to the founder.
- Include one-off and yearly costs: the Apple Developer Program, the Google Play registration fee, and a domain name.
- State the assumptions behind each figure, such as storage per user, emails per user per month, or requests per user per day.

### 4. Approval gate

Set `architect` to `awaiting_approval` and run the gate from `pipeline-core`. In the summary, cover:

- the stack in one sentence,
- the monthly cost at launch and at 12 months, plus the one-off costs,
- anything that went against the defaults, with the reason,
- any decision you need the founder to make. A decision is theirs when the options differ in cost or in what users see.

Once the founder approves, offer to start stage 5 (setup).
