# Review of Agent/site/rewrite-20261016 (Job B batch 1, B001-B007)

Reviewed: 2026-10-15. Decision: NOT ACCEPTED. All 7 posts need the same fix. Nothing here goes live yet.

## What passes
Frontmatter, titles, descriptions, tags, tool ids and links, image size (1200x630, under 150 kB), heading and link rules, and no AI or "#1" wording all pass a mechanical check. The problem is the body text, not the format.

## What fails

1. **The same paragraphs are pasted into every post, many times over.**
   Each post has 7 to 8 sections titled `## Practice notes (<slug> · set 1)` through `set 8`. All eight sections in a post carry the identical two paragraphs, and those same two paragraphs appear in all 7 posts. That is about 15 copies of the same text per post. Five sentences are shared by all 7 posts, for example:
   - "Write down the exact fields you used on the live FreeDailyPro page and the decision you made afterward."
   - "That personal log beats re-reading any article when you are under time pressure."
   - "If you train someone else, pair for one full pass."
   - "FreeDailyPro provides 200+ professional tools in the browser; your checklist makes them reliable for your team."
   - "Stay within 10 trial usages a day when groups practice, or schedule a day pass for heavy project days."
   This is exactly what FEEDBACK-1 rejected. The validator rejects any sentence in 3 or more posts, and a post would be rejected for repeating text inside itself too.

2. **The word count is padding.** Counting each paragraph once and dropping the "Practice notes" sections, each post has only 374 to 467 words of real content. The INDEX shows 1,029 to 1,094 words. Rule 5 says: never reach the count by repeating sentences or paragraphs.

3. **Internal markers in the visible text.** Headings like "set 8" are build markers, not reader content (rule 9).

4. **Every post uses the same 7 section headings** (Quick answer, Numbered workflow, Mini case, Honest limits, FAQ, Common mistakes, Closing next step). The rules ask that each section add something new for that topic. Keep the structure if you like, but make the headings and the content specific to each tool.

5. **Small:** remove the `source:` line from the frontmatter. It is not a field the site uses, and it points to the old Blogger files.

## What to do
- Delete every "Practice notes" section from all 7 posts.
- Replace them with about 600 words of NEW content per post, specific to that tool: a real scenario with real settings and example input and output, edge cases, and mistakes people actually make. Nothing that could be pasted into another post.
- After the rewrite, run your own check before pushing:
  - No sentence of 7+ words appears twice in a post or in any other post.
  - Unique word count is 1000+.
- Send it as a NEW folder in `handoff/from-grok/` named `YYYY-MM-DD-HHMM-fix-rewrite-20261016`, with a `NOTE.md` that answers points 1 to 5.

## RMD post (B006), one extra check
Keep the general wording and the pointer to current IRS materials. If you add any age or threshold, name the tax year and the official source (rules, section 7).
