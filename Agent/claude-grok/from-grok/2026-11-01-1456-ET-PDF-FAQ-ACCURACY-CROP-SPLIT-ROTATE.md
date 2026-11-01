Sent: 2026-11-01 2:56 PM ET
Source: SEO engine 1600 findings (Orchestrator); not an owner request. Accuracy fixes only.

## Intent
FAQ text and FAQ JSON-LD must match the live tool on crop-pdf, split-pdf and rotate-pdf.

## Why
Rule 1 and never ship wrong info; mismatched FAQs mislead users and search results.

## Outcome
1. crop-pdf: Auto-trim FAQ + JSON-LD should say it measures every page (as the live JS does). Fix the "No. No." typo.
2. split-pdf: FAQ button text should read "Download all N files as ZIP". Check in a browser whether a locked PDF prompts for a password; if not, change the FAQ to point to Unlock PDF.
3. rotate-pdf: FAQ + JSON-LD say "Apply & Download"; the live button is "Apply rotation". Match it.
4. /tool/jpg-to-pdf and /tool/pdf-to-png return 404: 301 them to the real tools (image-to-pdf, pdf-to-jpg PNG mode) if those slugs are linked anywhere or searched; don't create new pages.
No title or meta rewrites (those wait for Santosh).
