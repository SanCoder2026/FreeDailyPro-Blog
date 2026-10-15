# Grok and Claude: how we pass work (read this first)

Two folders at the root of this repo. That is all.

```
from-grok/     Grok puts everything it writes here. Claude reads it.
from-claude/   Claude puts its answers here. Grok reads it.
```

Grok works only in this repo (FreeDailyPro-Blog). Grok never touches the main site code.
Neither side edits a file the other side wrote. Each side only ADDS new files. That is why nothing ever conflicts.

---

## For Grok

### 1. Every time you make or fix something, add ONE new folder in `from-grok/`

Name it: `YYYY-MM-DD-HHMM-short-name` (24-hour time, same clock every time, e.g. `2026-10-16-0715-pdf-tools-posts`).

```
from-grok/2026-10-16-0715-pdf-tools-posts/
  NOTE.md      what this is (template below)
  posts/       the post files
  images/      the images, if any
```

Never put files loose in `from-grok/`. Never reuse or overwrite an old folder. A fix is a NEW folder.

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

### 3. Every morning, before you start, read `from-claude/`

For each of your folders there will be one file there:
- `<folder-name>--ACCEPTED.md`: done. Claude is publishing it. Do nothing.
- `<folder-name>--CHANGES.md`: Claude wants changes. Read it, then make a FIX folder in `from-grok/` that answers every point.

No file for a folder yet means Claude has not looked at it. Wait.

### 4. Then commit and push to `main`

```
git pull --rebase origin main
git add from-grok
git commit -m "grok: <folder name>"
git push origin main
```

Always run from the repo root, `/workspace/artifacts/FreeDailyPro-Blog`.

---

## For Claude (each morning)

1. `git pull` this repo.
2. A Grok folder is NEW to me when `from-claude/` has no file starting with `<folder-name>--`.
3. Check each new folder against RULES (`site-blog-pack/`): unique wording, length, tags, links, images, facts.
4. Good: publish it to the site, then add `from-claude/<folder-name>--ACCEPTED.md` (one line is enough, with the date).
5. Not good: add `from-claude/<folder-name>--CHANGES.md` with a numbered list of exactly what to fix and where.
6. When Grok sends a FIX folder, check it against the CHANGES file and repeat from step 3.
7. Commit and push `from-claude/`.

Claude never edits or deletes anything in `from-grok/`.

---

## Older folders

Folders under `Agent/site/rewrite-*` and similar were made before this system. Claude handles them as before. From now on, everything new goes in `from-grok/`.
