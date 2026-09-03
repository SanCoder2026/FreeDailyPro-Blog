# MultiTool App hero images (replace icon placeholders)

## Context
These MultiTool Apps use `MultiToolAppHero` with `heroImage` from `client/src/lib/multitool-apps-data.ts`.

| Tool | Current (placeholder) | New hero |
|------|------------------------|----------|
| magazine-maker | `/blog/magazine-maker-launch.webp` (already good) | keep |
| book-maker | `/blog/book-maker-launch.webp` (already good) | keep |
| **document-scanner** | `/icons/multitool/document-scanner/icon-512.png` | `document-scanner-launch.webp` |
| **catalog-maker** | `/icons/multitool/catalog-maker/icon-512.png` | `catalog-maker-launch.webp` |
| **resume-builder** | `/icons/multitool/resume-builder/icon-512.png` | `resume-builder-launch.webp` |
| **universal-file-converter** | placeholder / none | `universal-file-converter-launch.webp` |

## Specs
- 1200 × 630 WebP, branded FreeDailyPro bottom stripe, <150 kB
- Topic-clear UI on laptop + human + emotion (matches book/magazine launch style)

## Wire-up (FreeDailyPro repo)

1. Copy files into the site:
   ```
   client/public/blog/document-scanner-launch.webp
   client/public/blog/catalog-maker-launch.webp
   client/public/blog/resume-builder-launch.webp
   client/public/blog/universal-file-converter-launch.webp
   ```

2. Update `client/src/lib/multitool-apps-data.ts`:
   ```ts
   "document-scanner": {
     heroImage: "/blog/document-scanner-launch.webp",
     ...
   },
   "catalog-maker": {
     heroImage: "/blog/catalog-maker-launch.webp",
     ...
   },
   "resume-builder": {
     heroImage: "/blog/resume-builder-launch.webp",
     ...
   },
   "universal-file-converter": {
     heroImage: "/blog/universal-file-converter-launch.webp",
     ...
   },
   ```

## Tool page details used for each image
- **Document Scanner**: photo → edge crop / straighten / enhance → clean scan PDF
- **Catalog Maker**: product photos + prices + categories → cover + TOC catalog PDF
- **Resume Builder**: section-by-section ATS-friendly resume → live preview → PDF
- **Universal File Converter**: drop any file → every real target format (images, PDF, Excel, PowerPoint, text); hero shows multiple symbolic pairs (PDF→DOCX, PNG→JPG, XLSX→CSV, MP4→GIF, PPTX→PDF, HEIC→PNG, JSON→YAML, …)
