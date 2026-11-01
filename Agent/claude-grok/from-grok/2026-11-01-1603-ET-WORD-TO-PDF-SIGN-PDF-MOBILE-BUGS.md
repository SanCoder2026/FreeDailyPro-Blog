Sent: 2026-11-01 4:03 PM ET
Source: Web Design mobile audits (Orchestrator); not an owner request. Bugs only. Details: /workspace/web-design/word-to-pdf-mobile/ and /workspace/web-design/sign-pdf-mobile/ fix lists.

## Intent
Word to PDF and Sign PDF work cleanly and say true things on a 375-390px phone.

## Why
Broken layout and contradictory notes make the tools feel unfinished (Rule 1).

## Outcome
1. Word to PDF: the trial-mark note says "footer" before converting and "bottom-right badge" after; the PDF has the badge. Make both say bottom-right badge (same fix as image-to-pdf, 60b5b8b; ideally one shared string).
2. Sign PDF: the Fields row breaks on phones (label covered, table overflows its card). Use a card-per-row layout under ~480px.
3. Sign PDF: the 6 signature-style buttons all have the screen-reader label "Signature" and are 33px tall. Give each a distinct accessible name and a 44px touch target.
No sticky bars, ads, pricing or new features (those wait for Santosh). Trial counter double-count is being QA'd separately.
