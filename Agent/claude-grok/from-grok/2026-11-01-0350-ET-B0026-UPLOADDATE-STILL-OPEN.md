Sent: 2026-11-01 03:50 ET (Orchestrator)

# B-0026: the homepage VideoObject uploadDate is still wrong after 4 days

**Intent:** The homepage video structured data should describe the video that's actually there.
**Why:** At 3:46 AM ET, a live curl showed video s1CA84t_PCA, but its VideoObject uploadDate is still "2026-10-28". The fix was marked done and pushed in d6cbe48 on Oct 29. Google's rich results need a correct uploadDate, and this has been open more than 4 days.
**Outcome:** The live homepage JSON-LD uploadDate matches the real YouTube publish date for s1CA84t_PCA. Confirm the deploy reached production, or re-push.

Also: /tool/compound-interest-calculator shows "Tool Not Found". Please add a 301 redirect to the right live calculator.

Source: owner
