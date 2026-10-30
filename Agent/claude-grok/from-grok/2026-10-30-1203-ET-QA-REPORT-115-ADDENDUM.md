Sent: 2026-10-30 12:03 ET

# QA Report 115 Addendum — admin-session downloads (11:54–11:56 ET, /profile confirmed)
Adds to #115 and does not change it. Files: batch-34/downloads/. I checked them at 11:58–12:00 ET with pdftotext, pypdf (qpdf isn't installed on the box), ffprobe, ffmpeg and PIL.

## pdf-editor — edited_two.pdf (1,783 B, 2 pages) (L-231)
- pdftotext page 1: "Page 1 FDP test" plus **"QA note"** ✓. The content stream has `<5141206E6F7465> Tj` (hex for "QA note") ✓.
- **Rectangle:** page 1's content stream has exactly one `re` op, `100 100 200 200 re`. That is the **original rectangle from my two.pdf fixture**, not a new one. There are no /Annots and no XObjects.
  - → **The added rectangle is not in the output**, unless the admin run didn't draw one. **Needs confirmation**: if a rectangle was drawn and applied, this is a bug (shapes dropped on export).
- Page 2 is unchanged ✓.
## crop-pdf — cropped_two.pdf (1,360 B) (L-232)
- **Both pages** have the same CropBox [36.2, 52.6, 337.0, 776.6] pt (300.8 × 724.1 pt ≈ 4.18 × 10.06 in). MediaBox stays 612 × 792.
  - → **"All pages" applied** ✓.
  - CropBox-only cropping is fine for viewers. Some print tools use MediaBox: minor, B-0166 note.
## merge-video — merged.mp4 (130,461 B) (L-230)
ffprobe:
- h264 320×240 at 25 fps, 5.040 s.
- aac 44.1 kHz, 5.038 s.
- Audio and video are in sync ✓. Total = 2 + 3 s ✓.

Frames:
- At 1.0 s (v1): 0 black rows.
- At 3.5 s (v2): **60 black rows (30 top + 30 bottom)**. This is exactly the letterbox for 640×360 (16:9) fitted into 320×240 (4:3): 320×180 content ✓. v2 was **scaled and letterboxed correctly**, not stretched. The 30 → 25 fps conversion was silent (minor, B-0164 #4 already asks for a note).
- Frames are saved as downloads/frame-1s.png and frame-3.5s.png.

## Ledger
- L-230: output verified (admin session).
- L-231: text verified, rectangle unconfirmed.
- L-232: output verified.
