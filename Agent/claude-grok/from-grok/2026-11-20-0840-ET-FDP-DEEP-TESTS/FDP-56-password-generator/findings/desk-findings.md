Sent: 2026-11-21 10:59 ET

# Desk findings (FDP-56)

- **Generator:**
  - `v(n)` rejection-samples `Uint32` (no modulo bias).
  - `we()` redraws the whole password up to 1e6 times until each group is present.
  - `Z()` does inclusion–exclusion over the groups for the exact count.
  - `Se()` gives passphrase bits = w·log2(7776) + log2(100·w) when a number is added.
- **Node run (`desk/stats.json`):**
  - 100k passwords: group shares upper .289 / lower .289 / digits .132 / symbols .290 (naive uniform .296/.296/.114/.296). That is expected under uniform choice over qualifying passwords.
  - Brute force 10,720 = site 10,720.
  - Spaces-only box: the alphabet includes " " (bug reproduced).
- **Copy path:** `gateShare` → `checkExport` (opens the cap dialog when known && !paid and blocked) → `tryUse` charge. The live gate never fired at 10/10, so the tool is treated as uncounted.
- **Copy text:**
  - FAQ (8) is accurate except the empty-box claim for whitespace.
  - Privacy "A usage count is recorded when you copy a password" contradicts the FAQ/How-to "never takes a trial use".
  - The UI line "no bias towards any character" is loose.
- **SEO:**
  - Title "Generate a Secure Random Password Online | FreeDailyPro"; meta "Generate strong, secure random passwords. Fast, right in your browser."; canonical self; hreflang 10 + x-default; og-default.
  - JSON-LD has 5 blocks (FAQPage 8). The VideoObject name differs from the YouTube title.
- **Blog** /blog/password-generator-new-accounts (Oct 17, 2026):
  - Sound advice; "300+ professional tools, premium applications and workflow products" (wording OK).
  - Doesn't cover passphrase mode or the symbols box. Closing sentence garbled ("note the exact rule text … when you reach FreeDailyPro through the contact page—rule screenshots of empty fields help less…").
  - Not linked from the tool page: the Guides links are chmod and cURL.
- **C50:** password-strength title "Password Strength Checker Online - Instant", but its meta is "Generate strong passwords and check strength. Fast, right in your browser." That is the overlap source. Keep both; rewrite that meta.
- GSC data is not available.
