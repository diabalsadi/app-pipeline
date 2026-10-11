# Industry pack · Fintech (payments, wallets, lending, BNPL, savings)
Owner: Library Curator · Version 1.0 · Last reviewed: 2026-10 · Verify legal facts before relying on them.

## Signals
- Trust and clarity beat novelty: users want to see exactly what they pay, when, and what happens if they are late.
- Central banks regulate payments and lending; many run regulatory sandboxes for new products.
- Islamic finance is mainstream: many users prefer or require Sharia-compliant products, which changes vocabulary (profit rate, murabaha, no "interest").
- Identity verification (KYC) relies on national digital identity where available.
- Family finances are often managed collectively; remittances matter for expatriate users in the Gulf.

## Do
- Show total cost, schedule and fees before commitment, in local currency format.
- Ask whether the product is conventional or Sharia-compliant and use the matching vocabulary.
- Use national digital identity for KYC where the market offers it (e.g. Nafath, UAE Pass).
- Support the local instant-payment and card rails users already use.
- Write error and decline messages that say what to do next, never blame.

## Don't
- Hide fees or use dark patterns around repayments.
- Use "interest" language for Sharia-compliant products, or religious language for conventional ones.
- Copy Western neobank visual clichés (neon gradients, crypto aesthetics) when the brand is about trust.

## References
- Jordan: Central Bank of Jordan (regulatory sandbox), JoPACC (CliQ, eFAWATEERcom), mobile wallets.
- Saudi Arabia: SAMA (regulatory sandbox, open banking), mada, SADAD, Nafath; BNPL: Tabby, Tamara.
- UAE: Central Bank of the UAE, Aani instant payments, UAE Pass; DIFC/ADGM free-zone regulators (DFSA, FSRA).
- Card security: PCI DSS for any card data handling.

## Tokens
Currency formats per region pack · amounts right-aligned with tabular figures · Sharia-compliant: yes/no (must be stated) · KYC: national ID method.

## Checks
- Full cost visible before confirmation.
- Vocabulary matches conventional vs Sharia-compliant decision.
- No card data stored outside a PCI-compliant provider.
