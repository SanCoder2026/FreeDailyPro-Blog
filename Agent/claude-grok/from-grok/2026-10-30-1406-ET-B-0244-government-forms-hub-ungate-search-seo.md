Sent: 2026-10-30 14:06 ET

# B-0244 Government Forms Hub: don't gate a link directory, add search and state forms, fix title and meta
Priority: P2 · Estimated effort: M · Report: #139 · Source: Playwright headless, 0 trial uses, 1280/390 px + curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~14:03–14:05 ET. L-243 rank 1 (PDF Toolkit, live on ApyHub), then alphabetical. No GA/GSC rows for this page in the cited files.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Someone looking for a W-4, W-9, I-9 or 1099-NEC should get to the current official form in one click, and be offered to fill it in our PDF Editor.
## Why (1280 px; 0 trial uses)
- The page is a list of cards (Form W-4, W-9, 1099-NEC, I-9, W-2 …) with "View Official Form" (agency link) and "Fill in PDF Editor"; the copy says forms are not hosted or modified.
- **It still shows "Trial: 2 uses/day · 0 remaining today" with Day pass $3 / Monthly $9.99.** On the same run, Bates Numbering showed $1 day pass / $4.99 monthly. Owner to confirm whether the pass prices differ by tool on purpose; a trial counter on a page of outbound links reads as a paywall on free government forms.
- No search or filter; no edition/revision date per form (USCIS lists I-9 edition 01/20/25 and expiry dates on uscis.gov/i-9, checked ~14:04 ET); no state forms; no Spanish versions (IRS and USCIS publish them).
- No file input (by design). No overflow at 390 px.
## Who uses this
New hires, small employers and freelancers onboarding someone.
## Outcomes (ranked)
1. Remove the trial counter / pass prices from this directory, or say the links are always free.
2. Search box and filter (Tax, Employment, Immigration).
3. Show each form's current revision and a link to its instructions; Spanish version where the agency has one.
4. "Fill in PDF Editor" opens the editor with that form ready (admin to confirm today's behaviour).
## SEO
- **Now:** 200, sitemap, 11 hreflang, valid JSON-LD. **/es serves English** → **B-0123**. Site-wide → **B-0209**.
  - **Title "Find Official Government Forms Online - Directory | FreeDailyPro" is 64 chars.**
  - **Meta 68 chars.**
  - H1 "Government Forms" (generic).
- **Best result:** searchers want the form itself; irs.gov and uscis.gov rank top. Win with a hub page per form that links to the official PDF and offers fill-in.
- **Keywords:** "w-4 form", "w-9 form", "i-9 form", "1099-nec form", "new hire forms".
- **Suggested:**
  - Title: `Official W-4, W-9, I-9 & 1099 Forms – Links | FreeDailyPro` (58)
  - Meta: `Find the current official W-4, W-9, I-9, W-2 and 1099-NEC forms on the IRS and USCIS sites, then fill them in our free PDF editor. We never alter the forms.` (156)
  - H1: `Official US Tax and Employment Forms`
  - FAQ:
    - "Are these the official forms?" → "Yes, links go to the agency."
    - "Which forms does a new hire need?" → "W-4 and I-9."
    - "Is it free?" → only if the owner removes the counter.
## Constraints
Never host or edit government forms; link only.
## Test cases
1. Logged out at 0 trial uses: no trial counter or purchase prompt on the directory (if Outcome 1 accepted).
2. Each "View Official Form" link returns 200 on irs.gov/uscis.gov.
3. Title ≤ 60; meta 140–160.
