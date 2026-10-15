# FreeDailyPro Blog Agent: START HERE

**From now on you write blog posts ONLY for freedailypro.com.** Blogger, Medium, WordPress and HubSpot are retired and will be deleted. Do not create packages for them, do not mention them in posts, and do not worry about duplicating what is on them. Duplicates between posts on freedailypro.com do matter.

Claude (the site developer) imports your files into the website and runs an automatic checker. A post that breaks a rule marked "(checked)" is rejected and returned to you. Following the rules below avoids rework.

## 1. Files in this pack and what each one is for

| File | What to do with it |
|---|---|
| `00-START-HERE-INSTRUCTIONS-FOR-GROK.md` | This file. Read first. |
| `1-NEW-BLOG-RULES.md` | The full rules for any post: file format, frontmatter, structure, links, messaging, image, checklist. **Replaces every older RULES.md, START-HERE.md rule set, PLATFORM-LINKS.md and PLATFORM-UNIQUENESS-RULE.md in the repo. Ignore those from now on.** |
| `2-REWRITE-BLOG-RULES.md` | Extra rules when you turn an existing post into a site post, or upgrade a post already on the site. Rules 1 still apply. |
| `blog-import-plan.md` (and `blog-import-plan.csv`, same data) | The work list: 77 rows (ids R001-R015 and B001-B062). Each row names the source post in this repo, the target slug (file name), topic, tools, and what to fix. |
| `blog-legacy-upgrade-list.md` | 74 posts already on the site, worst first, that should be rewritten under the same slug. |
| `blog-coverage.md` | Which tools already have a post, which do not (backlog for brand-new posts), and every existing site slug. |
| `tool-ids.txt` | The only valid tool ids and workflow ids. Use them in `tools:` and in links `https://www.freedailypro.com/tool/<id>`. |

Put this folder in the repo as `site-blog-pack/` so you can read the files. Do not edit these files. Write your output only under `Agent/site/`.

## 2. The jobs, in order

Do the jobs in this order unless the owner asks for something else. Work in batches of 7 posts and push each batch to `main` before starting the next.

**Job A: replacements (plan rows R001 to R015).**
The site already has a thin post on each of these tools. Write the better version under the exact existing slug. Mode is REPLACE. Follow `2-REWRITE-BLOG-RULES.md`.
Output folder: `Agent/site/rewrite-YYYYMMDD/`.

**Job B: new posts from the plan (rows B001 to B062).**
The source post in this repo is your starting material. Write the site version as described in `2-REWRITE-BLOG-RULES.md`. Use the target slug, topic, tools and date from the row. Work in id order.
Output folder: `Agent/site/rewrite-YYYYMMDD/` (same structure).

**Job C: upgrade posts already on the site (`blog-legacy-upgrade-list.md`).**
Go worst-first, 7 per batch, same slug, same topic, better article. Follow section 7 of `2-REWRITE-BLOG-RULES.md`. If a post is too thin to deserve its own page, say so in `INDEX.md` and propose merging it into another; do not pad it.
Output folder: `Agent/site/rewrite-YYYYMMDD/`.

**Job D: brand-new posts for tools with no post yet (`blog-coverage.md`, "No dedicated post yet").**
Only when the owner asks, or when Jobs A and B are done. Follow `1-NEW-BLOG-RULES.md`. One post per tool, a specific task or scenario, 7 per week.
Output folder: `Agent/site/batch-YYYYMMDD/`.

## 3. The rules that matter most (details are in the rules files)

1. 1000+ words of real content, 3 or more `##` sections, short paragraphs. Never pad or repeat sentences.
2. Frontmatter must include `topic` (a category id), `tools` (real ids, primary first), 5 to 15 `tags`, `image` and `imageAlt`. See the template in `1-NEW-BLOG-RULES.md`.
3. Title: 70 characters or fewer, **no word "free"**, no "#1". Description: 70 to 150 characters.
4. Messaging: say "200+ professional tools" and "10 trial usages a day". Avoid the word "free" in visible text (the brand name FreeDailyPro is fine). **Do not mention AI anywhere**, including "AI-policy proof".
5. Links: at least 3 internal links. Every tool in `tools:` is linked in the body. Use only ids from `tool-ids.txt`. Known wrong ones in older posts: `/tool/qr-code-generator` (use `qr-generator`), `/tool/book-maker` (use `book-writing-toolbox`), `/category/developer-tools`, `/category/calculators`, `/category/finance-tools`, `/category/business-documents` (these categories do not exist; use a real category id).
6. No invented facts: no made-up customers, stories, testimonials, statistics or features. Check each tool on its live page before describing it. If you cannot verify something, leave it out.
7. Last paragraph: one short, topic-specific question to the reader linking to `https://www.freedailypro.com/contact`. Nothing after it. Do not reuse the same closing, privacy paragraph or stock phrases across posts.
8. Hero image: new for every post, 1200 x 630 WebP under 150 kB, a person doing the real task with the tool or props visible, FreeDailyPro bottom stripe only (no logo in the scene, no top-left logo).
9. File names: `<slug>.md` and `<slug>.webp`, lowercase hyphens, no date prefix. For replacements the file name equals the existing slug exactly.
10. Never put agent notes in a post (uniqueness, SEO, AdSense, other platforms).

## 4. What to deliver for each batch

```
Agent/site/<batch-folder>/
  posts/<slug>.md
  images/<slug>.webp
  INDEX.md
```
`INDEX.md` has one row per post: plan id (or slug), mode (NEW or REPLACE), slug, primary tool, word count, image raw GitHub URL, and any fact you could not verify. Push to `main` and tell the owner the folder name.

## 5. Start line for each chat

```
FreeDailyPro Blog Agent. Follow site-blog-pack/00-START-HERE-INSTRUCTIONS-FOR-GROK.md, 1-NEW-BLOG-RULES.md and 2-REWRITE-BLOG-RULES.md strictly. All files only under Agent/site/. Request:
```
Examples of requests:
- `Request: rewrite plan rows R001-R007` (replacements)
- `Request: rewrite plan rows B001-B007`
- `Request: upgrade the first 7 posts in blog-legacy-upgrade-list.md`
- `Request: write 7 new posts for the first 7 tools without a post in blog-coverage.md`

## 6. If Claude sends a post back
The reply lists the exact problems (for example "title contains free", "unknown tool id", "needs 3 internal links"). Fix only those, keep the rest, and push the corrected file under the same name.
