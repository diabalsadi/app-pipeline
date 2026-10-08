---
name: op-business-documentation
description: "Use when a team defines, writes, reviews or queries its product's business documentation with the OP method: one file group per feature (D1/D2/D3 Word + Registries Excel), optional Google Drive upload, clickable IDs, Jira."
---

# OP Business Documentation

A standard any product team can use to write its business documentation so that every business fact has one home, one ID and one owner. A product is documented **feature by feature**: each feature (a capability area) gets its own group of four files, plus one Shared group for the product as a whole. Use this skill to:

1. Set up a new product and divide it into features.
2. Write and extend definitions (rows, stories, rules, journeys) in the right feature.
3. Add a feature to an existing product.
4. Review a product or one feature against the standard.
5. Answer questions from a finished set.
6. Turn definitions into Jira epics and stories.

The standard is in this skill. The product content is not: always read the team's live files.

Examples below use a fictional product, **Billing (prefix BIL)**, with features Invoicing (INV), Refunds (REF) and Customer accounts (ACC). Replace them with the team's own.

## 1. Start: the product profile

Before any work, establish the product profile. Read it from the Shared workbook's Read me manifest if one exists; otherwise ask the team once:

- Product name and **ID prefix** (2 to 4 capitals, unique in the organisation, e.g. BIL).
- **Definition type**: Engine-driven, Service or Surface (section 4). If unsure, help the team choose with the descriptions in section 4.
- **The feature list** (section 2): each feature's name, **feature code** (2 to 4 capitals, unique in the product, e.g. INV) and owner.
- **Where the files live** and which system is the master (e.g. a Google Drive folder). Only files there count; copies elsewhere are superseded.
- Current version and status of each file group.
- Phase names (default: Current = Phase 1 · Next · Later · Never).
- Product-specific constraints (UI copy rules, "no AI in Phase 1", design system). Treat them as fixed.
- **Where finished files go**: download only, or also a Google Drive folder (section 14). Once chosen, reuse it for the rest of the work.

List the source location fresh at the start of each task. If a file can't be opened, say so and stop. Never answer from memory.

The master is edited by its owner. Edit it only when the owner explicitly asks in the current conversation: show the planned rows first, then report exactly what changed.

## 2. Dividing a product into features

A **feature** is a capability area: a group of related things users can do, owned by one person, that can be planned and delivered on its own (e.g. Invoicing, Refunds, Customer accounts). A product usually has 4 to 10.

**How to divide**
1. Start from what the team already has: the product's capability map, an existing Features List, epics, or the menu of the product. Group related capabilities by the business goal they serve and the people who use them.
2. Propose the list to the team as a table: Code · Feature · What it covers · What it does not cover · Owner. Each feature must be distinct (no capability in two features) and the list must cover the whole product scope.
3. **If it is not clear how to divide, ask; never guess.** Ask when: a capability could belong to two features; a feature would have only one or two stories or intents; a feature would cover most of the product; the team uses names you can't map; or there is no source to divide from. Ask one short question with your proposed split as the first option.
4. The owner confirms the list before any file is built. Record it in the Shared D1 (capability map) and the Shared workbook's Read me (feature register: Code · Feature · Folder · Owner · Phase · Status).

**The Shared group (code CORE)** is always present. It holds:
- The product-level view: Shared D1 is the product concept (problem, vision, users, scope, the feature map); Shared D2 is the product feature index (one row per feature with phase and priority, linking to each feature's D2); Shared D3 holds journeys that cross features.
- Rows used by more than one feature: shared entities (e.g. Customer), cross-cutting rules, and permissions that more than one feature needs.

**Who owns a row**
- A row lives in exactly one workbook: the feature whose behaviour it defines. Other features cite its ID and never copy it.
- An entity, rule or permission that two or more features need from the start lives in Shared.
- If a row later turns out to be needed elsewhere, it stays where it is and the other feature links to it. It is never moved or duplicated, because the feature code is part of its ID.
- A feature that only reads another feature's entity cites it; it never redefines its states.

**Changing the division** (splitting, merging or renaming a feature) is a change to the Shared D1 and the feature register, approved by the owner. Existing IDs never change; new rows go to the new feature, and the old feature's D1 names where its scope went.

## 3. Principles

1. **One fact, one place.** Every fact has one home; other documents cite its ID and never restate it.
2. **The workbook defines behaviour.** The feature's D1, D2 and D3 explain and cite workbook IDs. If a document and a workbook disagree, the workbook wins: flag the conflict and name both sources.
3. **Define building blocks, not paths** (engine-driven products). Sequences appear only as examples, in scenarios.
4. **Deterministic rules.** States, gates, invariants and authority are fixed and testable.
5. **Humans keep authority.** Every consequential decision is named, owned by a role type and recorded. AI may prepare, validate, explain and recommend.
6. **Type every rule:** Fixed, Governed (value set by the customer's configuration) or Contextual (evaluated per request).
7. **Business owns content; the technical team owns format.** Columns are agreed once, then fixed, and are the same in every feature.
8. **Each workbook holds only its own rows.**
9. **Prototypes and mock-ups are not sources.**

## 4. Definition types and file groups

| Type | What it is | Example | Documents | Workbook |
|---|---|---|---|---|
| **Engine-driven product** | Business logic that an engine or orchestrator assembles into work per request | An intake-to-order workspace | D1 Concept · D2 Features List · D3 Experience Journeys | Registries: core tabs + Intents · Activities · Knowledge · Scenarios |
| **Shared service** | A capability other products use and contribute to through a contract | Notifications, task inbox | D1 (with contribution model) · D2 · D3 Experience Journeys | Registries: core tabs + Intents · Actions · Contract · Contributors · Scenarios |
| **Structured surface** | A fixed, form-based product with set steps | An admin console | D1 · D2 (mapped to user stories) · D3 Workflows | Registries: core tabs + User stories (Scenarios optional) |

The type is set for the product; every feature uses the same documents and tabs.

### One file group per feature

```
<Product> Business Documentation/
  00 Shared/
    <Product> Shared D1 Product Concept
    <Product> Shared D2 Features List
    <Product> Shared D3 Experience Journeys      (or D3 Workflows)
    <Product> Shared Registries
  01 <Feature>/
    <Product> <Feature> D1 Feature Concept
    <Product> <Feature> D2 Features List
    <Product> <Feature> D3 Experience Journeys   (or D3 Workflows)
    <Product> <Feature> Registries
  02 <Feature>/
    ...
```

Folders are numbered in the order of the feature register. Example: `01 Invoicing/Billing Invoicing Registries`.

### The documents

| Doc | Shared group | Feature group | Structure |
|---|---|---|---|
| **D1 Concept** | Product concept: why the product exists, for whom, the feature map | Feature concept: why this feature exists, what it covers and doesn't, for whom | 1 Problem · 2 Domain principles · 3 Vision and differentiation · 4 Users and value · 5 Scope (Phase 1, Next, Later, Never) · 6 Capability map (Shared: features with codes and folders; feature: areas to intent or story IDs) · 7 Governance model · 8 Boundaries and integrations (feature: what it uses from Shared and other features, by ID) · 9 Success measures · 10 Assumptions and open decisions · 11 Document set |
| **D2 Features List** | Feature index: one row per feature (Code · Feature · Phase · Priority · Owner · Dependencies · link to its D2) | What ships in which phase for this feature | How to read · Phase 1 intents or stories · one table per capability: Feature · IDs · Phase · Priority · Dependencies |
| **D3 Journeys / Workflows** | Journeys that cross features | Journeys inside this feature | Journey index · per journey: goal, trigger, entry points; moments table (Moment · What they see · What they decide · IDs); friction to avoid; success signal · Appendix: UI patterns |
| **Registries workbook** | Shared rows and the feature register | This feature's rows | Section 5 |

Rules for the set:
- Every cover carries title, product, feature (or Shared), purpose, version, date, owner, status, and states that it follows the OP Business Documentation standard.
- D1 never names a state or field. Journeys describe what people see and decide, never system logic. Scenarios are examples, never specifications.
- Each file group has its own version and status; a feature can be Approved while another is Draft.

## 5. The Registries workbook

Every feature workbook and the Shared workbook have the same tabs and columns.

### Format rules
- Headers in row 1 of every tab. Notes about a tab go in the Read me tab guide.
- ID first column; Row status (Draft · In review · Approved · Retired) last.
- Rows are never deleted: a retired row keeps its ID and names its replacement.
- Column names are identical across all workbooks. A column that does not apply holds "—" and is never dropped.
- Reference columns hold IDs only, separated by " · ". They may cite IDs from Shared or any other feature.
- Every ID carries the product prefix and the feature code of the workbook it lives in.
- A core tab with no rows is kept and marked None in the tab guide.
- One row per building block; related details fold into the row that owns them.

### Core tabs (every workbook)

| Tab | One row is | Columns |
|---|---|---|
| **Read me** | — | Manifest (type · ID prefix · feature code and name · standard version · schema version) · version, date, owner · purpose · tab guide · how to edit · links to the Shared workbook and the feature's documents · open questions (ID · Topic · Question · Owner · Status). The Shared Read me adds the feature register (Code · Feature · Folder · Owner · Phase · Status) |
| **Entities & States** | An entity | Entity ID · Name · What it is · What it is not · Created when · Relationships · State dimensions and values · Key attributes · Fixed rules |
| **Transitions** | A state change | Transition ID · State dimension · From · To · Trigger · Guard · Performed by · Emits |
| **Rules** | An invariant, gate or rule | Rule ID · Statement (When … then …) · Type · Applies to · Parameters · Effect · Override |
| **Permissions** | A permission | Permission ID · Business object · Action · Scope · Data scope values · Used by · Separation of duties · Basic · Requires |
| **Attention** | A task | ID · Name · Type · Source · Trigger · Recipient · Actions · Quick actions · Blocking · Clears when · External-facing |
| **Notifications** | A notification | Notification ID · Name · Kind · Source · Trigger · Recipient · Settings section · Default channels · Always on · Links to task · External-facing · Description |

### Extension tabs

| Type | Tab | Columns |
|---|---|---|
| Engine-driven | **Intents** | Intent ID · Name · Example phrasings · Entry points · Who can start it · Required context · Goal state · Other endings · Activities that may be used · Direct UI shortcut |
| Engine-driven | **Activities** | Activity ID · Name · Purpose · Performer · Preconditions · Required when · Knowledge used · Outputs & state effects · Gates satisfied · Human decision · Emits · AI boundary · UI pattern · Tags · Acceptance (Given/When/Then) |
| Engine-driven | **Knowledge** | KI ID · Name · Kind · Used by · Criticality · Tier · Source priority · Provided by · Fallback template · Placeholders · Legal review · Country variants · Before adoption |
| All (optional for Surface) | **Scenarios** | Scenario ID · Name · Intent · What it proves · Given · Expected assembly · Gates & decisions · Attention · Outcome · Variations · Design coverage |
| Service | **Intents** | As above, with "Actions used" |
| Service | **Actions** | Action ID · Action · Behaviour · Changes owner · Changes source record · Permission · AI can run it · Recorded |
| Service | **Contract** | Field ID · Field · Purpose · Supplied by · Matching Attention column · Required |
| Service | **Contributors** | Contributor ID · Product · Where its items are defined · Phase · Status |
| Surface | **User stories** | Story ID · Area · As a · I want to · So that · Acceptance criteria (Given / when / then) · Rules · Permissions · Phase |

### Value lists

| Column | Allowed values |
|---|---|
| State dimension kind | Set by transitions · Additive set (attention conditions) · Derived |
| Performer / Performed by | System · AI · Human (role type) · External platform; combined where shared (e.g. AI + Requester) |
| Rule Type | Fixed (invariant) · Fixed · Governed · Contextual |
| Rule Effect | Always holds · Block · Condition · Flag · Insert activity |
| KI Kind | Policy · Taxonomy · Template · Threshold/parameter · Customer fact · Connection |
| KI Criticality | Blocking · Blocking with fallback · Enhancing only |
| KI Tier | 0 onboarding · 1 activation · 2 just-in-time · 3 enrichment |
| Task type | Action · Review · Dependency/Impact · Exception · Waiting · Incomplete · Expiration/Lifecycle |
| Notification kind | Information · Alert · Reminder · Confirmation |
| Phase | Current · Next · Later · Never |

### Writing rules by tab
- **Entities & States.** Keep lifecycle, progress, attention conditions and contextual eligibility as separate state dimensions. Anything that depends on the request is derived, never stored. Every terminal state says what a restart requires. Later-phase values go in brackets: [Next phase: Suspended]. An entity used by several features lives in Shared; a feature adds its own state dimension to a shared entity only with the Shared owner's approval, as a row in the feature workbook that cites the entity.
- **Transitions.** Every row has trigger, guard and performer. A decision-triggered transition names the decision and value (e.g. BIL-INV-DEC-02 = Approve).
- **Activities.** Verb-first, outcome-based. Never name a "next" activity; order comes from preconditions, gates and rules. Merge activities that never run apart. Write each decision in full at first use (options · decided by · what AI must never do · separation of duties), then "see first use".
- **Rules.** Write gates against activity tags, not single activities. Every Governed rule names in Parameters the knowledge items it reads. No consequential state change without a decision or a Fixed rule allowing automation.
- **Knowledge.** Provided by is a role type. Inferred values stay unconfirmed until a person accepts them. Templates are used only after an authorised owner adopts them; legal-text templates need legal review.
- **User stories.** One story per user goal. Acceptance criteria in Given / when / then, testable, one outcome each. Rules and Permissions columns hold IDs only.
- **Scenarios.** Keep the set small: each happy path, each blocking gate, each state-changing exception, once. Expected assembly in completion order; "+" joins parallel steps. Scenarios that cross features live in Shared.
- **Attention.** Tasks only (section 6). Task state is Open · Completed · Dismissed; the source record's state is never copied into a task. Quick actions are those finishable in two steps (choose, confirm) with no form.
- **Permissions.** One row per grantable action. Every human decision, performer and recipient maps to a permission; definitions name permissions, never roles. Basic marks permissions every role includes. Requires lists prerequisite permissions. State whether missing permissions hide or disable the action.
- **Notifications.** Each feature lists its own; the Shared D2 links to every feature's Notifications tab. A notification about a task names it in Links to task.

## 6. Task or notification

| Question | If yes |
|---|---|
| Does a named person need to perform or record an action? | **Task**, plus a notification linking to it if people should be told |
| Should someone only be informed? | **Notification** only |
| Is it system or AI work in progress? | **Neither**: show it as status on the record |

A notification never holds the action. Reminders and escalations are notifications about an existing task.

## 7. IDs and integrity

- Format `<PREFIX>-<FEATURE>-<TYPE>-<NN>`, e.g. BIL-INV-RULE-07, BIL-REF-US-12, BIL-CORE-ENT-CUS. The feature code says which workbook the ID lives in.
- Type codes: ENT entity · `<entity>-S` state dimension · `<entity>-T` transition · `<entity>-I` invariant · INT intent · ACT activity · DEC decision · GATE / RULE · KI knowledge item · TPL template · ATT task · NTF notification · SCN scenario · US user story · PERM permission · UIP UI pattern · J journey · Q open question. Entity-scoped IDs keep the entity code after the feature code: BIL-INV-INVC-T06.
- Numbering is per feature and per type: each workbook starts at 01.
- IDs are never reused or renumbered, including on retired rows, and never change feature.
- Never invent an ID. New rows get the next free number in the owning feature's tab, marked NEW (proposed) until the owner adds them.
- A reference to an undefined ID, a knowledge item used by nothing, or a decision in no activity is a defect. So is the same ID in two workbooks.
- Changing a state or gate lists everything that cites it, in every feature.
- **Every reference to an ID is a link** to the row or section that defines it, across features, in every file and in chat answers and Jira tickets (section 15).

## 8. UI patterns

UX builds one component per pattern and prototypes the scenarios, not every path. The pattern set is product-wide and lives in the Shared D3 appendix; products add their own after UIP-09 (Pattern · Used for · Must show · Actions · Design reference · Status).

| Pattern | Used for | Must show |
|---|---|---|
| UIP-01 Check | System/AI evaluation | Result, what was checked, why, next action |
| UIP-02 Collect | Intake, evidence | Only fields needed now, what is missing, source of prefilled values |
| UIP-03 Review | Human review | Item, findings, evidence, request-changes path |
| UIP-04 Decide | Consequential decision | Options, evidence, governing rule, authority, rationale |
| UIP-05 Sign | E-signature | Signatories, status per document, reminders |
| UIP-06 External | Work in a connected platform | Link, version, mirrored status, return point |
| UIP-07 Wait | Waiting on someone | Who, since when, threshold, nudge/escalate |
| UIP-08 Journey map | Steps assembled for this request | Done, current, upcoming, parallel, inserted, and why |
| UIP-09 Adopt configuration | Missing knowledge with a template | Template summary, placeholders, accept / edit / author |

Never show spec IDs in UI text; they belong in specs and code comments.

## 9. Definition of done

Per feature group:
- All four files exist, follow section 4, and carry version and status.
- Entities separate lifecycle, progress, attention conditions and derived eligibility; every transition has trigger, guard and performer.
- Every intent has a goal state; every activity has preconditions, outputs, emits, AI boundary and UI pattern, and names no "next" activity. Every user story has testable acceptance criteria.
- Every rule is typed; every Governed rule names its knowledge items.
- Every task has a clears-when; every human decision, performer and recipient maps to a permission.
- Scenario coverage met.
- Format rules met; every open question has an owner.

For the product:
- The feature register lists every feature, each with a folder and a complete file group; no capability sits in two features.
- No duplicate IDs across workbooks; no broken or orphan IDs.
- Every ID reference is a working link, across features; the link check (section 15) reports nothing to fix.

## 10. Procedures

### Setting up a new product
1. Agree the profile (section 1).
2. Divide the product into features (section 2) and get the owner's confirmation. Ask if the split is unclear.
3. Create the Shared group and one file group per feature as skeletons (section 14).
4. Write the Shared D1 sections 1 to 6: problem, principles, vision, users, scope, feature map.
5. Fill Shared Entities & States with the entities more than one feature uses.
6. For each feature, in priority order: write its D1 sections 1 to 5; fill Entities & States and Transitions (sketch each lifecycle first); fill Intents or User stories with goal states and entry points.
7. Pilot the intent or story that touches the most tabs end to end, with three or four scenarios.
8. Review the pilot with the technical team (format), developers (buildability) and UX (patterns); fix the columns for all features.
9. Complete the rest of each feature, reusing building blocks and citing Shared and other features by ID.
10. Finish Scenarios, then each feature's D2, D3 and D1, then the Shared D2 index and D3.
11. Run the definition of done and the link check; the owner approves.

### Adding a feature
1. Agree the name, code, owner and scope with the owner, and confirm it doesn't overlap an existing feature. Ask if it might.
2. Add it to the feature register (Shared Read me), the Shared D1 feature map and the Shared D2 index.
3. Create its file group (section 14) and fill it as in step 6 onward above.

### Adding a capability to an existing feature
No new files. Add rows to that feature's workbook and a row to its D2. Update its D3 only if what a persona sees changes, and its D1 only if scope changes. If the capability is used by other features, add their references (links) too.

### Reviewing
Check a feature group, or the whole product, against sections 2, 4, 5, 7 and 9. Report each gap with its location (feature, document and section, or tab and ID) and the rule it breaks. Don't fix anything unless asked.

Change control: the business owner approves content; the technical team confirms format; UX confirms pattern impact.

## 11. Answering questions from a set

When the set exists, you are its reader, not its designer.

- Every statement about behaviour cites an ID, or document and section. No source, no sentence.
- Never fill gaps with general knowledge, common practice or a prototype.
- Find the feature from the question (or the ID's feature code). Search that feature's workbook (all relevant tabs and open questions), then Shared, then any feature its rows cite, then the documents, with synonyms, before saying something is missing.
- Not covered: **"Not defined in the documents.** I checked: <features, files and tabs>." Then what is defined nearby, and whether an open question covers it.
- Partly covered: split into **Defined** and **Not defined**.
- Open questions are undecided; quote them, never present them as decisions.
- Retired rows are not current; name the replacement.
- Answer about Phase 1 unless asked; say when something is Next or Later.

Shape: **Answer** (with linked IDs, section 15; quote criteria and rules exactly, then plain words) · **Not defined** (if any) · **Source** (feature, file, tab, version, status).

For "what happens when…": walk the chain with IDs, across features where it crosses: trigger, transition (guard, performer), rules, tasks and notifications, what the user sees. Name any missing step.

## 12. Drafting rows

- Decide the owning feature first (section 2). If unclear, ask.
- Read the target tab's header row and use its exact columns.
- Deliver drafted rows as an Excel file of proposed rows per feature (section 14), not only as a chat table, whenever there are more than a few rows or the team asks for a file.
- When answering from an existing set, label drafts **Suggestion (not in the documents)**; give them as a table the owner can paste, plus the reason. Never claim a document was updated unless you edited it at the owner's request.
- Check knock-on effects in every feature: rules, permissions, transitions, tasks, notifications, scenarios, the D2 rows.

## 13. Jira tickets

The workbooks are the master; content flows one way, workbook to Jira.

- Read every row the item cites, and every row those cite, in any feature.
- One Epic per row of a feature's D2; one Story per user story or intent. Label every ticket with the product and the feature code.
- Copy business text exactly; plain words only under "In short".
- Omit empty sections except "Open questions and gaps" and "Source" (write "None").
- Show drafts first; create only on explicit go-ahead, Epic then linked Stories. Update existing tickets with the same `[ID]` instead of duplicating. Never change status, assignee, sprint or priority unless asked.

### Story template

**Summary:** `[<ID>] <plain name>` · **Type:** Story · **Labels:** product, feature code, phase, cited IDs · **Epic:** its D2 row

```
### In short
<Who does what, and why.>

### User story  (<ID>)
As a <As a>, I want to <I want to>, so that <So that>.
(Engine-driven: Intent <ID> · Goal state · Entry points)

### Acceptance criteria  (copied exactly from <ID>)
- [ ] AC1 <criterion>

### Business rules
| ID | Statement | Type | Effect |

### States and transitions
| ID | From → To | Trigger | Guard | Performed by | Emits |

### Activities and decisions  (engine-driven only)
| ID | Activity | Human decision | Preconditions | Outputs | UI pattern |

### Permissions
| ID | Object · Action · Scope | Basic | Requires |

### Tasks and notifications
| ID | Name | Recipient | Clears when / Default channels |

### Knowledge needed  (engine-driven only)
| ID | Knowledge item | Tier | Fallback template |

### Depends on other features
<IDs from Shared or other features this story uses>

### UI
Screen or journey moment · Pattern · Design link

### Out of scope (Later)
<cited items with Phase Next/Later>

### Test notes
Scenarios and expected outcome · each guard that can fail and what happens

### Open questions and gaps
<Q IDs quoted> · Not defined: <gaps>

### Source
<Feature> Registries v<version> (<status>), <date> · tabs · link
Every ID in this ticket links to its row in the workbook that defines it.
Business content is copied from the workbook: change it there, not here.
```

### Epic template

```
Summary: [<Product> <Feature>] <D2 row>   Type: Epic

### In short
### Scope
D2 row · Phase · Priority · Dependencies · IDs
### Stories
- [<ID>] <name>
### Open questions and gaps
### Source
<Feature> D2 and <Feature> Registries, versions and status
```

### Drift check
On request, compare each ticket's Source version and copied text with the current rows; list changed, retired (with replacement) or newly questioned items; refresh only after approval.

## 14. Output: Word, Excel and Google Drive

Every file this skill creates is a real file: each D1, D2 and D3 as **Word (.docx)**, each Registries workbook as **Excel (.xlsx)**, in the folder layout of section 4. Before building, confirm once which groups and files are wanted (the Shared group and all features, or some). Name files as in section 4.

### Word documents (D1, D2, D3)
Read the docx skill before building. Then:
- **Cover:** title, product, feature (or Shared), purpose, version, date, owner, status, and the line "Follows the OP Business Documentation standard".
- **Table of contents** after the cover, built from real heading styles (Heading 1 per numbered section, Heading 2 below).
- **Sections** exactly as in section 4 for that document and group. Tables are real Word tables with a bold header row that repeats across pages.
- **Footer:** document name, version and page number.
- Sections not written yet hold a bracketed placeholder, e.g. "[To be written: who the users are and what they gain]". Never fill them with invented content.
- IDs in the text are written in full (BIL-INV-US-12) and every one is a link (section 15).

### Excel workbooks (Registries)
Read the xlsx skill before building. Then, for the Shared workbook and each feature workbook:
- One sheet per tab, in order: Read me, the seven core tabs, then the extension tabs for the product type (section 5). Sheet names are the tab names.
- **Headers** in row 1 with the exact column names from section 5: bold, filled, frozen, with filters and wrapped text. Sensible column widths.
- ID is the first column and Row status the last.
- **Dropdowns** (data validation) for Row status, Phase and every column with a value list in section 5. Keep the lists on a hidden sheet named Lists.
- **Read me sheet:** manifest block (type, ID prefix, feature code and name, standard version, schema version, version, date, owner, status, file location), purpose, tab guide (Tab · One row is · Status: In use or None), how to edit, links to the Shared workbook and this feature's documents, and the open questions table. The Shared Read me adds the feature register.
- Empty tabs keep their header row. No merged cells inside tab data.
- Every ID is linkable (section 15): run the Excel link pass over all workbooks together as the last build step.
- **Proposed rows** go in a separate file per feature, "<Product> <Feature> Registries proposed rows <date>.xlsx": one sheet per target tab with that tab's exact headers, plus a Changes sheet (ID · Tab · Change: Add, Change or Retire · Reason). Never overwrite a team's workbook unless the owner asks.

### Delivery
1. Always give the finished files as downloads first, grouped by folder (zip the product folder when there are many files).
2. Then ask once where else they should go:
   - **Download only.**
   - **Add to Google Drive as Google Docs and Sheets** (recommended: editable in the browser, comments, one shared master, and each ID gets its own link).
   - **Add to Google Drive as Word and Excel files.**
3. If Drive is chosen:
   - It needs the Google Drive connector. If it is not on, say so, keep the downloads, and tell the user to turn on the Google Drive connector and ask again.
   - Ask for the destination folder (link or name) and confirm it by searching Drive. Create the product folder "<Product> Business Documentation" inside it, then the "00 Shared" folder and one numbered folder per feature.
   - Before uploading, search each folder for files with the same names. If any exist, ask whether to replace them, add them as a new version (name suffix with the version), or skip them. Never overwrite silently.
   - Upload **all workbooks first** (Shared, then features), run the Google Sheets link pass over all of them (section 15), then rebuild the Word documents with links to the uploaded workbooks and upload them into their folders.
   - Upload each file with the connector's create-file tool: base64 content, the file's content type (Word: application/vnd.openxmlformats-officedocument.wordprocessingml.document; Excel: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet) and its feature folder as parent. For Google format leave conversion on; for Word and Excel format turn conversion off.
   - Afterwards list the folders and give the user a link to each file, grouped by feature. Ask them to open each once and check that headings, tables, dropdowns and ID links came through.
   - Record the folder links in the feature register and each workbook's Read me manifest as the master location.
4. Later changes to files already in Drive: edit the Google file in place only when the owner asks (follow the google-workspace skill), or upload a new version as above. After any workbook change, re-run the link pass for that workbook and for any workbook that cites it.

## 15. Linkable IDs

Every reference to an ID anywhere is clickable and opens the place that defines it, in its own feature's workbook. The ID in its own defining cell (column A of its row) is not linked.

**Where each ID lives**
- Workbook IDs: the row whose first column holds the ID, in the workbook of its feature code. IDs defined inside another row (state dimensions, invariants, decisions written in an activity) point at that row.
- D3 IDs that live in the document (journeys J-, UI patterns UIP-): a bookmark on their heading.
- Open questions (Q-): their row in the Read me open questions table.

**Name convention:** the named range for an ID is the ID with underscores: `BIL-INV-RULE-07` is `BIL_INV_RULE_07`. It covers the whole row.

**Link colour:** blue (#1155CC), underlined.

### Excel (.xlsx)
1. Every workbook gets a defined name for each of its own IDs, covering the row.
2. Every cell that mentions an ID gets a hyperlink: to the defined name in the same workbook, or to the other workbook by relative path (`../00 Shared/Billing Shared Registries.xlsx#BIL_CORE_ENT_CUS`). Cross-feature links work while the product folder keeps its layout.
3. **Limit:** Excel allows one link per cell. A cell that lists several IDs links to the first one; the others are reachable through the Name Box in their own workbook. Say this once when delivering an Excel-only set, and recommend Google Sheets, where each ID gets its own link.
4. Run [scripts/link_excel.py](scripts/link_excel.py) over **all** workbooks of the product together, as the last build step and after every change (it needs `openpyxl`):

```
python scripts/link_excel.py <PREFIX> <workbook.xlsx> [<workbook.xlsx> ...]
```

Add names by hand for IDs defined inside another row. Every DUPLICATE ID and BROKEN REFERENCE is a defect (section 7): report it, never invent or move rows to fix it.

### Google Sheets (after upload with conversion)
Imported names become named ranges with random IDs and imported cell links don't work in Sheets, so run [scripts/link_sheets.py](scripts/link_sheets.py) in two passes over **every** workbook of the product, after uploading and after every edit session. Keep all files for the product in one scratch folder.

For each workbook, with its spreadsheet ID:
1. Read the named ranges (`get_spreadsheet`, fields `namedRanges`) into `nr_<id>.json`, and the grid of every tab (`get_spreadsheet` with grid data; fields `sheets.properties.sheetId`, `sheets.properties.title`, `sheets.data.startRow`, `sheets.data.rowData.values.userEnteredValue`, `sheets.data.rowData.values.textFormatRuns`, `sheets.data.rowData.values.hyperlink`) into `grid_<id>.json`.
2. **Pass 1, ranges:** `python scripts/link_sheets.py <PREFIX> <id> grid_<id>.json nr_<id>.json ranges`. If it writes range fixes, apply `range_reqs_<id>.json` with `update_spreadsheet`, re-read the named ranges and run again until it says "ranges clean". This writes `links_<id>.json` (each ID to the URL of its row).

When pass 1 is clean for every workbook:

3. **Pass 2, links:** `python scripts/link_sheets.py <PREFIX> <id> grid_<id>.json nr_<id>.json links` for each workbook. Apply `link_reqs_<id>.json` with `update_spreadsheet`, in batches of about 24 KB. Each ID in a cell gets its own link, to its row in this workbook or in another feature's workbook.
4. Re-read a few changed cells to confirm. Keep the `links_*.json` files: they are what Word documents, chat answers and Jira tickets link to.

Done means: every workbook says "ranges clean", 0 cells to link, no DUPLICATE ID, and every BROKEN REFERENCE reported to the owner.

### Word documents (D1, D2, D3)
Every ID in the text and in tables is a hyperlink to its row in the workbook of its feature:
- **Downloads:** link by relative path to the workbook and the ID's defined name, e.g. from `01 Invoicing/`: `Billing%20Invoicing%20Registries.xlsx#BIL_INV_RULE_07` or `../00%20Shared/Billing%20Shared%20Registries.xlsx#BIL_CORE_ENT_CUS`. Tell the user the links work while the product folder keeps its layout.
- **Google Drive, Google format:** link to the row URL from the `links_*.json` files. Build the documents after the workbook link pass, then upload them.
- **Google Drive, Word and Excel format:** Drive can't open an Excel file at a row, so link each ID to its workbook's Drive URL and say so once.
- IDs that live in the document itself (J-, UIP-) link to a bookmark on their heading; Shared journeys and patterns are linked from feature documents by the Shared D3 URL or path.
- An ID with no defining row stays plain text and is reported as a broken reference.

### Chat answers and Jira tickets
When the workbooks are in Google Sheets, write each ID as a link to its row: `[BIL-INV-RULE-07](https://docs.google.com/spreadsheets/d/<sheet id>/edit#rangeid=<range id>)`, using the workbook of the ID's feature code. Read that workbook's named ranges first to get the range IDs. If they can't be read, link the ID to its feature's workbook and tab instead, and never make up a range ID.
