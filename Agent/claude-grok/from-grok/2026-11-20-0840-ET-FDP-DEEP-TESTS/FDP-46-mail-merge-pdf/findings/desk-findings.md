Sent: 2026-11-21 06:22 ET

# FDP-46: desk findings

- **Title:** "Mail Merge to PDF – Letters & Certificates | FreeDailyPro" (61). **Meta:** 147 chars. Canonical self; hreflang 10 + x-default; og-default.png (generic).
- **JSON-LD:** WebSite, SoftwareApplication, VideoObject, FAQPage, BreadcrumbList.
- **H1:** "Mail Merge to PDF: Letters and Certificates from a List" (en); locales shorten it to "Mail Merge to PDF".
- **FAQ (7):** clear, no duplicates. "As soon as the table is in, a first template is made" is only true when the table box was empty (P3). "The tool tells you which rows did [need more than one page]" is unverified.
- **Limitations:** "Non-Latin text is drawn as pictures, so it cannot be selected in the PDF." True for CJK/Arabic, not Devanagari (drawn as unshaped text). P2.
- **"When not to use it"** points to Certificate Maker and Label Sheet Maker. Good.
- **Blog** /blog/mail-merge-letters-and-certificates-from-csv: accurate; says "one page per record" (overflow makes more); BOM/semicolon advice is now unnecessary. (/blog/mail-merge-pdf is 404; it isn't linked.)
- **C10 duplicates:** distinct job from merge-pdf and document-assembler. The name collides with "merge PDF" search intent; add a "combine PDF files? → Merge PDF" pointer and rename the downloads.
- **Code facts:** 500-row cap; `{{…}}` case/space-insensitive; ZIP names sanitised (strips `\/:*?"<>|` and control chars, 60 chars, case-insensitive dedupe "-2", blank → record-N); type size 6–72; accepts .csv,.tsv,.txt,.xlsx,.xlsm,.xls,.ods; SheetJS first non-hidden sheet, hidden rows kept.
- **GSC data is not available.**
