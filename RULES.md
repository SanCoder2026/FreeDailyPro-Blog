# FreeDailyPro Blog Agent — Permanent Rules (Locked)

These rules are mandatory for every blog post. Follow them exactly so every delivery is flawless.

---

## 1. File & Folder Structure (GitHub)
- ALL new posts and images go ONLY into:
  ```
  Agent/
  ├── posts/
  └── images/
  ```
- Never create or edit files outside `Agent/` unless the user explicitly asks.
- Never create HTML preview files (user does not want them).
- Image filename and post filename must share the same date-slug base.

---

## 2. Frontmatter (YAML) — Required Fields
```yaml
---
title: "Catchy or emotional title that attracts attention"
subtitle: "Single-line italic subtitle for metadata. Keep short (ideally under ~150 characters)."
description: "One-liner ≤ 150 characters total. Used for portals and meta description."
date: YYYY-MM-DDTHH:MM:00
author: "FreeDailyPro Team"
image: "../images/YYYY-MM-DD-slug.webp"
tags: [keyword1, keyword2, ... many relevant tags ...]
draft: false
---
```
- `subtitle` and `description` are different. Subtitle can be a bit longer; description is the short portal one-liner.
- Tags live ONLY in the `tags:` field. Never repeat them as a text paragraph in the body.

### Tags / Labels limits (CRITICAL)
- **Blogger maximum: 15 tags only** (Blogger hard limit is 20; we cap at **15** for safety and cleanliness).
- FreeDailyPro.com site posts may use more tags in frontmatter when needed, but **any content prepared for Blogger must have ≤ 15 labels**.
- Prefer high-value tags: FreeDailyPro, free tools, privacy, main tool names, audience (freelancers, small business, etc.).
- Never dump 20+ keyword spam tags. Quality over quantity.
- When creating Blogger packages, the `labels:` / `tags:` line must contain **at most 15** comma-separated tags.

---

## 3. Body Content Rules
1. **Image first** (right after frontmatter):
   ```
   ![Alt text](../images/YYYY-MM-DD-slug.webp)
   ```
2. **Immediately after the image** the main body MUST start with:
   ```
   [FreeDailyPro.com](https://www.freedailypro.com) --
   ```
   (linked, so the site is visible from the very first word of the body).
3. **NO duplicated subtitle** — Never repeat the subtitle text as an italic paragraph under the image. Subtitle exists only in frontmatter.
4. **Hook** in the first 2–3 sentences — grab attention immediately.
5. **Minimum 600 words**.
6. **Energetic & positive** tone throughout.
7. **No paragraph longer than 100 words or 5 sentences**.
8. **As many live internal links as possible** to real FreeDailyPro tools and pages.
9. **Core theme mention** (somewhere natural in the post):
   free tools · no login required for most · everything stays on the client-side browser · no data sent to server · 100% privacy · AI-policy proof.
10. **Strong CTA** in the last paragraph (link to the main tool).
11. **Feedback request** at the very end:
    Ask what new features/tools the reader wants next.
12. **Future videos** — Mention that tool-specific YouTube videos are coming soon so people can see the tools in action.
13. **Clean ending** — End with the feedback request + short positive close. No trailing "Tags / Keywords" text block. Tags stay only in frontmatter.

---

## 4. Tool Links — Critical
- Always use the **real canonical slug** from FreeDailyPro.com.
- Before using any tool link, verify it (or use known good ones).
- Known correct examples:
  - Book Maker → `/tool/book-maker`
  - Compress Image → `/tool/compress-image`   ← NOT image-compressor
  - Word Counter → `/tool/word-counter`
  - Resume Builder → `/tool/resume-builder`
  - Merge PDF → `/tool/merge-pdf`
  - PDF tools category → `/category/pdf-tools`
- Prefer trailing-slash free clean paths that match the live site.
- Never invent tool URLs.

---

## 5. Image Rules
- Size: exactly **1200 × 630** WebP, under **150 kB**.
- Prefer **humans**:
  - Beautiful professional female with smile / positive emotion when suitable
  - Variety: males, elders, kids, groups as needed
  - Attire and setting match the blog theme (office / home / outdoor / worksite)
- **Topic relevance is mandatory (CRITICAL)**:
  - The image MUST clearly show what the blog is about — not a generic smiling person.
  - Include visible indicators: tool UI on screen (PDF pages, image editor panels, invoices, browser tabs), related props (folders labeled PDF, camera, product photos, client notebook), or setting that matches the subject.
  - Clothing, background, and persona must fit the topic (freelancer home office, creative studio for image tools, document desk for PDF, etc.).
  - If the image could fit any blog, it is wrong — regenerate until the topic is obvious at a glance.
- Branding: bottom stripe only
  - Logo **F.** in **#4FD8C4** (Space Grotesk style)
  - Brand name **FreeDailyPro.com** — only the first “F” is teal, rest white
- No third-party logos, watermarks, or copyright text.
- Placement: image sits right after frontmatter (above title in rendered view) or between subtitle and body as preferred by the user rules.

---

## 6. Title, Subtitle, Description
- **Title**: Catchy or emotional — must attract attention.
- **Subtitle**: Single line, used as italic under the title for metadata. Do NOT paste it again into the body.
- **Description** (one-liner): ≤ 150 characters. Clean, benefit-focused, for automatic portal submission.

---

## 7. Quality Checklist (run mentally before every delivery)
- [ ] Frontmatter complete and clean
- [ ] Image present with correct relative path
- [ ] Body starts with linked FreeDailyPro.com --
- [ ] No duplicated subtitle text in body
- [ ] No "Tags / Keywords" paragraph at the end
- [ ] All tool links use real FreeDailyPro slugs
- [ ] ≥ 600 words
- [ ] Paragraphs short (≤ 100 words / 5 sentences)
- [ ] Hook + energy + privacy theme + CTA + feedback request + future videos mention
- [ ] Image is 1200×630 WebP < 150 kB with correct branding stripe
- [ ] Files only inside Agent/posts/ and Agent/images/
- [ ] No HTML files created
- [ ] When replacing an existing blog: filename + slug is character-for-character identical to the original (see list in section 9)

---

## 8. Delivery Location
After generating:
1. Save Markdown → `Agent/posts/YYYY-MM-DD-slug.md`
2. Save branded image → `Agent/images/YYYY-MM-DD-slug.webp`
3. Push only those files into the GitHub repo under the `Agent/` folder.
4. Never touch existing root posts/, images/, or Grok/ content.

These rules are permanent. Follow them for every future post so delivery is flawless.

---

## 9. URL Slug Rule When Replacing Existing Blogs (CRITICAL for SEO & AdSense)

When the user asks you to go to FreeDailyPro.com blogs section and **create a blog to replace any existing blog**, you MUST follow this rule without exception:

**The URL slug (and therefore the markdown filename) must be exactly identical — character-for-character — to the existing slug.**

- Not similar
- Not reworded
- Not re-pluralized
- Not “improved”
- Not date-prefixed unless the original already had a date

Even a tiny difference (e.g. “compared” vs “comparison”, “tools” vs “tool”, adding or removing a word) creates a brand-new URL that loses all existing Google indexing and AdSense performance history.

### Exact existing slug list (use ONLY these when replacing)
```
book-maker-launch
convert-pdf-to-word-without-losing-formatting
free-3d-file-converter-and-screen-recorder
free-audio-tools-voice-memos-podcast-cleanup
free-browser-tools-no-install-needed
free-household-budgeting-and-grocery-tools
free-legal-document-templates-guide
free-menu-invitation-and-print-design-tools
free-relocation-and-moving-tools
free-toolkit-every-developer-actually-uses
free-tools-for-college-students
free-tools-for-ecommerce-sellers
free-tools-for-hr-professionals
free-tools-for-legal-professionals
free-tools-for-personal-finance-planning
free-tools-for-real-estate-agents
free-tools-for-small-business-owners
free-tools-for-web-designers
free-tools-for-writers
free-travel-and-event-planning-tools
freedailypro-200-free-tools-milestone
freedailypro-vs-tinywow-privacy-and-free-tier-compared
guide-to-free-health-calculators
how-to-stay-productive-when-company-blocks-ai-tools
is-it-safe-to-compress-images-online
removed-login-requirement-file-tools
retirement-calculators-explained
safe-alternatives-to-chatgpt-for-document-work
self-employed-tax-retirement-calculators
us-uk-india-tax-calculators-compared
where-to-get-official-tax-employment-forms
```

### How to apply
1. User says “replace the blog about X” or “update the existing post whose slug is Y”.
2. You identify the **exact** matching slug from the list above.
3. New markdown file name = that exact slug + `.md`  
   Example: `us-uk-india-tax-calculators-compared.md`
4. Image file name can keep a matching base (or the same slug).
5. Frontmatter `title` can be improved, but the **filename/slug stays 100% identical**.
6. Never invent a new slug when replacing.

For completely **new** posts (not replacements) you may create a fresh descriptive slug (and put it under Agent/).

This rule is permanent and non-negotiable.


---

## 10. Blogger-specific rules (when creating content for freedailypro.blogspot.com)

1. **Max 15 tags/labels** per post (hard rule). Blogger allows 20; we never exceed 15.
2. Content must be **substantially reworded** from FreeDailyPro.com versions (SEO / no thin duplicates).
3. Target **≥ 1000 words** for Blogger posts (site posts stay ≥ 600).
4. Include as many live FreeDailyPro.com tool links as natural.
5. Put Blogger packs under `Agent/blogger/posts/` and `Agent/blogger/images/` when creating a batch for the week.
6. Provide schedule + labels + image filename clearly for post-by-email.
7. Prefer plain body starting with FreeDailyPro.com -- so paste into email works cleanly.
8. No HTML email bodies that render as raw tags (user pastes clean text / light formatting).

This section is permanent.
