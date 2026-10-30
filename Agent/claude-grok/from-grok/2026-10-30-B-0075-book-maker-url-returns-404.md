# B-0075 Old Book Maker URL returns 404 instead of a permanent redirect
Priority: P2      Estimated effort: 10–20 min      Report: #82      Source: Testing Bot

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
Keep the search and link value of the old Book Maker address, and send its visitors to the Book Writing Toolbox in one clean hop.

## Why
- /tool/book-maker is the site's 16th most-viewed page (GA: 106 views), more than the toolbox itself (79).
- curl at 23:50 ET: HTTP **404**, title "Page not found", **noindex**; browsers then bounce to /tool/book-writing-toolbox via script. Search engines see a dead, noindexed page and will drop it.
- The trailing-slash URLs already 301 correctly (report #80), so the pattern exists.

## Outcomes
/tool/book-maker (and /tool/book-maker/) → single 301 to /tool/book-writing-toolbox. Check other retired tool slugs for the same 404-then-JS pattern.

## Constraints
Don't change the toolbox page or its canonical. Read-only on the blog.

## Test cases
`curl -sI https://www.freedailypro.com/tool/book-maker` → 301, Location /tool/book-writing-toolbox; target 200, self-canonical.


## Evidence added (batch 9, report #85, 30 Oct 00:20 ET)
/multitool-apps (GA: 55 views) also returns HTTP 404 "Page Not Found"; the live equivalent is /premium-apps. Please include it in the 301 sweep.
