Sent: 2026-10-30 14:58 ET

# B-0279 Bill of Sale Generator: sale date, parties' addresses and a fuller vehicle record
Priority: P2 · Estimated effort: M · Report: QA-REPORT-151 · Source: live probe 2026-10-30 ~14:55 ET (headless, logged out) + live competitor search

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Produce a bill of sale that a buyer and seller can actually sign and file for a private car or item sale, and a snippet that wins searches for "bill of sale".

## Why
The form asks only for seller name, buyer name, item description, price, optional state and notes, plus a "motor vehicle" checkbox (VIN and odometer). Live top-5 results (PDFforBiz, FormBarn, OnPDF, utilhq) all collect date and place of sale and the parties' addresses, validate the 17-character VIN, and print the federal odometer disclosure (49 CFR 580) with its three certifications and a buyer acknowledgment. Meta is 51 characters.

## Who uses this
Private sellers of cars, motorcycles, boats, furniture and equipment.

## Outcomes (ranked)
1. Date of sale, place of sale, and buyer/seller addresses on the form and document.
2. Vehicle mode: separate year/make/model/body/VIN fields, 17-character VIN check, odometer reading with the three federal certifications and buyer acknowledgment.
3. "As-is" / warranty choice and price printed in words and figures.
4. Snippet rewrite; /es title localised if served in English (L-189).

## SEO
- Now: title "Bill of Sale Template Online - Generator | FreeDailyPro" (55); meta 51; H1 "Bill of Sale Generator".
- Keywords: bill of sale, car bill of sale, vehicle bill of sale, bill of sale template.
- Suggested Title: "Bill of Sale Generator – Car or Item, PDF | FreeDailyPro" (56)
- Suggested Meta: "Create a bill of sale for a car or any item: buyer, seller, price, VIN and odometer disclosure. Preview it, then download a Word or PDF file in your browser." (157)
- Suggested H1: "Bill of Sale Generator – Vehicle or Item"
- FAQ: Does a bill of sale need a notary? · When is an odometer disclosure required? · Is it "as is"? · What if a lender holds the title?

## Constraints
Keep the not-legal-advice notice. Download gating unchanged.

## Test cases
1. Required fields empty → Preview/Word/PDF blocked with the existing message.
2. Vehicle mode, VIN of 16 characters → inline error; 17 valid characters → accepted.
3. Odometer 45,000 + "actual mileage" → PDF shows reading, certification and buyer acknowledgment line.
4. Date and addresses appear in Preview, Word and PDF identically.
5. Meta 140–160; 390 px no overflow.
