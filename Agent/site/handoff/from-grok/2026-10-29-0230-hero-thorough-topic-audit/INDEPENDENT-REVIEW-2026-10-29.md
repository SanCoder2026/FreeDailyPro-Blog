# Independent thorough review — 2026-10-29 (Grok)

Reviewed against owner originals:
- `RULES.md` §5 Image Rules
- `site-blog-pack/1-NEW-BLOG-RULES.md` §10 Hero image
- Locked `from-grok/HERO-IMAGE-RULE.md`
- Gold: `password-generator-new-accounts.webp`

## 1. Technical (all 27 pack images)

| Check | Result |
|-------|--------|
| Count | 27 files, match APPLY-MAP 1:1 |
| Size | all exactly 1200×630 WebP |
| File size | all < 150 KB (max ~101 KB etsy; min ~38 KB stage countdown) |
| Unique | 0 MD5 twins (size-twin mail-merge + plan-event is coincidence only) |
| Bottom FreeDailyPro brand | present on all (teal F + FreeDailyPro.com) |
| Floating F / logo in photo body | none found in pack |

**PASS technical.**

## 2. Branding style

| Asset | Script signature |
|-------|------------------|
| Gold password-generator | **brand_hero-like**: solid ~48px dark bar, teal circle “F”, no bottom hairline |
| This pack (27) | **brand_image** (locked preferred): gradient strip ~78px, logo F icon + FreeDailyPro.com, **teal hairline** at bottom edge |

Locked rule: prefer `brand_image.py`. Pack is correct. Gold is a historical alternate lockup that still meets “bottom stripe FreeDailyPro.com” wording. Do **not** rebrand pack to brand_hero solely to match gold pixels; keep brand_image.

## 3. Topic relevance (visual, every pack image)

| Slug | Topic props/UI visible? | Verdict |
|------|-------------------------|---------|
| assign-guests-to-tables-seating-chart | Large seating chart board + guest names | PASS |
| bates-stamp-production-zip-legal-desk | Bates stamps on legal pages + Production ZIP | PASS |
| capture-event-receipts-against-budget | Receipts + budget spreadsheet | PASS |
| corporate-safe-tools | “Chat assistant blocked” + local PDF tools | PASS |
| free-toolkit-every-developer-actually-uses | Browser JSON/Regex/Base64 toolkit | PASS |
| free-tools-for-college-students | GPA / PDF / Citation tools | PASS |
| free-tools-for-ecommerce-sellers | Product listing + packing slip | PASS |
| free-tools-for-freelancers-and-solopreneurs | Invoice + client tracker | PASS |
| free-tools-for-hr-professionals | Offer letter + onboarding checklist | PASS |
| free-tools-for-legal-professionals | NDA + redaction tools | PASS |
| free-tools-for-marketers | UTM builder / campaign UI | PASS |
| free-tools-for-personal-finance-planning | Budget + retirement calculator | PASS |
| free-tools-for-real-estate-agents | Listing + mortgage calculator | PASS |
| free-tools-for-small-business-owners | Invoice + inventory | PASS |
| free-tools-for-web-designers | CSS / image-compress tools | PASS |
| free-tools-for-writers | Manuscript editor + word count | PASS |
| freedailypro-vs-tinywow-privacy… | Privacy / free-tier comparison UI | PASS |
| how-to-stay-productive-when-company-blocks-ai-tools | Local tools + Chat blocked | PASS |
| install-event-apps-iphone-android | Phone install screens (no floating logo) | PASS |
| journal-submission-pack-paper-desk | Manuscript submission pack (not shipping) | PASS |
| launch-etsy-batch-with-seller-studio | Product batch SKUs + photos | PASS |
| mail-merge-letters-and-certificates-from-csv | CSV + mail-merge letters | PASS |
| one-link-per-exhibitor-trade-show-floor | Booth + one-link QR (no floating F) | PASS |
| plan-event-one-shared-project-event-suite | Shared Event Project board | PASS (weakest of pack but event-specific) |
| price-after-marketplace-fees-seller-pricing-desk | Marketplace fee calculator | PASS |
| run-stage-countdown-and-focus-rounds | Stage countdown 03:00 | PASS |
| safe-alternatives-to-chatgpt-for-document-work | PDF tools vs Chat AI blocked | PASS |

**27 / 27 topic PASS.** No pack image is generic stock that could fit any post.

## 4. Live site status (checked 2026-10-29)

| Status | Count | Notes |
|--------|------:|-------|
| Already applied (MD5 = pack) | **15** | seating, bates, receipts, developer toolkit, marketers, tinywow, AI-blocked, install apps, journal, etsy, mail-merge, exhibitor, plan-event, price-fees, stage countdown |
| Pending apply | **12** | mostly free-tools-for-* + corporate-safe + safe-alternatives + writers |

Spot-check: several **pending live** free-tools heroes already show clear tool UI (GPA, NDA, offer letter, invoice, CSS, etc.). Pack images are **stronger/unique replacements**, not the only acceptable version. Still apply the 12 for batch consistency.

Spot-check claimed PASS live heroes (password-strength, bulk-QR, cron-builder, booth leads, pdf-to-jpg, tip-calculator, word-counter, json-formatter, book-maker, browser-tools, 200-tools): **topic-correct**.

## 5. Issues / notes (not blockers for this pack)

1. **Brand visual ≠ gold** — expected: brand_image vs brand_hero. Keep brand_image per locked rule.
2. **plan-event** is the softest topic hit (shared project board). Still event-suite specific → PASS. Only regenerate if owner wants more “venue / guest list / timeline” props.
3. **`/blog/split-pdf.webp`** returned 404 HTML in this check — different slug path or missing file; not part of this 27 pack. Worth a separate missing-hero pass later.
4. Older README “PRIMARY 82 pack” lines are historical; **current hero-fix primary** for topic failures is this `0230` folder (plus remaining 12 pending).

## 6. Verdict

| Item | Status |
|------|--------|
| Locked HERO-IMAGE-RULE matches RULES §5 / §10 | YES |
| Pack technical compliance | PASS 27/27 |
| Pack topic relevance | PASS 27/27 |
| APPLY-MAP complete | YES |
| Ready for Claude to finish applying pending 12 | YES |

**No regeneration required for this pack.** Claude: apply remaining 12 images from `images/` per APPLY-MAP.
