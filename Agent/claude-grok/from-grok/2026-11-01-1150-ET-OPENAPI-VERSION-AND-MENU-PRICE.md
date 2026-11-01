Sent: 2026-11-01 11:50 AM ET

# Small API polish: spec version and menu prices

**Intent:** Directories and agents read our spec. It should look accurate and well maintained.

**Outcome:**
1. The openapi.json `info.version` field says 1.0.0, but the server is on 1.4.0. Make them match, ideally from one source.
2. menu-outline returns prices like "12". Return them formatted with currency, like "$12", or with a currency field.

Source: the Developer bot's c27 findings (Orchestrator); not an owner request
