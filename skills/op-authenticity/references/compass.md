# The OP Authenticity Compass — 4 lenses, 16 dimensions

Use this file in Step 1 (what to look for in business files), Step 3 (the gap question to ask) and Step 5 (what a good rule looks like).

Each dimension below has:
- **Defines** — what the dimension covers.
- **Look for in business files** — signals that often hide inside requirements, BRDs, proposals and decks.
- **Found when** — the bar for marking it Found rather than Partial.
- **Gap question** — what to ask if it is Partial or Missing (adapt the wording to the product).
- **Good rule example** — the kind of rule to write in the profile.

The **critical four** (must score 2+ to pass the gate) are marked ★.

---

## PEOPLE — Who is it for?

### 01 Audience ★
- **Defines:** who uses the product: roles, age range, tech comfort, devices, data plans and connection quality.
- **Look for:** user roles and permissions tables, "actors" in use cases, target market sections, device or browser requirements, user counts, shift patterns, any mention of "mobile", "tablet", "desktop", "kiosk".
- **Found when:** each main user group is named with at least their role, rough age or seniority, main device, and tech comfort.
- **Gap question:** "Who will use this most days? Describe them: their job, roughly how old, and what phone or computer they use."
- **Good rule example:** "Primary users are clinic receptionists (25–45) on shared Windows desktops; secondary users are patients on mid-range Android phones with prepaid data. Design for low data use and large tap targets."

### 02 Persona
- **Defines:** two or three real-to-life people with names, goals, fears and a day in their life.
- **Look for:** customer stories, quotes from stakeholders, "pain points", journey maps, interview notes, support tickets.
- **Found when:** the files describe at least one specific person or situation with goals and frustrations, not just a role name.
- **Gap question:** "Think of one real person who will open this product next week. What are they trying to get done, and what annoys them today?"
- **Good rule example:** "Rana, 34, dental student supervisor: needs to approve 40 procedures a day between patients; hates re-typing the same notes in two systems."

### 03 Culture & Values ★
- **Defines:** beliefs, etiquette, family and gender norms, calendars and holidays, symbols and colours with local meaning, what would feel disrespectful.
- **Look for:** working days and hours, Ramadan or holiday schedules, gender-specific services (female doctor, separate sections), formality requirements, religious considerations (prayer times, Islamic finance), family roles in decisions.
- **Found when:** at least two concrete cultural rules are stated or clearly implied (for example working week, a gender preference, a formality level).
- **Gap question:** "Is there anything about how people here live, work or talk to each other that the product must respect — or anything that would feel disrespectful or out of place?"
- **Good rule example:** "Week runs Sunday–Thursday. Offer reduced hours in Ramadan. Patients can request a female clinician at booking. Address users formally (حضرتك) in all system messages."

### 04 Accessibility & Inclusion
- **Defines:** abilities, literacy levels, age-related needs, inclusive language, support for people who are often left out.
- **Look for:** WCAG mentions, elderly or low-literacy users, screen-reader needs, government accessibility mandates, multilingual workforce.
- **Found when:** an accessibility target is stated **and** at least one specific group's needs are named.
- **Gap question:** "Who might struggle to use this — older users, people with poor eyesight, people who don't read well, people who speak another language? How should we help them?"
- **Good rule example:** "WCAG 2.1 AA. Many technicians have limited reading in English: every key action has an icon plus an Arabic label; voice notes allowed instead of typed reports."

---

## PLACE — Where does it live?

### 05 Market & Region
- **Defines:** countries and cities, currency, units, date and number formats, local competitors and the apps users compare you to.
- **Look for:** client location, branches, launch countries, currency in pricing, competitor lists, "phase 2: expand to…".
- **Found when:** launch country/cities, currency and at least one local competitor or reference app are known.
- **Gap question:** "Which country and cities does this launch in, and which local apps or systems do users already use for something similar?"
- **Good rule example:** "Launch: Amman and Irbid. Prices in JOD with three decimals (3.250 JD). Dates as DD/MM/YYYY. Reference apps users trust: Talabat, Careem, eFAWATEERcom."

### 06 Language & Script ★
- **Defines:** languages and dialects, right-to-left or left-to-right, script typography, bilingual rules, which language users think in versus read in.
- **Look for:** "bilingual", "Arabic/English", report language, official documents, data entry language, names in two scripts.
- **Found when:** the primary language, the secondary language (if any), text direction and the dialect or register are stated.
- **Gap question:** "Which language do users mostly use on their phones and at work — and should the product speak formal Arabic, a local dialect, English, or a mix?"
- **Good rule example:** "Arabic-first (Modern Standard Arabic in UI, light Levantine in marketing), right-to-left by default, English toggle. Names stored in Arabic and English. Fonts must include Arabic glyphs."

### 07 Context of Use
- **Defines:** the real moment of use: where, when, on the move or at a desk, in bright sun, at night, one-handed, gloves on, poor signal, offline.
- **Look for:** field work, site visits, clinic workflow, shift work, offline requirements, kiosk or shared device, sunlight, noise.
- **Found when:** the main place and moment of use is described, including any physical or connectivity constraints.
- **Gap question:** "Picture the exact moment someone uses this. Where are they, what are their hands doing, and is the internet reliable there?"
- **Good rule example:** "Technicians use it on rooftops in 45°C sun, often wearing gloves, with patchy 4G. High-contrast mode, 56 px buttons, full offline job list with sync on reconnect."

### 08 Local Ecosystem
- **Defines:** the payment, maps, messaging, identity, delivery and government services people already rely on.
- **Look for:** payment gateway requirements, SMS/OTP, WhatsApp, national ID or e-government integrations, local ERPs, address formats, map providers.
- **Found when:** how users pay (if they do), how they sign in, and how they get support are known, using services that actually exist in the market.
- **Gap question:** "How do people here usually pay, sign in to apps, and ask for help — for example cards, CliQ, cash on delivery, SMS codes, WhatsApp?"
- **Good rule example:** "Pay by CliQ or cash on delivery; card as third option. Sign in with mobile number + SMS code. Support via WhatsApp Business. Addresses by area + landmark + map pin."

---

## PURPOSE — What does it stand for?

### 09 Industry & Domain
- **Defines:** vocabulary, workflows, trust signals and conventions that professionals in the field expect.
- **Look for:** process descriptions, glossaries, regulatory bodies, standard forms, codes (ICD, procedure codes, chart of accounts), job titles.
- **Found when:** the core workflow and its key domain terms are clear enough that an expert would not spot a wrong term.
- **Gap question:** "What would an expert in this field immediately notice if we got it wrong — a term, a step in the process, a form?"
- **Good rule example:** "Use FDI tooth numbering (11–48), not the US 1–32 system. Every treatment needs supervisor sign-off before the patient is billed."

### 10 Brand DNA
- **Defines:** origin story, mission, personality, and the one feeling every user should leave with.
- **Look for:** company profile, mission statement, brand guidelines, logos, tone words, "about us".
- **Found when:** brand personality and the intended feeling are stated, or a brand guide exists.
- **Gap question:** "If the brand were a person, how would they greet a customer? What is the one feeling users should leave with?"
- **Good rule example:** "Feels like a calm senior colleague: precise, warm, never salesy. Users leave feeling 'that was handled properly'."

### 11 Business Model
- **Defines:** how value is exchanged locally: pricing norms, who pays, subscription vs one-off, offers and loyalty habits.
- **Look for:** revenue model, pricing tables, licensing, B2B vs B2C, commissions, government tender terms.
- **Found when:** who pays, how much roughly, how often, and through which channel are known.
- **Gap question:** "Who pays for this, roughly how much, and how often? Is that normal for this market?"
- **Good rule example:** "B2B annual licence paid by the university; students never see prices. Invoices in JOD, VAT-inclusive."

### 12 Trust & Compliance ★
- **Defines:** data-protection law, sector regulation, where data must be stored, ethics, and what builds or breaks trust.
- **Look for:** "data must stay in-country", hosting requirements, privacy policy, health/financial/children's data, regulator names, audit or retention rules, consent.
- **Found when:** the applicable data-protection law and sector rules are named, plus where data is hosted and any consent requirement.
- **Gap question:** "Which laws or regulators apply here — for example data protection, health or banking rules — and is there any rule about where the data must be stored?"
- **Good rule example:** "Personal health data under Jordan's Personal Data Protection Law; explicit consent at registration; data hosted in-country; treatment records retained per Ministry of Health rules."

---

## PRESENCE — How does it look, sound and behave?

### 13 Visual Identity
- **Defines:** palette, type pairing that supports the product's scripts, iconography, and one signature element.
- **Look for:** brand guidelines, logo files, existing website or app, colour preferences, "modern", "clean", reference screenshots.
- **Found when:** brand colours and typefaces (or clear direction) exist, and the chosen fonts support every script the product uses.
- **Gap question:** "Are there brand colours, fonts or a logo we must use? Which colours or shapes already mean something to these users?"
- **Good rule example:** "Primary teal from the faculty crest; warm sand background. Type: IBM Plex Sans Arabic + IBM Plex Sans. Signature: the tooth-chart grid motif. Avoid red except for clinical alerts."

### 14 Interaction Patterns
- **Defines:** navigation habits, gestures, form style, information density and motion pace users are used to.
- **Look for:** existing systems users work in today, "like WhatsApp", data-entry volume, power users vs occasional users, keyboard-heavy workflows.
- **Found when:** the systems or apps that shaped users' habits are known, plus the expected density (quick glance vs heavy data entry).
- **Gap question:** "Which apps or systems do these users spend their day in? Should this feel quick and simple, or dense and powerful?"
- **Good rule example:** "Receptionists live in spreadsheets: keyboard shortcuts, dense tables, inline editing. Patients: WhatsApp-like simplicity, one action per screen."

### 15 Voice & Tone
- **Defines:** personality in words, formality, humour, and how success and errors are said.
- **Look for:** sample messages, SMS templates, tone words, formal/informal requirements, customer communications.
- **Found when:** formality level and at least one example of how the product speaks (a button, an error) are known.
- **Gap question:** "How should the product talk to people — like a formal official letter, a friendly expert, or a casual friend? Can you give an example message?"
- **Good rule example:** "Formal but warm. Button: 'احجز الموعد' (Book the appointment). Error: 'لم نتمكن من حفظ الملاحظة، حاول مرة أخرى' — never blame the user."

### 16 Content & Imagery
- **Defines:** real names, places, photos, examples and sample data from the user's own world.
- **Look for:** sample data, real forms, photos of sites or staff, product catalogues, real report examples.
- **Found when:** real or realistic local content exists to design with (names, places, items, photos).
- **Gap question:** "Can you share real examples — a filled form, product photos, real place names, a typical report — so the screens show the users' own world?"
- **Good rule example:** "Sample patients use local names (أحمد الخطيب, Lina Haddad). Photos of the real faculty clinics, never stock models. Example addresses: Jubeiha, Amman."
