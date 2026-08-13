# FreeDailyPro Blog Agent — Easy Access

## How to start this agent in any new chat

Copy and paste this short prompt (or just say the first line):

```
Continue as the FreeDailyPro Blog Agent.
Follow RULES.md + config.yaml strictly.
All output only under Agent/posts/ and Agent/images/.
I need: [describe your request]
```

Or simply say:

**"FreeDailyPro Blog Agent – [your request]"**

Examples:
- FreeDailyPro Blog Agent – create image for the magazine-maker-launch post
- FreeDailyPro Blog Agent – write a new blog for the Book Maker tool
- FreeDailyPro Blog Agent – create images for all missing posts
- FreeDailyPro Blog Agent – prepare Blogger email version of this post

---

## What this agent does

- Writes full blog posts (≥600 words) following every FreeDailyPro rule
- Creates matching 1200×630 WebP hero images with branding stripe
- Puts everything only in `Agent/posts/` and `Agent/images/`
- Pushes to GitHub: https://github.com/SanCoder2026/FreeDailyPro-Blog
- Supports Blogger post-by-email workflow
- Never touches existing content outside the Agent folder

---

## Key files (always read these first)

| File | Purpose |
|------|---------|
| **RULES.md** | Complete locked rules (must follow) |
| **config.yaml** | Machine-readable rules + known tool URLs + slug list |
| **README.md** | Overview |
| **START-HERE.md** | This file – quick access |

---

## Current capabilities

1. New blog posts (with correct structure, links, privacy theme, CTA, feedback)
2. Branded images named exactly `<slug>.webp`
3. Replacement of existing blog images (exact slug match for SEO)
4. Varied content for Blogger to avoid duplicate issues
5. Clean Blogger email format (PLAIN + CLEAN-HTML)

---

## Quick commands you can give me

- "Create image for https://www.freedailypro.com/blog/XXXX/"
- "Write a new post promoting [tool]"
- "Create images for all posts that don't have one yet"
- "Prepare Blogger version of [post]"
- "Update the rules with ..."
- "List current Agent/images/"

---

## GitHub location of everything

https://github.com/SanCoder2026/FreeDailyPro-Blog/tree/main/Agent

- Images → `Agent/images/`
- Posts → `Agent/posts/`

---

**Tip:** Bookmark this START-HERE.md or pin the GitHub Agent folder.  
In a new conversation just paste the short activation prompt above and continue from where we left off.
