Sent: 2026-10-30 14:58 ET

# B-0281 Blind CV Redactor: redacted file out, and clearer coverage
Priority: P3 · Estimated effort: M · Report: QA-REPORT-151 · Source: live probe 2026-10-30 ~14:55 ET (headless, logged out) + live competitor search

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Let a recruiter go from a candidate's resume file to a shareable blind copy in one step, with confidence about what was removed.

## Why
Live check: name "Maria Gonzalez" + text with email, phone, "She…" and 2015-2020 → "4 items removed: name 1, email addresses 1, phone numbers 1, gender and family words 1"; years left in by default (documented option). Output is copy or .txt only. Competitors Formatix.AI and NullifyCV return a redacted PDF/Word file; KeptPDF flattens redacted PDF pages; Formatix offers they/them pronoun replacement; NullifyCV handles batches of files. Title 63 chars (over 60); meta 130.
The page showed "0 remaining today" in a fresh session yet the redaction still ran — trial counter mismatch, filed under B-0156.

## Who uses this
Recruiters and hiring managers running blind first-round screening.

## Outcomes (ranked)
1. Download the blind copy as .docx/PDF when the input was a file.
2. Option to replace gendered pronouns with they/them instead of deleting them (sentences stay readable).
3. Batch: several resumes in, one zip out.
4. Snippet rewrite.

## SEO
- Now: title "Blind CV Redactor: Anonymize a Resume for Review | FreeDailyPro" (63); meta 130; H1 "Blind CV Redactor".
- Keywords: blind cv, anonymize resume, cv anonymiser, redact resume.
- Suggested Title: "Blind CV Redactor – Anonymize a Resume | FreeDailyPro" (53)
- Suggested Meta: "Remove names, emails, phones, links, addresses, birth dates and gender words from resume text for a blind first review. Choose what to strip, in your browser." (158)
- Suggested H1: "Blind CV Redactor – Anonymize a Resume"
- FAQ: Is my resume uploaded? · Does it read scanned PDFs? · Should years be removed? · What about school names?

## Constraints
Text stays in the browser. Trial gating unchanged.

## Test cases
1. Sample above → same 4 removals (regression); years option on → 2015-2020 removed.
2. Text PDF in → redacted PDF out, no hidden text recoverable.
3. Pronoun mode → "She led" becomes "They led".
4. Trial counter matches the gate (B-0156).
5. Title ≤60, meta 140–160; 390 px no overflow.
