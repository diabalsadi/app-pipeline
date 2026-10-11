---
name: business
description: Stage 1 of the app pipeline. Interviews a non-technical founder about their app idea and writes the product's business documentation with the OP method (op-business-documentation) - a product profile, a feature list, and one group of D1 Concept, D2 Features List, D3 Journeys and Registries files per feature - for approval. Use when someone wants to start a new app or website idea, says "I have an idea for an app", or runs /business.
---

# Stage 1: Business

Turn the founder's idea into the product's business documentation, written to the OP standard, and get it approved. Everything after this stage refers back to these documents. Follow the shared rules in the `pipeline-core` skill: environment, state file, approval gate, and how to talk to the founder.

This stage replaces the earlier business plan and requirements stages. The standard itself is the `op-business-documentation` skill: load it and follow it for the profile, the feature division, the file groups, the IDs and the definition of done. This file only says how to run it inside the pipeline.

## Outputs (in `docs/01-business/`)

The folder layout of section 4 of the standard: `<Product> Business Documentation/`, with `00 Shared/` and one numbered folder per feature, each holding D1, D2, D3 (Word) and Registries (Excel). Also keep `docs/01-interview-notes.md`, in the founder's own words, so documents can quote them.

## Steps

### 1. Start the project

- If no state file exists, ask for a working name and create it with `business` set to `in_progress`.
- If `business` is already `approved`, say so and ask whether the founder wants to revise the documents. A revision sends every later stage to `needs_reapproval`.

### 2. Interview, then the product profile

Ask one question at a time, in plain words, with a recommendation where there is a choice. The founder is not a documentation expert, so you propose and they confirm. Cover, in this order:

1. The problem, the customer and how they cope today. Ask about past behaviour, not opinions about the idea (`mom-test` if installed).
2. What the first version must do, and what it will not do (the Phase 1 line).
3. Platform (web, mobile or both), languages, countries, rules that add weight (payments, health or financial data, users under 16, location, moderation), and how the app makes money.
4. The product profile from section 1 of the standard: name, ID prefix, definition type, features, owners. For a founder, the owner of every feature is the founder unless they say otherwise. Propose the definition type: most apps are a **Structured surface**; choose **Engine-driven** only when an engine or AI assembles the work per request.

Where the Google Drive upload and Jira parts of the standard are not wanted, say once that the files are delivered as downloads, and move on. Do not ask about them unless the founder raises them.

If you can browse, check the market and competitors for the features you are defining, cite every page, and put what you learn into the D1 sections that need it. Never invent a market size.

### 3. Divide into features

Follow section 2 of the standard. Propose the table (Code · Feature · What it covers · What it does not cover · Owner), ask the founder to confirm it, and only then build files.

### 4. Write the documents

Follow section 10 (Setting up a new product) and section 14 (Output) of the standard, with these pipeline rules:

- Real `.docx` and `.xlsx` files, in the folder layout, with clickable IDs (run `scripts/link_excel.py` over all workbooks as the last step).
- Because the app is built from these files, write user stories with testable Given / When / Then acceptance criteria (or Activities with acceptance, for engine-driven), and list every screen the stories need in the D3 journeys' moments tables.
- Never fill a section with invented content: leave the bracketed placeholder and add an open question with an owner.
- Check the definition of done (section 9) before asking for approval, and fix every defect it finds.

### 5. Approval gate

Set `business` to `awaiting_approval` and run the gate from `pipeline-core`. In the summary, give the product and prefix, the feature table with codes, the number of stories (or intents) in Phase 1, the platform, and the biggest open question. Point the founder to the Shared D1 as the one document to read. Once approved, record the prefix and feature codes in the state file's `product` field and offer to start stage 2 (authenticity).

## Specialist skills

| Step | Skill | Use it for |
| --- | --- | --- |
| Whole stage | `op-business-documentation` | The standard: profile, features, file groups, IDs, review, Jira |
| Interview | `grilling` | Pinning down any decision the draft leaves open, branch by branch. Answer from the documents first; ask the founder only what you cannot. Where it says to ask a whole round at once, the pipeline's one-question-at-a-time rule wins |
| Interview | `mom-test`, `jobs-to-be-done` (extra plugins, if installed) | Better questions about the problem and the job to be done |

The founder can also run `/grill-me` at any point to be interviewed about the documents.
