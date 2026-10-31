Sent: 2026-10-31 11:44 ET

# NEEDS-ADMIN addendum 6 (rows 54–62)

| # | Tool | URL | Input | What to check |
|---|---|---|---|---|
| 54 | Regex Tester | /tool/regex-tester | pattern `(\d{3})-(\d{4})`, flag g, text "call 555-1234 or 555-9876" | 2 matches, group 1 = 555, replace preview `$2` works |
| 55 | Rental Application Maker | /tool/rental-application-maker | landlord name, property address, all sections on | PDF has applicant, employment, income, references, consent and signature lines |
| 56 | Repair PowerPoint File | /tool/repair-powerpoint | qa.pptx truncated by 1 KB | repaired file opens; slides kept; clear message if it cannot be repaired |
| 57 | Replace Fonts in PowerPoint | /tool/replace-fonts-powerpoint | qa.pptx, Calibri to Arial | font list detected; output uses Arial on every slide |
| 58 | Resize PowerPoint Slides | /tool/resize-slides | qa.pptx 16:9 to 4:3, fit | slide size 10x7.5 in; content scaled, not cropped |
| 59 | Resume / CV Builder | /tool/resume-builder | 2 jobs, 1 degree, 6 skills | PDF text selectable (ATS), one page, matches preview |
| 60 | Resume Keyword Matcher | /tool/resume-keyword-matcher | resume text with "Python, SQL"; posting asking for "Python, SQL, Tableau" | Tableau listed as unmatched; match score about 67% |
| 61 | Reverse Video | /tool/reverse-video | a short clip with sound (small.mp4 is silent) | output plays backwards; same length; audio option behaves |
| 62 | Schema Markup Generator | /tool/schema-generator | FAQ type, 2 questions | JSON-LD valid in Google Rich Results test |
