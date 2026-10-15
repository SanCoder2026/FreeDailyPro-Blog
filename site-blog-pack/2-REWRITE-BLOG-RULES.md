# FreeDailyPro Blog Agent — Rules 2: REWRITING existing posts for the site

Use this file when the request names a row of `blog-import-plan.md` (ids like B012 or R003) or one of the slugs in `blog-legacy-upgrade-list.md`.
**Every rule in `1-NEW-BLOG-RULES.md` also applies** (frontmatter, structure, links, messaging, image, checklist). This file only adds what is different for a rewrite. If the two files disagree, this one wins for rewrites.

Start line:
```
FreeDailyPro Blog Agent. Follow RULES 1 and RULES 2 strictly. All files only under Agent/site/. Request: rewrite plan rows B001-B007
```

---

## 1. What a rewrite is
The source posts were written for Blogger, Medium, WordPress or HubSpot, in other voices and with older rules. The owner is deleting those external blogs once the site is done, so **copying from them is not a duplicate-content problem**. You may keep any wording from the source that is good, accurate and fits the site rules.

What still matters is the site:
- Each site post must be clearly different from every other post on freedailypro.com (different tool or scenario, title, headings, examples, closing). Never reuse a paragraph between two site posts.
- Fix everything the rules below list (wording, links, claims, structure). A source sentence that breaks a rule is rewritten, not kept.
- Other platform versions of the same topic (the plan's "alternate sources") may be mined for useful facts or examples, but publish only one post per plan row.

## 2. Inputs per row
For each plan row you get: id, mode, target slug, topic, primary tool, other tools, persona, the source file path (under `Agent/`), and notes. Use them exactly:
- **Mode NEW**: create a new file named `<target slug>.md`.
- **Mode REPLACE**: the file name is exactly the existing slug, character for character. The old URL and date are kept automatically. Improve it fully; do not make a second post on the same topic.
- Take `topic`, `tools` and `personas` from the row. The primary tool goes first in `tools`.
- Add the source path to the frontmatter for traceability: `source: "Agent/blogger/week-oct13/posts/2026-10-14-redact-pdf-remove-sensitive-data.md"` (the field is removed on import).
- `date`: the date in the plan row (YYYY-MM-DD). For REPLACE rows put today's date; the original date is kept.

## 3. What to keep, what to change

| In the source | In the site version |
|---|---|
| The core task, the real workflow steps, concrete numbers and settings | Keep the facts. Re-verify them on the live tool page. Re-express in new wording and a new order if it reads better |
| The word "free" (often 10 to 58 times) | Remove. Use "professional", "browser-based", "no install", "10 trial usages a day". The brand FreeDailyPro stays. Titles never contain "free" |
| "AI-policy proof", "AI tools", "company blocks AI" | Remove. No AI mentions. Say "files stay on your device" only if true for that tool |
| First-person invented stories ("The night I replaced my invoice spreadsheet", "Our tiny nonprofit ditched...") | Delete. Do not invent anecdotes, customers, testimonials or results. Use a clearly hypothetical case ("Say you run a three-person studio...") or a plain scenario |
| Platform voice (HubSpot "RevOps / Trust Ops / EdTech Ops" framing, Medium confessional tone, Blogger labels) | Replace with the site voice: practical, positive, specific, written to a reader with a task |
| "YouTube videos coming soon", "subscribe", "follow us" | Remove |
| "Tags: ..." lines, labels lines, "Blogger exclusive", uniqueness or AdSense remarks | Remove |
| Links | Fix every link. Only real ids from `tool-ids.txt`. The plan's "Fix links" column lists known wrong ones (for example `/tool/qr-code-generator` is `qr-generator`; `/tool/book-maker` is `book-writing-toolbox`; `/category/developer-tools` does not exist, pick the real category) |
| Many unrelated tool links in one post | Keep the primary tool and 1 to 3 truly related tools |
| Closing feedback paragraph copied across posts | Write a new, topic-specific closing question linking to /contact |
| Pricing, limits and capabilities | Keep only what you can see on the live site today. When unsure, leave it out |

Where the source is thin, wrong or generic, say less rather than padding. Where the source is missing something a reader needs (an edge case, a worked example, a common mistake, an FAQ), add it.

## 4. Verify before you write
For each tool in the row:
1. Open `https://www.freedailypro.com/tool/<tool-id>` and note the real controls, options, supported formats and limits.
2. Describe only what you saw. If a feature in the source is not on the page, drop it.
3. Confirm each related link exists (`tool-ids.txt`). Confirm any `/blog/<slug>` link against `blog-coverage.md`.

For tax, legal, health and finance posts: name the tax year and official source for any figure; add a plain sentence that it is general information, not professional advice; never invent thresholds, rates or dates.

## 5. Same rules as new posts (quick reminder)
- 1000+ words, at least 3 `##` sections, hook, quick answer, numbered steps, common mistakes, closing next step.
- 5 to 15 tags, comma + space. Title max 70 characters, no "free". Description 70 to 150 characters. Subtitle max 150.
- 3+ internal links, every listed tool linked.
- Image: a **new** hero for each post (1200 × 630 WebP under 150 kB, bottom stripe only, topic obvious). Never reuse the source post's image or any other post's image. File name `<slug>.webp`.
- Last paragraph is the topic-specific question linking to /contact.
- No sentences reused from other posts in the batch (the validator rejects sentences found in 3 or more posts).

## 6. Delivery
```
Agent/site/rewrite-YYYYMMDD/
  posts/<slug>.md
  images/<slug>.webp
  INDEX.md   (table: plan id, slug, mode, source path, words, image URL)
```
- Do 7 rows per batch unless asked otherwise. Push to `main`.
- In `INDEX.md`, list for each post what you changed and anything you could not verify.

## 7. Upgrading the existing site posts (`blog-legacy-upgrade-list.md`)
These 74 posts are already live. For each one:
- Mode is REPLACE. File name = the slug in the list. The URL and original publish date stay.
- The "Main problems" column says what to fix (thin, "free" in title, few tags, few internal links, repeated boilerplate sentences, AI mention, near-duplicate of another site post, missing video).
- Read the current post (the repo `Agent/site/...` or `posts/` copy, or the live URL `https://www.freedailypro.com/blog/<slug>`), then write the improved version as a new article on the same topic. Keep the topic and the useful facts; you may retitle.
- "Near-duplicate" means it shares text with another site post. Make this one clearly about its own tool or scenario and different in wording and examples.
- Work worst-first, 7 per batch. If a post is thin and the topic is very small, combine it into a stronger post and tell the owner in `INDEX.md` instead of padding.

## 8. Checklist before you push a rewrite
- [ ] Plan row id, mode and target slug followed exactly; `source:` set
- [ ] Different from every other post on the site (no shared paragraphs or closings)
- [ ] No invented stories, testimonials or numbers; every claim checked on the live tool page
- [ ] No "free" in title/subtitle/body (brand name excepted), no AI mentions, "10 trial usages", "200+ professional tools"
- [ ] All links are real; plan's "Fix links" handled
- [ ] Everything from the RULES 1 checklist (word count, sections, tags, image, closing question, spacing)
- [ ] New hero image created; not the source's image
- [ ] `INDEX.md` updated; pushed

*Keep this file stable. Change it only when the owner asks.*
