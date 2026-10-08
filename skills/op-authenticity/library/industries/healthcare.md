# Industry pack · Healthcare (clinics, hospitals, dental, pharmacy)
Owner: Library Curator · Version 1.0 · Last reviewed: 2026-10 · Verify legal facts before relying on them.

## Signals
- Trust is everything: users judge the product by calm, precision and privacy, not by flashiness.
- Many actors: patients, family members booking for them, receptionists, nurses, doctors, supervisors (in teaching hospitals/faculties), billing and insurance staff.
- Patients often act through family; gender preferences for clinicians are common in the region.
- Health data is a sensitive / special category of personal data in Jordan, Saudi and UAE data-protection laws; some countries add sector rules on where it is stored.
- Clinical vocabulary must be exact (e.g. dental: FDI two-digit tooth numbering is standard outside the US; ICD codes for diagnoses).

## Do
- Make consent explicit and readable at registration and before sharing records.
- Let a patient book for a family member and record the relationship.
- Offer clinician gender preference where culturally expected.
- Show clear appointment rules (arrival time, documents, cancellation) in the patient's language.
- Keep clinical screens dense but calm for staff; keep patient screens simple, one action per screen.
- Use real local clinic names, areas and realistic (fictional) patient names in mockups.

## Don't
- Stock photos of smiling Western doctors; red used for anything other than clinical alerts.
- Medical advice without a qualified professional in the loop.
- US-specific terms (HIPAA as the governing law outside the US, US insurance language, 1–32 tooth numbering).
- Show diagnoses or sensitive notes on shared screens or notifications.

## References
- Jordan: Hakeem (national electronic health record programme); Ministry of Health; Jordan Food and Drug Administration (medicines).
- Saudi Arabia: Sehhaty (Ministry of Health app), NPHIES (national insurance and health information exchange), Saudi FDA.
- UAE: DOH Abu Dhabi and Malaffi (health information exchange), DHA Dubai and NABIDH, MOHAP (Riayati); health data under Federal Law No. 2 of 2019.
- Standards: ICD-10/11 for diagnoses, FDI tooth numbering, HL7 FHIR for integration.

## Tokens
Data class: sensitive health data · consent: explicit · notification content: no clinical detail · time slots in local working week.

## Checks
- No clinical detail in push notifications or SMS.
- Consent captured and stored before any record is shared.
- Family/guardian booking works; clinician preference works.
- Domain terms reviewed by a clinician.
