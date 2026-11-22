Sent: 2026-11-22 03:49 ET

# FDP-95 findings: page copy, blog, video, SEO, locales

## Page claims checked live
| Claim | Live | Verdict |
|---|---|---|
| "Bookmarks follow their pages, a bookmark for a removed page is dropped" | Follow ✓; parent "Part B p5" re-pointed to p6; named-dest bookmark dropped; /XYZ → /Fit | P2 #4 |
| "fillable form fields remain fillable"; duplicates renamed with a number | ✓ (`name_2` …, values copied) | PASS |
| "Each press adds 90 degrees clockwise … a display setting, not a redraw" | ✓ /Rotate only, inherited included | PASS |
| "Save Changes is disabled once every page has been removed" | ✓ | PASS |
| "Will this work on a password-protected PDF? Yes" vs Limitations "Password-protected PDFs cannot be read" | unlock works | P3 #7a |
| "brought back with Undo Remove" | button is "Undo" | P3 #7b |
| "doesn't alter the content of any individual page" / "copied across as they are" | drawn content same; links broken | P3 #7c (+P1 #2) |
| Organize doesn't add other files; use Merge first | ✓ no second-file input | PASS (disclosed) |
| "A blank page takes the size of the page before it" | ✓ | PASS |
| "No page, thumbnail or edit list is transmitted" | only usage.log POST seen | PASS |

## Blog
- /blog/organize-pdf (1,217 words): the 12-page backwards-scan scenario; steps match the UI (Reverse, rotate, checkboxes, "3 (was 11)", -organized). Repeats the bookmark claim.
- /blog/redact-organize-pdf-sensitive (Sept 9 2026): "Organize pages so sensitive appendices are removed entirely"; "dropping privileged pages" (P2 #6). Meta "Free PDF redaction and page organization"; "Monthly Pro"; heading HTML `FreeDailyPro&amp;#39;s` shows as `&#39;` (P3 #8).

## Video TZTL_wd-NJY
- "How to Use Organize PDF – Free Step-by-Step Walkthrough", 2:19, uploaded 2026-09-24 02:57 ET (YouTube shows 2026-09-23T23:57:54-07:00), 1 view.
- Description: "Try Organize PDF free", "Free daily uses in your browser, no account needed", "Subscribe for the next free tool". Thumbnail "FREE · PRIVATE · NO LOGIN".
- Storyboard (8 sheets, video/sb-contact.jpg): intro card, the current thumbnail grid UI, edits, presenter outro "Thanks for watching!". The UI matches today's.
- yt-dlp is bot-blocked on this box; storyboard and watch-page metadata were used.

## SEO
Title "Reorder or Remove PDF Pages Online - Visual Editor | FreeDailyPro"; meta "Reorder or remove pages using real page previews." (49); canonical self; hreflang en/es/pt/fr/de/ja/hi/zh/ko/id + x-default; og:image og-default.png; H1 "Reorder or Remove PDF Pages"; JSON-LD WebSite, SoftwareApplication (9.99 USD /MON), VideoObject "How to Reorder or Remove PDF Pages Online with Previews", FAQPage, BreadcrumbList; 1 empty-alt image.

## Locales (de, ja loaded with a file)
H1 "PDF Organisieren" / "PDF整理", breadcrumb, strip and Quick Buy are translated. Strapline, "Runs on your device", the Premium line, the drop zone, the tool buttons, the aria labels, the accordion headings, the title and the meta are English. /ar → 404.
