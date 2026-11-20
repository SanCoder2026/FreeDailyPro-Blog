Sent: 2026-11-20 08:40 ET

# Reproduce: FDP-13 Grammar Checker

Guest browser, https://www.freedailypro.com/tool/grammar-checker, English = Auto-detect unless noted. Each step costs no trial use today (tool is ungated). Faster: `node scripts/gc-offline.js` runs the same engine with no browser.

- **R1 (auxiliaries):** paste `Does she have time to meet tomorrow? Did it work after the update? Can he go to the meeting on Friday?` → Check Grammar. Output: "Does she has… Did it works… Can he goes…", listed as fixes, applied.
- **R2 (possessives):** `They visited their late father's house. The company lost its very best engineer. Thanks for signing up! Your welcome email is on its way.` → "they're late", "it's very best", "You're welcome email".
- **R3 (a/an):** `Paste a URL or a USB device name. The UX designer used a UI kit. Pick plan a or plan b.` → "an URL", "an USB", "an UI kit", "plan an or".
- **R4 (names/terms):** `Santosh reviewed it. Priya and Rahul reviewed the webhook payload. We flew to Bora Bora. (i) first item; (ii) second item.` → "Santos", "Oriya", "webfoot", "Bora", "(I)".
- **R5 (copy):** open "Details: when to use it, limits, privacy" and "Common questions"; compare with R1–R4 (auto-applied, agreement rewritten, no accept/ignore controls). View source for the FAQPage JSON-LD ("misplaced commas").
- **R6 (trial use):** in a context showing 0 remaining (`localStorage fdp-usage-v1` usageToday 10 of 10), click Check Grammar and Copy: no dialog, count unchanged, "Copied!". Compare /terms and the blog line "stay aware of 10 trial usages a day".
- **R7 (suggestion):** `Me and him was late.` → suggestion "consider 'him and I were'".
- **R8 (a11y/phone):** after Check, run axe on main → `label` critical on the output textarea; no `[aria-live]`/`[role=status]` in main. On iPhone SE (320×568), the output starts at y≈577.
