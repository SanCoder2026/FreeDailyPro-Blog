Sent: 2026-11-21 06:06 ET

# Instructions for Claude: FDP-45 HTML to PDF

1. Read REPORT.md ("How to work with us" first), then PRIORITIES.md.
2. Fix the WebKit hang first: put a timeout on the capture and image loads, fall back to the blank placeholder, and make Stop abort an in-flight capture. Confirm on real Safari/iOS.
3. Fix the shared Download trial-use wrapper: charge per new result and check the limit every time. It's the same fix as FDP-44, so verify both tools.
4. HtmlToPdf:
   - Recompute the file name per conversion.
   - Drop the empty leading page.
   - Stop resolving `#`/relative links to the FDP page.
   - Decode dropped files by their declared charset.
5. Copy: merge the duplicate FAQs, and move the 200-page limit into its own answer. Fuller meta description; OG image.
6. Plan the video re-record on a clean profile.
7. P3s: repeating table headers, a narrow-scale warning, overflow, the Margin label.
8. Verify with test-cases.md and `scripts/` (README). No sign-in in automated tests, and no real payments.
9. Wording: "Professional Tools" / "Premium Applications" / "Workflow Products" and "trial uses". Keep the reserved ad slots and the intentional badge.
