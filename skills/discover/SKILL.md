---
name: discover
description: Stage 1 of the app pipeline. Interviews a non-technical founder about their app idea, researches the market and competitors, and writes a business plan for approval. Use when someone wants to start a new app or website idea, says "I have an idea for an app", or runs /discover.
---

# Stage 1: Discover

Turn the founder's idea into a business plan they approve. Follow the shared rules in the `pipeline-core` skill: environment, state file, approval gate, and how to talk to the founder.

## Specialist skills

| Step | Skill | Use it for |
| --- | --- | --- |
| Interview | `mom-test` | Asking about past behaviour, not opinions of the idea, and spotting compliments that carry no commitment |
| Interview | `jobs-to-be-done` | Framing the problem as the job the customer is trying to get done |
| Interview | `customer-research` | Turning the interview notes into needs, pains, and the founder's ideal customer |
| Market research | `competitor-profiling` | Building each competitor's profile from its website and reviews |
| How we win | `obviously-awesome`, `blue-ocean-strategy` | Positioning against the competitors, and finding what to drop, raise, or create |
| Revenue model | `monetizing-innovation`, `pricing` | Checking willingness to pay, choosing the pricing model, and setting tiers |
| Success metrics | `lean-analytics` | Picking the one metric that matters for this kind of business, with sensible targets |
| Business plan | `business-plan`, `market-researcher` | General prompts for plan sections and research synthesis. The template in this skill still sets the structure |
| Positioning summary | `product-marketing` | Writing the value proposition and messaging. Put the result in the business plan, not in a separate context file |

## Steps

### 1. Start the project

- If no state file exists, ask for a working name for the app (a placeholder is fine) and create the state file with `discover` set to `in_progress`.
- If `discover` is already `approved`, say so and ask whether the founder wants to revise the plan. A revision sends later stages to `needs_reapproval`.

### 2. Interview

Use the question bank in [references/interview-guide.md](references/interview-guide.md). Ask one question at a time and follow up whenever an answer is vague. Stop when every "must know" item has a clear answer; the "nice to know" items are optional.

Keep running notes in `docs/01-interview-notes.md`, using the founder's own words, so the plan can quote them.

### 3. Market research

Research with web search and by opening the pages you cite. A search snippet is not a source.

- **Competitors:** find 3 to 6 direct or close competitors. For each, record what it does, its price, its platforms, and what its reviews praise and complain about. App store and review-site pages are good for the complaints.
- **Market:** who the customers are and roughly how many, using published figures with links. Do not invent a market size. If none is published, describe the audience in words and say no figure was found.
- **Rules that apply:** flag anything that adds legal or technical weight, such as taking payments, health or financial data, users under 16, location tracking, or user-generated content that needs moderation.
- **Differentiation:** state in one or two sentences how this app wins against the competitors.

If you cannot browse the web, tell the founder, research nothing from memory, and leave the competitor table for them to fill or confirm.

### 4. Write the business plan

Write `docs/01-business-plan.md` from the template in [references/business-plan-template.md](references/business-plan-template.md). Keep it to what a founder would read in 10 minutes. The first-version feature list is the most important section, because every later stage builds from it, so keep it small.

### 5. Approval gate

Set `discover` to `awaiting_approval` and run the gate from `pipeline-core`. In the summary, cover the problem, the customer, the first-version features, and the biggest risk. Once the founder approves, offer to start stage 2 (validate).
