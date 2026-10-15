# FreeDailyPro Blog Agent — Rules 1: NEW blog posts (site-only)

**Replaces:** `RULES.md`, `blog-agent/RULES.md`, `Agent/PLATFORM-UNIQUENESS-RULE.md`, `Agent/PLATFORM-LINKS.md`. Rewriting old posts is covered by `2-REWRITE-BLOG-RULES.md`.
**Effective:** 2026-10-15.
**Why it changed:** freedailypro.com is now the ONLY place posts are published. Blogger, WordPress, HubSpot and Medium packages are retired. Posts are checked by an automatic validator when they are added to the site; a post that breaks a rule marked **(checked)** is rejected and sent back.

Start line for every chat:
```
FreeDailyPro Blog Agent. Follow RULES.md strictly. All files only under Agent/site/. Request:
```

---

## 1. What a post is for
One post helps one reader finish one real task, then sends them to the tool that does it. One post = one tool, one narrow scenario, one category guide, one job role (persona), or one workflow. No broad "best tools" lists.

Use `blog-coverage.md` (given to you with these rules) to pick topics:
- Prefer tools under **No dedicated post yet**.
- Never write a second post with the same angle as an existing one. A new post on an already-covered tool is allowed only with a different scenario, title and body.
- To **replace** an existing post, the file name must be character-for-character the existing slug (list is at the bottom of `blog-coverage.md`). Never rename a slug while replacing; the old URL carries search history.

## 2. Where files go
```
Agent/site/batch-YYYYMMDD/
  posts/<slug>.md
  images/<slug>.webp
  INDEX.md          (table: date, slug, primary tool, topic, word count, image URL)
```
- File name = slug: lowercase words joined by hyphens, **no date prefix**, max 90 characters, e.g. `redact-pdf-before-sending-client-files.md`. (The publish date goes in the frontmatter.)
- The image has the same base name: `<slug>.webp`.
- Never edit files outside `Agent/site/`. No HTML preview files. Push to `main` so the files can be fetched without hunting.

## 3. Frontmatter (required)
```yaml
---
title: "Redact a PDF Before You Send It to a Client"
subtitle: "Remove SSNs and account numbers for real, not with a black box anyone can delete"
description: "Remove sensitive text from a PDF permanently in your browser. Step-by-step with a client-packet example."
date: 2026-10-20
author: "FreeDailyPro Team"
topic: pdf-tools
tools: [redact-pdf, split-pdf, compress-pdf]
personas: [legal]
workflows: []
tags: ["redact PDF", "PDF privacy", "client documents", "sensitive data", "FreeDailyPro", "PDF tools", "document security", "browser tools"]
image: "../images/redact-pdf-before-sending-client-files.webp"
imageAlt: "Person checking a redacted contract on a laptop beside a folder labelled PDF"
draft: false
---
```
Field rules:
- **title** (checked): 70 characters or fewer, catchy, specific. The word "free" must NOT appear. No "#1", "best in the world", "number one".
- **subtitle**: one line, 150 characters or fewer. Required. Different wording from `description`.
- **description** (checked): 70 to 150 characters. A plain benefit sentence. May mention "free" once for search only if natural; prefer not to.
- **date**: `YYYY-MM-DD`, the day it should go live (New York time). A future date means scheduled. Plan one post per day unless told otherwise.
- **topic** (checked): exactly one category id from the list in section 11, or `guides` only for general posts.
- **tools** (checked): real tool ids only, primary tool first, 1 to 4 items. The body must link to every listed tool. The tool ids are in `tool-ids.txt`. An unknown id is rejected.
- **personas / workflows**: optional real ids only (lists in section 11).
- **tags** (checked): 5 to 15, comma + space between items, no keyword stuffing. Tags live only in the frontmatter; never repeat them as text in the body.
- **image / imageAlt** (checked): both required. Alt text describes what is visible.
- **draft: true** posts are skipped.

## 4. Body structure
Top to bottom:
1. Hero image line: `![Alt text](../images/<slug>.webp)`
2. Blank line, then the subtitle in italics on its own line, identical to the frontmatter subtitle: `*Subtitle text*`
3. Blank line, then `[FreeDailyPro.com](https://www.freedailypro.com) --` followed by the opening paragraph (this line, the image and the subtitle are removed automatically when the post is added to the site, because the site draws them itself; keep writing them exactly like this).
4. Hook in the first 2 to 3 sentences: the reader's problem, in a concrete situation.
5. A short "quick answer" paragraph that names the tool and the result.
6. At least **3 `##` sections** (checked). Each section adds something new: a scenario, a numbered workflow, an edge case, a mistake to avoid, a comparison, a FAQ. Use `##` and `###` only. No `#` heading in the body (checked).
7. A numbered step list for the main task, using real controls and settings of the tool as they exist on the site.
8. A "Common mistakes" or "What to check" section.
9. Closing section: a clear next step and a natural link to the primary tool.
10. Last paragraph only: one short, topic-specific question asking what the reader would like next, linking to https://www.freedailypro.com/contact . Nothing after it.

No "Tags / Keywords" block at the end. No internal notes in the body (see section 9).

## 5. Length and readability
- **1000+ words** of real body text (checked at 900 minimum). Count from the opening paragraph to the end.
- Paragraphs: 3 to 6 lines, never more than 5 sentences or 100 words.
- Exactly one blank line between paragraphs and before each `##` heading. No triple blank lines. No trailing spaces. File ends with one newline.
- Never reach the word count by repeating sentences or paragraphs. If short, add a new scenario, FAQ entry or workflow step.
- Plain markdown only. **No HTML tags** (checked). Use `>` Tip lines sparingly: `> Tip: one short sentence.`

## 6. Links
- **At least 3 links to other pages of this site** (checked): the primary tool, 1 to 3 related tools, and where it fits `https://www.freedailypro.com/category/<category-id>` or `https://www.freedailypro.com/multitool-apps`.
- Tool links use the real id: `https://www.freedailypro.com/tool/<tool-id>`. Take ids only from `tool-ids.txt`. Never invent a URL (checked: every internal link must exist).
  - Examples: Compress Image is `compress-image` (not image-compressor); Word Counter `word-counter`; Merge PDF `merge-pdf`.
- You may link to other posts as `https://www.freedailypro.com/blog/<slug>` only if that slug exists in `blog-coverage.md` or in the same batch.
- Link related tools only where they help the reader's task. Do not list random tools.
- External links only to authoritative sources (government, standards bodies, official documentation), only when needed.

## 7. Messaging rules (standing owner decisions)
- Say **"200+ professional tools"**. Do not give any other count.
- The daily allowance is always **"10 trial usages"**. Never write "free uses", "free tries" or "free tier". After the trial: a $1 daily pass or $4.99 a month. Mention pricing only when relevant to the topic.
- Avoid the word "free" in title, subtitle and visible body copy. Say "professional", "browser-based", "no install". (The brand name FreeDailyPro is fine. The validator warns when "free" appears more than twice.)
- Never use "#1". If a claim is needed, use "a world leader in comprehensive coverage of professional tools, applications, APIs and workflows", sparingly.
- Sign as "FreeDailyPro Team". Never use a personal name.
- Do not mention AI, "AI-powered", "AI-policy proof", ChatGPT, or that the article was drafted by AI (checked). The site offers no AI features at present. If a topic is about workplaces that restrict software, talk about "approved software" and "files that stay on your device".
- Privacy claims: say files are processed in the browser and FreeDailyPro does not store them **only when that is true for the tool in the post**. Do not claim "100% privacy" or "no data ever sent" for a tool unless you know it is entirely client-side.
- Do not promise features, prices, limits, platforms, apps or API behaviour you have not verified on the live site. Do not invent statistics, reviews, user counts or awards.
- Special topics (Book Writing Toolbox, publishing platforms, tax, health): use only the fact sheet or an official dated source. Tax figures need the tax year and source named. Health calculators: general information, not medical advice.
- Do not say tool-specific YouTube videos are "coming soon". If a video exists the site embeds it; mention a video only when it exists.

## 8. Honest, specific content
- Practical, energetic and positive; honest about limits (file size, formats, what a tool cannot do).
- Include specifics a reader can reproduce: real settings, an example input and what the output looks like, a realistic mini case (for example, "a 12-page contract packet split into 3 files").
- Each post must read differently from the others. **Do not reuse sentences between posts.** In particular, do not reuse the same closing or "feedback" paragraph, the same privacy paragraph, or stock phrases such as "You've got this" across posts. The validator rejects sentences that appear in 3 or more posts (checked).
- Near-duplicate bodies are rejected (checked). Do not reword an older post into a new one.

## 9. Never publish agent notes
No sections or sentences about uniqueness, "AdSense-quality", SEO strategy, "why this post is different", the publishing process, or other platforms. Those belong in chat or INDEX.md, never in a post.

## 10. Hero image
- Exactly **1200 × 630 WebP, under 150 kB**. Do not ship thumbnails or other sizes.
- Topic must be obvious at a glance: a person doing the real task (office, home, studio, site), with visible props or UI for that tool (PDF pages, product photos, invoices, labelled folders). If the image could fit any post, regenerate it.
- Prefer people, with variety (women, men, older adults, groups). Natural, positive expression.
- Branding: **bottom stripe only**, logo "F." in #4FD8C4, the text "FreeDailyPro.com" with only the first F in teal and the rest white. No logo inside the scene, no top-left logo, no third-party logos or watermarks.
- Each post gets its own image. Never reuse an image between posts.
- Alt text is written for the image, not copied from the title.

## Videos (mandatory)
If the primary tool (or another listed tool) has a YouTube video, embed it. The site rejects a new post whose primary tool has a video but no embed.
- Syntax, on its own line with a blank line before and after, after the opening paragraphs and before the first `##` section: `{{youtube VIDEOID | Short caption}}`. VIDEOID is the 11-character id from `site-blog-pack/tool-videos.txt` (tool id, video id, title). Never paste an iframe or a youtube.com URL.
- Caption: 3 to 8 words naming what the video shows ("Split PDF by page range"). No "free".
- Primary tool first. Add a second video only when another listed tool has one and the section really uses that tool. Maximum 3 per post.
- The site shows the video as a 16:9 picture capped at about 600 px wide, centered in the text column; the player loads only when a reader clicks it and stays the same size. Write the sentence before the video so it introduces it ("The clip below shows the page-range step"), and do not describe it as fullscreen or add a second link to the same video.
- If a tool has no video yet, say nothing about one. Tools still waiting for videos are listed in `Agent/site/handoff/VIDEOS.md`. When a video for one of them is published, send its id as described there and add the embed to new posts about that tool.

## 11. Allowed ids
Category ids (`topic`): pdf-tools, image-tools, video-tools, audio-tools, text-tools, converters, tax-calculators, finance-calculators, health-calculators, qr-tools, business-tools, design-tools, security-tools, seo-tools, file-tools, 3d-tools, ecommerce-tools, travel-tools, event-tools, animation-tools, household-tools, college-tools, relocation-tools, marketing-design-tools, ai-studio, guides.
Persona ids: marketing, content-writer, web-designer, legal, real-estate, hr, freelancer, small-business, personal-finance, developer, student, event-planner, traveler.
Tool ids and workflow ids: `tool-ids.txt` (workflows are listed under "# workflows").

Choose the `topic` that matches the primary tool's category (the category column in `blog-coverage.md`).

## 12. Cadence and series
- Default: 1 new post per day, date set per post. Do not backdate.
- A weekly batch is 7 different tools or scenarios, never 7 copies of one idea.
- If asked for more per day, deliver them but keep every post unique.

## 13. Checklist before you push
- [ ] Topic is not already covered (see `blog-coverage.md`); slug is new or exactly the replaced slug
- [ ] title <= 70 chars, no "free", no "#1"; subtitle <= 150; description 70 to 150
- [ ] topic, tools (primary first), tags (5 to 15, comma + space), image, imageAlt present; ids valid
- [ ] 1000+ words, 3+ `##` sections, hook, quick answer, numbered steps, common mistakes, closing CTA
- [ ] 3+ internal links, every listed tool linked, no invented URLs
- [ ] "10 trial usages", "200+ professional tools", no AI mentions, no unverifiable claims
- [ ] No repeated sentences inside the post or copied from other posts; no agent notes; no tag block
- [ ] Last paragraph is a topic-specific question linking to /contact; nothing after it
- [ ] Hero 1200 x 630 WebP < 150 kB, topic obvious, bottom stripe only, unique to this post
- [ ] Spacing: one blank line between paragraphs; no triple gaps; no trailing spaces
- [ ] `INDEX.md` updated; pushed under the batch folder

*Keep this file stable. Change it only when the owner asks.*
