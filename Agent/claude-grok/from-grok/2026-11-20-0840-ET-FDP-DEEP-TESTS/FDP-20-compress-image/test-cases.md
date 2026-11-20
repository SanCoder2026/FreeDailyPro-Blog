Sent: 2026-11-20 08:40 ET

# FDP-20 Compress Image: test cases for after the fix

| ID | Steps | Expected |
|---|---|---|
| CI-01 | photo.jpg → Medium | ≥25 % smaller, same pixels, no EXIF/GPS |
| CI-02 | photo.jpg → Strong | ≥50 % smaller |
| CI-03 | already-compressed JPG (q40) → Strong | target met, and a note if quality is now very low |
| CI-04 | small_gps.jpg → Custom Target 200 KB | returned file has **no GPS**, or the line says location data is kept |
| CI-05 | small_gps.jpg → Manual 100 % | same as CI-04 |
| CI-06 | photo.jpg → preset 1 MB | ≤ 1,000,000 bytes, line shows bytes |
| CI-07 | photo.jpg → 100 KB | ≤ 100,000 bytes |
| CI-08 | photo.jpg → 200 KB | result looks reasonable (not q≈0.13 at 12 MP) or a quality warning |
| CI-09 | photo.jpg → 200 KB + Don't change dimensions | same pixels; target missed message if needed |
| CI-10 | anim.gif → Medium | warning that animation is lost (or pointer to GIF tool) |
| CI-11 | logo.png (transparent) → Medium | WebP, transparency kept |
| CI-12 | vector.svg | returned unchanged with message |
| CI-13 | notimage.jpg | "could not be read as an image" |
| CI-14 | Target 0 / −5 / empty | inline error under the field, `aria-invalid`, toast |
| CI-15 | Screen reader | target field and unit named; mode state announced; result announced |
| CI-16 | Meta, FAQ, JSON-LD, Details, YouTube description | only the 4 live modes; no "Light/10 %"; no "free" |
| CI-17 | Video | current UI, no "free" caption, short outro |
| CI-18 | Several files ×6 | 5 kept with notice; ZIP costs 1 use |
| CI-19 | With uses left: single Download ×2 | cost per download recorded; name `compressed_<name>.<ext>`; bytes = result |
| CI-20 | iPhone SE | Compress reachable without 2–3 screens of scrolling; no overflow |
