Sent: 2026-11-20 08:40 ET

# FDP-08 bulk-qr: live functional findings

- **Written:** 2026-11-19 12:55:24 EST (box `date`, ET). Live window 2026-11-19 12:37–13:00 EST. Headless Playwright (Chromium) in guest contexts, no sign-in, no card or email entered, no ad clicks.
- Counters are **display-only** evidence: the strip text and localStorage `fdp-usage-v1`. No backend claims.

## Starting state (fresh contexts, Professional scope, limit 10)
- At 0 remaining: probe, explore, kbd, sample-key ×2 and the battery dry run A/B/C/E, then the battery real run A/B/E/C ×2 (contexts that load at 0 skip themselves).
- At **10 remaining**: the battery dry-run D context and the battery real-run D context.
- So 2 of about 17 readable fresh Chromium contexts loaded with uses. The matrix's starting counts are in `devices-locales-findings.md`.

## Previews (free; usageToday never changed)
14 list scenarios plus the sample passes. Preview images decoded with zxing-cpp (`json/decoded.json`, `previews/`).
- **PASS:**
  - S02 URLs and text. S05 **Unicode** (Grüße 日本 👍, Arabic, Cyrillic) decodes exactly.
  - S03 blanks and duplicates: "2 QR codes will be generated (2 duplicate lines skipped)".
  - S06 510 lines: "500 … Only the first 500 of your 510…" and "+488 more".
  - S07 301 characters: long-value warning shown, and it decodes.
  - S09 low contrast (1.6:1) and S10 inverted warnings.
  - S11 SVG disables the PNG size menu.
  - S12 WiFi/vCard/mailto/formula/"-5+3" payloads are encoded literally.
  - S14 EC H. S13 shows a 12-image preview and "+8 more".
  - Empty input: 0 codes, Generate disabled.
  - Preview images have alt "QR for <value>".
- **FAIL / PARTIAL:**
  - **S08:** one 3,000-character line makes the whole preview disappear (0 images, including the valid line), yet the counter still says "2 QR codes will be generated" and Generate stays enabled. By code, Generate then fails the whole batch with "Generation failed" (not run: no uses). The user isn't told which line is the problem.
  - **S04 name mode:** "Table 1,…/menu" and "Table 2,…/menu" both point to the same URL, and the second is dropped as a duplicate, so its named file is never made. "OnlyName," encodes "OnlyName," literally.

## Guest passes and project
- "Guest passes from my project (0)" until "Try a sample", which loads 8 guests. "Confirmed and attended guests" gives 5 passes.
- Pass previews decode as `FDP1.<tag>.g_sampleNN.<sig>`. There is a different random key per context (`json/sample-key.json`).
- **Open project** with broken files shows clear toasts: "That isn't a project file (it isn't valid JSON)." and "That isn't a FreeDailyPro project file."
- "New project" asks for confirmation ("The open one is cleared unless you saved it").

## Downloads (battery, real; display-only counts)
| Ctx | Step | Strip before → after | Result |
|---|---|---|---|
| D | Generate ZIP, 5 guest passes | 10 → 9 | qr-codes.zip 57,272 B. 5 PNGs 600×600, **4-module quiet zone (3.99)**, EC M, no mark. All decode. **5/5 signatures verify** against the saved key. index.csv has file,name,value with guest names. |
| D | Save project | 9 → 9 (free) | Sample-offsite.fdp-project.json 9,909 B. Holds the pass key **and** guest emails, dietary needs, rooms, vendors, quotes and expenses. |
| A, B, C, E | – | – | **Skipped**: the fresh contexts loaded at 0. **Needs re-run after midnight UTC.** |

## Cap dialogs (at 0)
- **Generate ZIP** shows "You've used today's trial uses… Monthly $4.99… Day Pass $1… removes the 'Created with FreeDailyPro.com' mark from your PDFs and images." The test stopped there.
  - The mark claim doesn't apply here: the trial PNG has no mark.
- **Save project at 0 is also blocked** ("Today's trial uses are done | Your input stays where it is, but downloading needs a pass").
  - With uses left, Save was free (D2).
  - So a capped user who built a guest list (or opened the sample and edited it) cannot keep the project or its pass key. The project is "kept in this tab only, then erased", and passes already printed from it can no longer be verified once the tab closes.

## Sign-in
- Nothing in the visible tool needs sign-in.
- The ProjectBar bundle has Event Suite features: saved projects "from any device", publish to Guest/Door apps, email and text invites. These appear only with an Event Suite plan.
  - So the Event Suite parts are **untested (needs sign-in + plan)** via https://www.freedailypro.com/pricing (Event Suite).
- Nothing on the bulk-qr page itself blocked on sign-in.
