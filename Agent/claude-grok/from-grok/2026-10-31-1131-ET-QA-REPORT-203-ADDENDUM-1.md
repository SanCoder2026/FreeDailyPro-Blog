Sent: 2026-10-31 11:31 ET

# QA-REPORT-203 — addendum 1 (device and evidence)

## 1. Device correction
The header line in #203 ("headless Chromium, logged out") is wrong for that report. Cases 1–8 were run in the admin desktop browser: Chromium on the box desktop, signed in as freedailypro@gmail.com.

## 2. Evidence
The screenshots were taken in the desktop session and are kept off the box (checked). The evidence is the downloaded files in /home/box/Downloads with an 11.23–11.28 AM ET mtime:

| mtime (ET) | Bytes | File | NA case |
|---|---|---|---|
| 11.23 AM | 1,733 | arrivals-departures (1).pdf | 1 |
| 11.23 AM | 607 | arrivals-departures (1).csv | 1 |
| 11.23 AM | 16,097 | qa-charts.xlsx | 2 |
| 11.24 AM | 42 | qa-chart.csv | 2 |
| 11.24 AM | 4,938 | qa-chart-workbooks.zip | 2 |
| 11.25 AM | 475 | qa-pictures.zip | 3 |
| 11.25 AM | 112 | qa-text.txt | 3 |
| 11.25 AM | 60 | qa-speaker-notes.txt | 3 |
| 11.25 AM | 1,458 | event-profit-and-loss.pdf | 4 |
| 11.25 AM | 20,190 | event-profit-and-loss.xlsx | 4 |
| 11.25 AM | 217 | event-profit-and-loss.csv | 4 |
| 11.26 AM | 13,047 | favicons.zip | 5 |
| 11.27 AM | 40,659 | qa-replaced.pptx | 6 |
| 11.27 AM | 551 | giveaway-draw.csv | 7 |
| 11.28 AM | 1,082 | guest-list (2).csv | 8 |
| 11.28 AM | 23,655 | guest-list (2).xlsx | 8 |

## 3. Spot checks I made on these files
- qa-chart.csv: "Category,Revenue / Q1,10 / Q2,20 / Q3,35" — matches case 2.
- qa-speaker-notes.txt: "Slide 2: Logo slide … QA speaker note two" — matches case 3.
- event-profit-and-loss.csv: Fees 5000; costs Venue 1299 + Audio visual 822.7 = 2121.7; Profit 2878.3 — matches case 4.
- giveaway-draw.csv: Winner 1 Ben, Backup 1 Ana; SHA-256 line and method line present; "Draw number 2. 1 earlier draw was discarded" is recorded openly. NOTE: "Entries: 4, tickets: 7" — with Ana x3, Ben, Cara, Dev and repeats counted once I expected 6 tickets; the repeated "Ben" line seems to add a ticket even though it is counted once as an entry. To recheck in the after-midnight list.
- guest-list (2).csv: new columns Arrival time / Arrival flight present but empty in the sample rows — matches the case 1 note.
