Sent: 2026-10-30 14:43 ET

# B-0272-v2 Emoji Picker: search relevance (whole-word matches first) and title/meta rewrite
Supersedes: 2026-10-30-1442-ET-B-0272-emoji-picker-copy-trial-seo.md (B-0272). The copy-limit framing in v1 was withdrawn: copy counting against trial uses is final (B-0142/B-0149 closed as "limit kept by owner").
Priority: P3 · Estimated effort: S · Report: #148 · Source: curl + seo.py, Playwright headless logged out at 1280/390 px, Google top 5 (WebSearch), 2026-10-30 ~14:36–14:43 ET. SEO backfill 11 (GSC Top 50 pages by clicks).

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
A person searching for an emoji should see the emoji they meant first.
## Why
- **GSC:** /tool/emoji-picker 10 clicks / 261 impr / 3.8% / pos 16.1 (raw analytics, Top 50 pages).
- Search works: "heart" → 46 emoji; "cat" → 20; "zzqx" → "No emoji found…". Categories and 6 skin tones present.
- **Relevance:** "cat" also returns 🫴 🤾 🤾‍♂️ 🤾‍♀️ 🪝 (matching "catch"); "hearth" returns 💟. Whole-word or name-start matches should rank first.
- At 0 trial uses, a click shows the trial-uses dialog, nothing is copied, and **no false "Copied" toast** appears (re-checked ~14:43 ET). This is correct behaviour; no change.
- Missing vs competitors (~14:40 ET): emoji names on hover/label (emotes.io); recently used row (MojiGrab, Use Emoji).
- No overflow at 390 px. Ad text "Learn Mandarin" stuck to copy → L-004. /es English title → **B-0123**.
## Who uses this
Social media users, writers and desktop users without an emoji keyboard.
## Outcomes (ranked)
1. Whole-word / name-start matches ranked above substring matches.
2. Emoji names on hover and as accessible labels.
3. Recently used row.
## SEO
- **Now:** 200, canonical, 11 hreflang, valid JSON-LD. Title "Emoji Picker Online Free - Search and Copy | FreeDailyPro" (57, has "Free"). **Meta 71.** H1 "Emoji Picker & Copy".
- **Keywords:** "emoji copy and paste", "emoji picker", "copy emoji", "search emoji".
- **Suggested:**
  - Title: `Emoji Picker – Search, Copy & Paste Emoji | FreeDailyPro` (56)
  - Meta: `Search every emoji by keyword or category, choose a skin tone, and click to copy it. Then paste the emoji into any app, message, bio or document you like.` (154)
  - H1: `Emoji Picker: Search and Copy Any Emoji`
  - FAQ: "How do I paste an emoji?" · "Can I choose a skin tone?" · "How do I get the Unicode code?"
## Constraints
Do not change the trial-uses rule.
## Test cases
1. "cat" → cat faces first; 🪝 and 🤾 not above them.
2. At 0 trial uses, a click never shows "Copied".
3. Title ≤ 60, no "Free"; meta 140–160.
