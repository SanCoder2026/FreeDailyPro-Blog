Sent: 2026-11-20 08:40 ET

# Desk findings (page copy, JSON-LD, code)

- Title "File Converter – Convert Any File, No Upload | FreeDailyPro"; meta "…in your browser… Nothing is uploaded."; chip "Files never stored"; on-page note "Files are converted in your browser and are not uploaded."
- FAQ "Are my files uploaded to a server?" → "Nothing is uploaded anywhere." FAQ "Are my files uploaded?" → "…your document contents are not sent." Privacy (Details) repeats it. All untrue for presentation conversions using `legacyDeck` (old formats, and any → .odp). (`html/tool-expanded.txt` L10, 61, 89–94, 130)
- Format table L56: "PowerPoint presentation (.ppt .pptx .pps .odp .key)"; accept list `Os` (UniversalFileConverter L223) = .jpg .jpeg .png .webp .heic .pdf .txt .html .htm .md .xlsx .xls .csv .ppt .pptx .doc .docx — no .pps/.odp/.key/.ppsx/.potx even though `universalCore`/`legacyDeck` handle them.
- Compression: FAQ "four modes: Balanced/Aggressive/Extreme/Target size"; Tips "Try PDF compression at Light before Strong"; UI Recommended/Medium/Strong.
- "How to use this app" lists only images, PDF, text, spreadsheet and PowerPoint (no Word, HTML, Markdown, CSV).
- Limitations: ".doc accepted by name but must really be .docx" — the UI still offers targets and fails generically.
- About: "Nothing is offered that isn't actually implemented" / "never a dead-end option" — .pptx → .pptx target contradicts.
- H1 "File Converter — Convert Any File Online"; breadcrumb "Universal File Converter"; category PDF Tools; breadcrumb section Premium Applications; blog/video "MultiTool Apps".
- Hero illustration: mock UI "Convert files between 100+ formats", MP4→GIF, JSON→YAML, "Convert All", 62% progress — not this tool.
- Blog /blog/universal-file-converter (Sep 22, 2026): honest "~30 conversions"; mentions Multiple files up to 20.
- tools.csv: Premium Application, PDF Tools; outputs JPG/PDF/PNG/WEBP; share/save/my-files/cloud; gated. C05 duplicate cluster with convert-image hub and file-conversion-studio (Workflow).
