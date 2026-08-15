# FreeDailyPro Blog Agent — Easy Access (no hang)

## Fastest way to start in any new Grok chat

**Copy only this short line** (do not open long GitHub Pages links inside Grok):

```
FreeDailyPro Blog Agent. Follow RULES.md strictly. All files only under Agent/. Request: 
```

Then type your request after the colon.

### Examples (copy one)

```
FreeDailyPro Blog Agent. Follow RULES.md strictly. All files only under Agent/. Request: create Blogger package for the language support post
```

```
FreeDailyPro Blog Agent. Follow RULES.md strictly. All files only under Agent/. Request: write a new 1000-word Blogger post about free PDF tools, max 15 tags
```

```
FreeDailyPro Blog Agent. Follow RULES.md strictly. All files only under Agent/. Request: regenerate image for favorites post to match topic better
```

---

## Why the old “open this link in Grok” hangs

Grok can hang if you paste a large GitHub Pages URL or ask it to open and load a whole agent portal page.
**Do not** open long github.io or portal HTML links as the start of the agent.
**Do** paste the short prompt above. The agent rules live in RULES.md and conversation context.

---

## Permanent rules (always apply)

| Rule | Detail |
|------|--------|
| Output location | Only `Agent/posts/` and `Agent/images/` (or `Agent/blogger/` for Blogger week packs) |
| Blogger tags | **Max 15 labels** (Blogger limit 20; we use 15) |
| Site posts | ≥600 words (Blogger week posts ≥1000 words) |
| Images | 1200×630 WebP <150kB, topic-relevant humans, branding stripe |
| Body start | FreeDailyPro.com -- (linked) |
| No HTML previews | User does not want HTML preview files |
| Never edit outside Agent/ | Unless user explicitly asks |

Full permanent rules: `blog-agent/RULES.md`

---

## GitHub repo

https://github.com/SanCoder2026/FreeDailyPro-Blog

- Site-style posts: `Agent/posts/` + `Agent/images/`
- Blogger week pack: `Agent/blogger/posts/` + `Agent/blogger/images/`
- Schedule: `Agent/blogger/WEEK-SCHEDULE.md`

---

## Blogger publish reminder

1. Subject = post title
2. Body = content from FreeDailyPro.com -- onward
3. Attach matching .webp
4. Labels = max **15** from the post labels line
5. Send to your Blogger post-by-email address
6. Review in Blogger → schedule/publish

---

## Bookmark this (lightweight)

Raw START-HERE:
https://raw.githubusercontent.com/SanCoder2026/FreeDailyPro-Blog/main/START-HERE.md

Or keep the short prompt in Notes and paste into any new Grok chat. Never open a heavy portal URL inside Grok.
