Sent: 2026-11-21 23:35 ET

# Placement on rotated and cropped pages

`qe`: `x = fx * page.getWidth()`, `y = h - (fy + fh) * h` with `getSize()` = MediaBox size, ignoring `/Rotate` and the CropBox origin. The preview is rendered by pdf.js (rotation and CropBox applied).

- rotated.pdf (/Rotate 90, displayed 792×612): field placed 25 %/25 % → rect [83.9, 578.0, 223.7, 607.3] in unrotated space → shows as a vertical 29×140 box at the right of the displayed page. screens/rot-preview-vs-output.
- cropbox.pdf (CropBox 100,100–512,692): field placed 25 %/25 % → rect x 19.7–287.9 (visible x starts at 100) → half off-page, over the heading, 268 pt wide. screens/crop-preview-vs-output.
