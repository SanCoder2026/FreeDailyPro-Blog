Sent: 2026-10-31 12:31 AM ET
# B-0316 Add Reddit as an official FreeDailyPro channel (homepage footer, same style as X/LinkedIn/YouTube)
Priority: P3      Estimated effort: 15–30 min      Source: owner

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
Santosh: "add reddit as our channel on the home page."

Reddit is now an active community channel for FreeDailyPro. The account is u/FreeDailyPro, and we are starting disclosed, helpful participation in r/mcp, r/apyhub, r/excel and other subs. Visitors and search engines should be able to see that it's an official account, the same way they see X, LinkedIn and YouTube. That also makes our Reddit disclosures ("I run FreeDailyPro") easy to verify.

## Why / evidence (checked 2026-10-31, 12:31 AM ET)
- The live homepage footer has a nav with `aria-label="Follow and pricing"` and the heading "Explore". It contains Pricing, Newsletter, and then text links in this order:
  - X (Twitter)
  - LinkedIn
  - YouTube
- Each social link is a plain text `<a>` with `target="_blank" rel="noopener noreferrer me" class="hover:text-foreground transition-colors"`. There are **no icons**, so match that text style rather than adding one.
- Source: `client/src/components/Layout.tsx` lines ~539–541 (repo at 74a9113). That's the shared Layout footer, so the change shows on every page, /developers included.
- The live homepage has **no Organization JSON-LD and no `sameAs`**. The only JSON-LD is a VideoObject. `hubSchema.ts` uses Organization only as a `provider`, without sameAs.
- `utility-api/core/seo/schema.ts` is the user-facing Schema Generator tool. Don't touch it.

## Outcomes
1. **Footer:** add `<li><a href="https://www.reddit.com/user/FreeDailyPro/" target="_blank" rel="noopener noreferrer me" aria-label="FreeDailyPro on Reddit" className="hover:text-foreground transition-colors">Reddit</a></li>` right after YouTube, so the order is X, LinkedIn, YouTube, Reddit. It belongs in the same list, on every page.
2. **Organization JSON-LD (optional):** a site-wide Organization block on the homepage would be a real SEO improvement:
   - `name`, `url`, `logo`
   - `sameAs`: X, LinkedIn, YouTube, Reddit
   If you think it fits, add it (one block on the homepage, valid in Google's Rich Results test). If it doesn't fit, say why and skip it.
3. **/developers (optional):** a short "Community" line linking the Reddit profile is fine if it fits the existing layout. Mention r/apyhub only if it reads naturally. Don't add a promo banner.
4. **Other channels:** if the site lists them anywhere else (About, Contact, newsletter template), add Reddit there too, in the same order.

## Acceptance criteria
- The live footer on `/`, `/developers` and a tool page shows "Reddit" after YouTube, with the same classes.
- `href` is exactly `https://www.reddit.com/user/FreeDailyPro/`, and it has `target="_blank"`, `rel` containing `noopener noreferrer me`, and `aria-label="FreeDailyPro on Reddit"`.
- It's keyboard focusable, has a visible focus ring like its siblings, and doesn't break the mobile footer layout (check at 375px width).
- If JSON-LD is added, it validates with no errors and `sameAs` lists exactly the 4 official profiles.
- There are no other visual changes, and existing tests and the build pass.

## Constraints
- Use "Reddit" as the plain text label. No icon unless all the channels get icons together.
- Don't link subreddits as if we own them. r/apyhub belongs to ApyHub.
- Don't change the existing channel URLs.

Source: owner
