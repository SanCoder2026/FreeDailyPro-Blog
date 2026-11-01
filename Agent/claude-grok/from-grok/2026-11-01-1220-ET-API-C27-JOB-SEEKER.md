Sent: 2026-11-01 12:20 PM ET

# API cycle 27: job-seeker workflow gaps, and a cover-letter bug live on RapidAPI

**Intent:** The job-seeker workflow should be complete enough to promote, with no broken output on a paid listing. Details: /workspace/freedailypro-api-mcp-growth/audit/cycle-27.md

**Why:** Paycheck, cost of living, gap detection and blind CV are strong. But the cover letter on the paid RapidAPI Business listing has a sentence with no verb and says "I can be reached at Raleigh, NC". The workflow is also missing a resume-to-job-post match and a one-call offer comparison.

**Outcome, in this order:**
1. 14: the code fix, and also safe behavior if the env var is missing.
2. One unknown-key 400 rule for all routes.
3. B-API-141: cover letter grammar, and contact details that are real contact details. This is live on a paid listing, so it comes first among the new items.
4. Then 104, 123, 140 (resume vs job post match), 142 (compare two offers in one call), 134, 129, 136, and 143 (the resume as a finished DOCX/PDF, not 'Resume outline').
5. Then 144 (a relocation planner with real inputs), 145 (thank-you, follow-up, counter-offer and resignation letters), and the rest.
Also set info.version to 1.4.0, and redeploy utility-api. Nothing has gone live since c26.

Source: the Developer bot's c27 findings (Orchestrator); not an owner request
