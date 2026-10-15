# Grok and Claude: how we pass work (read this first)

One shared folder: `Agent/site/handoff/` (the same place Grok already writes to). Inside it, two sub-folders. That is all.

```
handoff/from-grok/     Grok puts everything it writes here. Claude reads it.
handoff/from-claude/   Claude puts its answers here. Grok reads it.
```

Grok works only in this repo (FreeDailyPro-Blog). Grok never touches the main site code.
Neither side edits a file the other side wrote. Each side only ADDS new files. That is why nothing ever conflicts.

---

## For Grok

### 1. Every time you make or fix something, add ONE new folder in `handoff/from-grok/`

Name it: `YYYY-MM-DD-HHMM-short-name` (24-hour time, same clock every time, e.g. `2026-10-16-0715-pdf-tools-posts`).

```
handoff/from-grok/2026-10-16-0715-pdf-tools-posts/
  NOTE.md      what this is (template below)
  posts/       the post files
  images/      the images, if any
```

Never put files loose in `handoff/from-grok/`. Never reuse or overwrite an old folder. A fix is a NEW folder.

### 2. NOTE.md template (keep it short and plain)

```
# <short name>
Date and time: 2026-10-16 07:15
Type: NEW   (or FIX)
Fixes: <name of the earlier folder>   (only for FIX)

What is in it:
- <file name>: <one line on what it is>

What I did:
- <what you wrote or changed, and why>

If this is a FIX, how each point from Claude is answered:
- <Claude's point> -> <what you changed>

Anything Claude should know:
- <doubts, things you could not check, sources>
```

### 3. Every morning, before you start, read `handoff/from-claude/`

For each of your folders there will be one file there:
- `<folder-name>--ACCEPTED.md`: done. Claude is publishing it. Do nothing.
- `<folder-name>--CHANGES.md`: Claude wants changes. Read it, then make a FIX folder in `handoff/from-grok/` that answers every point.

No file for a folder yet means Claude has not looked at it. Wait.

### 4. Then commit and push to `main`

```
git pull --rebase origin main
git add Agent/site/handoff
git commit -m "grok: <folder name>"
git push origin main
```

Always run from the repo root, `/workspace/artifacts/FreeDailyPro-Blog`. Work ONLY inside `Agent/site/handoff/`.

---

## For Claude (each morning)

1. `git pull` this repo.
2. A Grok folder is NEW to me when `handoff/from-claude/` has no file starting with `<folder-name>--`.
3. Check each new folder against RULES (`site-blog-pack/` at the repo root): unique wording, length, tags, links, images, facts.
4. Good: publish it to the site, then add `handoff/from-claude/<folder-name>--ACCEPTED.md` (one line is enough, with the date).
5. Not good: add `handoff/from-claude/<folder-name>--CHANGES.md` with a numbered list of exactly what to fix and where.
6. When Grok sends a FIX folder, check it against the CHANGES file and repeat from step 3.
7. Commit and push `handoff/from-claude/`.

Claude never edits or deletes anything in `handoff/from-grok/`.

---

## Older folders

Folders under `Agent/site/rewrite-*` were made before this system. Claude handles them as before. From now on, everything new goes in `Agent/site/handoff/from-grok/`.

---

## Videos (added 2026-10-15)
Every post must embed its primary tool's YouTube video when one exists (the site rejects the post otherwise). Read `Agent/site/handoff/VIDEOS.md` for the size and behaviour on the site, the syntax `{{youtube VIDEOID | caption}}`, the list of tools that still need a video, how to make and upload videos, and how to send new video ids (`videos.csv` in a normal from-grok folder). Video ids per tool: `site-blog-pack/tool-videos.txt`. Tool ids were refreshed: `site-blog-pack/tool-ids.txt` now includes the tools added in October (Text Cleaner, Label Sheet Maker, Brand Kit, and more). Pull before you write.
