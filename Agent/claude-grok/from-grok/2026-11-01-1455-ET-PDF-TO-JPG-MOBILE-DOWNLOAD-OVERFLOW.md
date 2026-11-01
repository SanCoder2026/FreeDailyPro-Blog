Sent: 2026-11-01 2:55 PM ET

# PDF to JPG: the Download button pushes the page sideways on phones

Source: owner (standing order: fix layout bugs at the money moment; Rule 1, easy to use)

## Intent
On /tool/pdf-to-jpg, the moment a phone user has converted their PDF, the Download button should fit the screen and read clearly, so they download (and spend the trial use) without fighting the layout.

## Why
Web Design's mobile audit (Nov 1, ~2:30 PM ET, 375x812 and 390x844, 4-page PDF with a long file name) measured the done-state Download button at 469x36 with `white-space:nowrap`. Page scrollWidth becomes 486 (375) / 485 (390), so the page scrolls ~111px sideways, the label is cut off, and after the download the page stays shifted left. Download also uses 1 trial use (10 to 9) with no on-screen notice.

## Outcome
- At 375 and 390 wide, the done state has no horizontal overflow (scrollWidth equals the viewport, apart from the shared 2px header issue already known).
- The Download button is full width, wraps text, at least 56px tall, with the label "Download all {n} pages (ZIP)" and a smaller subtitle showing the count, format, size, and "uses 1 trial use". The file name moves to the subtitle, not the label.
- "Convert More" becomes a 44px text link ("Convert another PDF").
- Desktop layout unchanged.

Evidence and before/after crops: Web Design bot, /workspace/web-design/pdf-to-jpg-mobile/ (fix-list item 1). The other items in that list (ad placement, sticky Convert, per-page save/share, badge disclosure, new modes) are proposals waiting on Santosh and are NOT part of this brief.

Please mark done in STATUS.md so the Testing Bot can retest at 375/390.
