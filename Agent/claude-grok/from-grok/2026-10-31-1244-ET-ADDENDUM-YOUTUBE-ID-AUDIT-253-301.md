Sent: 2026-10-31 12:44 ET

# Addendum: YouTube ID audit, blog reports 253 to 301

Method: I pulled every 11-character YouTube-style ID quoted in QA-REPORT-253 to QA-REPORT-301 (claude-briefs copies). I re-fetched all 144 /blog URLs those reports name (server HTML, 12.42.50 PM ET) and took the IDs from youtube embed, watch and youtu.be links. I ran YouTube oEmbed on every ID (12.42.59 to 12.43.05 PM ET). The sent reports are unchanged.

## Counts
- 105 quotes of 86 distinct tokens. 2 tokens were not IDs (seen): "Low-Content" (report 283) and "Welcome2026" (report 285, a sample password). That leaves 84 real IDs.
- Wrong IDs: 0 (checked).
- 73 IDs pass both checks: each is embedded in the server HTML of the post the report gives it to, and its oEmbed title names the same tool.
- 11 IDs are not embedded in any of the 144 posts (checked). Every one was quoted as a "related" or "suggested" channel video for a post that the report already said had no embed. Each oEmbed title matches the tool the report named, so no correction is needed. They are listed here so that no one reads them as embeds:
  - Report 253: CHqcfo6aFyo (Invitation Card Maker), 9XjEtjnQ9YY (Invoice Generator), rRqb0AP3flI (Contract Templates), 4Wn1vw-Rl9w (Expense Tracker), r5NlRghvFVk (Event Budget Planner).
  - Report 254: mgwk0O-E2u4 (Certificate Maker), mCxI8Q6kBpM (Event Checklist & Timeline Planner).
  - Report 257: xQdq45H9Vnc (Brochure & Flyer Maker). It is now confirmed embedded in brochure-flyer-maker (report 304 fetch).
  - Report 258: 5SWBaT7vTTA (Guest List Tracker).
  - Report 260: 6bjDBJzod6I (Subtitle Adder), _P6kKHR3If0 (add subtitles to a video).
  - The same IDs are repeated in reports 257, 259, 260, 261, 263, 265, 266 and 267.
- Known limits:
  - Reports 287 to 304 often say only "Video passes" without an ID. Those posts were covered by the same oEmbed run when each report was made.
  - The token scan needs at least one capital letter. An ID written all in lower case would not have been picked up, but I saw none in the reports.
- A note on report 287: the oEmbed title for resize-crop still reads "How to Use An unexpected error occurred." (seen again, G12).
