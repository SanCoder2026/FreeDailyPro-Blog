Sent: 2026-11-06 10:48 AM ET

# B — JSON-LD Offer price "0" on tip-calculator and pdf-watermark

**Intent:** Stop schema implying the tools are free when they are Professional Tools with trial uses and paid passes.

**Why:** Web Design mobile audits Nov 6 (`/workspace/web-design/tip-calculator-mobile/`, `pdf-watermark-mobile/`): live SoftwareApplication JSON-LD has `"offers":{"@type":"Offer","price":"0","priceCurrency":"USD"}` while UI correctly shows Trial 10/day and Ad-free $1 day / $4.99 month. Same class of bug already fixed on other Professional pages. Layout/sticky proposals from those audits are **not** in this brief — they still await Santosh.

**Outcomes / done when:**
1. `/tool/tip-calculator` and `/tool/pdf-watermark` JSON-LD no longer advertise price "0".
2. Prefer day-pass `"1"` (USD) or omit price while keeping honest Professional positioning — match whichever pattern you already use on corrected sibling tools.
3. Title/meta/H1 stay free of “free tools”; on-page Trial / $1 / $4.99 copy unchanged.

**Suggested direction:** Shared schema helper for Professional Tools; fix these two and check whether the helper still emits "0" elsewhere. Layout/sticky work out of scope here.

**Constraints:** Never remove ads. No price changes. No “free tools” wording.

**Process:** Inspect schema builders → fix → curl/browser verify Offer → DONE note.

Source: owner
