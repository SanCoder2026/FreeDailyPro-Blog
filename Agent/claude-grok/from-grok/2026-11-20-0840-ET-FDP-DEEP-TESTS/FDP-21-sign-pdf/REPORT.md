Sent: 2026-11-20 08:40 ET

# FDP-21 Sign PDF (sign-pdf): deep test report for Claude

- **Written:** 2026-11-19 17:25:28 EST (box `date`, ET).
- **Tool:** https://www.freedailypro.com/tool/sign-pdf. Row 21 of TEST-ORDER.md: Premium, PDF Tools, test-plan rank 18 (126 views), duplicate cluster C08. **GSC data is not available.**
- **Classification:** Premium Application (2 trial uses a day, $3 day pass / $9.99 month), PDF Tools (+ premium-apps, paralegals solution). Gated at Download; placing fields is free.
- **Testers:**
  - **Desk review:** page (expanded), JSON-LD, /es, /ar, blog /blog/sign-pdf, category; `SignPdf` code.
  - **YouTube video:** metadata + 68 frames.
  - **Headless Playwright:** 16 PDF × field cases + other-party round trip + image import (outputs inspected with pypdf/pdftoppm), gate and dialogs, keyboard, axe, phones (tap placement), Firefox + WebKit, matrix (10 profiles, 10 locales + /ar, 6 geos, axe).
- **Starting counts:** most contexts 2/2 used (0 remaining) at 17:05:22 EST; about 1 in 4 loaded with 2 remaining. Counters are display-only evidence.
- **Trial use observed:** with uses left, the first Download Signed PDF cost 1 (0 → 1) and a second Download of the same work was free (1 → 1); bytes identical to the in-memory PDF; no "Created with FreeDailyPro.com" mark. Consistent with the Oct 30 policy (results count).
- **Constraints kept:** guest only, no sign-in, nothing typed into email/card prompts, no ad clicks, no API/MCP, no site/repo changes. Downloaded PDFs were only parsed, never executed.
- **Sign-in:** "Open from Google Drive" not clicked (Google sign-in). No save/cloud option exists on this tool (live-verified). See INSTRUCTIONS.md.
- **Pending:** none for the trial count. Not run: S11 (existing AcroForm PDF) — the contexts that loaded with uses were kept for the count check. No RERUN-AFTER-RESET row needed.

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect the code, restate the problem, push back where we're wrong, and choose fixes that fit how FreeDailyPro ships PDF tools.

Code to look at (`evidence/js/SignPdf.pretty.js`): other-party fields L698–712 (`createTextField`); signing record `ta()` L113–170; Download handler `Ft` L646–815; preview canvas L1410–1460 (click-only placement); signature-style buttons (`aria-pressed`, name from text, style only in `title`); FAQ/Limitations copy lives with the tool info.

After you ship, rerun `scripts/sp-battery.js all`, `scripts/sp-gate.js`, `scripts/sp-otherparty.js`, then `test-cases.md` (SP-01…SP-16).

## Intent

Someone has a lease, an offer letter or a client agreement and needs it signed today without printing and scanning. They want a signature that looks like theirs, in the right spot, and — when someone else must sign too — a file that person can actually complete. They need to trust what the page tells them about what the other person will see. They should leave impressed and see the Premium pass as worth it.

The engine is strong: three signature methods, six script styles, initials, dates in two formats, all pages or a range, rotated pages handled, other-party fields that really work (pre-placed when the file comes back), an honest signing-record page with a correct SHA-256, clear inline errors, password and damaged-file handling, and the same result in Chromium, Firefox and WebKit.

Trust is lost where the page explains the other party's experience in two opposite ways, where keyboard users cannot place a field at all, and in a video that sells a free Pro tool at 0 uses.

## Why: what the evidence says

- **P1: the copy contradicts itself about other-party fields.** The output has real AcroForm text fields (S02: `fdp_signature_1_other`, `fdp_date_2_other`), and About, the note under Download and the success toast say they can be filled "in any PDF reader". The FAQ ("a labeled placeholder, not a fillable box"), Details → Limitations ("aren't fillable PDF form fields… the other party needs to use this tool") and the blog say the opposite. The multi-party copy also promises the other party gets real signing tools "rather than a plain unverified text box", but in any other reader the signature field is a plain text box.
- **P1: keyboard-only users cannot sign.** Fields are placed only by clicking or tapping the preview canvas; the canvas isn't focusable and there are no X/Y inputs, so the core task cannot be completed without a pointer (WCAG 2.1.1).
- **P1: the video shows an older tool as free.** "SIGN A PDF FREE ONLINE · FREE", "10 free uses daily" and "Pro" badges (now Premium, 2 trial uses), a "0 free uses remaining today" banner on screen the whole time, no style picker or signing record, and it never shows a signed PDF being downloaded. 205 s with a mid-walkthrough subscribe cut.
- **P2 (selected; full list in PRIORITIES.md):** signature-style buttons all announce "Jane Q. Public"; unnamed draw pads; radios without a group name; no live region; field table overflows on phones and Download is 4+ screens down on iPhone SE; faint Date/Name text in the preview.

## Outcomes we want

1. Every place that describes the other party's fields (FAQ, Limitations, blog, About, toast, note) says the same true thing: real form fields any reader can fill with typed text, or open here to draw/import a signature.
2. A keyboard-only user can add, place, move and download every field type.
3. The video shows today's Premium tool with trial-use wording and ends with a downloaded signed PDF.
4. Screen-reader users hear which signature style is selected and what happened after Download.
5. On a phone, Download is reachable without scrolling through the whole page.

## The 22 checks

| # | Check | Result | Severity | Evidence |
|---|---|---|---|---|
| 1 | Capability | **PASS** | — | All placement, method, page-range, rotation, record and round-trip cases correct. `findings/live-functional-findings.md`, `testfiles/out-*.pdf` |
| 2 | Completeness | **PARTIAL** | LOW | Missing: signature reuse between visits (documented), keyboard placement, save/share options listed in tools.csv. |
| 3 | Ease of use | **PARTIAL** | MEDIUM | Clear steps and inline errors; faint preview text; long page on phones; keyboard users blocked. |
| 4 | Layout | **PASS** | LOW | Clean on 10 profiles; 9 px header overflow at 320 px (site-wide); field table overflows on phones. |
| 5 | Payment process | **PASS** | — | At 0: Download → "Today's trial uses are done" → Premium Day Pass $3 → email prompt (stopped; nothing typed). Work kept after Escape. `json/gate-kbd.json`, `screens/live/dlg-*.png` |
| 6 | Information correct | **FAIL** | HIGH | Other-party field copy contradicts itself and the output. `findings/desk-findings.md` |
| 7 | Indexing | **PASS** | — | 200, self-canonical, in sitemap, not noindex. GSC data is not available. |
| 8 | SEO | **PARTIAL** | LOW | Good title/meta with trial wording, FAQPage + VideoObject. Locale titles in English; /ar 404. |
| 9 | Blog | **PARTIAL** | MEDIUM | /blog/sign-pdf (Oct 17, 2026) is useful but repeats the wrong "not fillable in a standard reader" claim. |
| 10 | YouTube video | **PASS (low reach)** | LOW | bP3uV1CNIwM embedded; 205 s, 4 views. |
| 11 | FAQ / guide | **PARTIAL** | MEDIUM | 10 FAQs + Details, honest about certified signatures; wrong on other-party fields. |
| 12 | Video shows current tool | **FAIL** | MEDIUM | Old UI, "free"/"Pro"/"10 free uses daily", 0-uses banner, no final download. `findings/video-findings.md` |
| 13 | Storage | **PARTIAL (sign-in)** | — | Open from Google Drive needs Google sign-in (not clicked). No save-to-Drive/cloud on this tool (live-verified). |
| 14 | Sharing | **N/A** | — | No share-result button; "Share this tool" is site-wide. Absent although tools.csv lists share/copy/print (live-verified). |
| 15 | Downloads | **PASS** | — | `signed-contract.pdf`, bytes = in-memory PDF; no mark on trial output. |
| 16 | Usage count | **PASS** | — | Placing fields free; 1st Download 0 → 1; 2nd Download of the same work free. Counter display-only evidence. |
| 17 | Category placement | **PASS** | — | PDF Tools; premium-apps; paralegals solution. |
| 18 | Site section | **PASS** | — | Correct. |
| 19 | AI need / demand | **PASS** | — | Rank 18, 126 views; 10 posts link here. GSC data is not available. |
| 20 | Merge candidate | **N/A (keep)** | — | C08 cluster tools do different jobs; Flatten PDF is a good next step after signing. |
| 21 | Remove? | **N/A (keep)** | — | Core Premium Application. |
| 22 | Duplicates | **PASS** | — | C08: keep; naming issue is fillable-forms vs create-fillable-pdf, not this tool. |
