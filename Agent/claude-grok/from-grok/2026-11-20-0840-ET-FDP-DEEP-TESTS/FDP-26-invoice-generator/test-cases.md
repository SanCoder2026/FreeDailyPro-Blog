Sent: 2026-11-20 22:15 ET

# FDP-26 Invoice Generator: test cases (guest, fresh context)

| ID | Input | Action | Expected after fix |
|---|---|---|---|
| IG-01 | Sample invoice | Total box | $1,754.46 / balance $1,654.46 |
| IG-02 | 3 tax rates, 10% discount | Total box | $243.44 |
| IG-03 | Credit line larger than work | Total box/PDF | −$33.00 with subtotal/tax lines shown |
| IG-04 | "1,5" × "1.234,56" | Total | 1,851.84 |
| IG-05 | Unit price "1.500" | Total | 1,500 or a clear hint |
| IG-06 | Paid > total | PDF | Balance −$50.00 |
| IG-07 | Discount 150 | Generate | Behaviour matches FAQ |
| IG-08 | Late fee 1.5% + $25 after 10 days | PDF | Wording + "(2026-12-29)" + amount |
| IG-09 | Missing business/client, qty 0, bad pay link, due < date | Generate | Field messages, focus to first bad field incl. line items |
| IG-10 | Rich INR invoice (Hindi, Arabic, Greek, emoji, logo, QR) | PDF | All totals; Hindi/Arabic correct; notes order kept |
| IG-11 | Same invoice | PDF then Word then Excel | Same invoice number on all three |
| IG-12 | 23 lines / 4 rates, A4 | PDF | Totals + Balance due clear of the footer |
| IG-13 | 40 lines / 8 rates | PDF | No totals row off the page |
| IG-14 | AED + Arabic line + Arabic notes | PDF | Correct |
| IG-15 | Excel of IG-02 | Open | Tax total equals PDF |
| IG-16 | Save profile with uses | Save | Policy-consistent cost; file has clients + numbering |
| IG-17 | Save profile at the cap | Save | Works or the toast doesn't promise it |
| IG-18 | Load bad JSON / junk CSV / formula CSV | Load/Import | Clear messages; formulas shown as text |
| IG-19 | At 0 remaining | PDF/Word/Excel | Cap dialog → Day Pass $3 → email prompt (stop) |
| IG-20 | Firefox / WebKit | IG-10 | Same as Chromium |
| IG-21 | Phones (SE, Pixel 7) | load + fill | No sideways scroll |
| IG-22 | Video | watch | Premium wording, current form |
