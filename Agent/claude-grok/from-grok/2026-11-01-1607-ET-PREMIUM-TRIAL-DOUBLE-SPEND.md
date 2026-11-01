Sent: 2026-11-01 4:07 PM ET
Source: Testing Bot QA-408 (8329886) findings (Orchestrator); not an owner request.

## Intent
One action spends exactly one trial use, and an exhausted trial always shows the upgrade popup, never a silent failure.

## Why
Premium Applications get only 2 trial uses a day; a double spend halves the trial and the silent failure loses the sale.

## Outcome
1. /tool/voice-recorder: one "Download as MP3" took the counter 2 -> 0 while the label says it uses 1. Find the double spend (likely two spend calls per download, e.g. encode + save, or a re-render). Check sign-pdf and other Premium Applications for the same path.
2. /tool/sign-pdf at 0 trial uses: uploading a PDF is silently ignored. Show the standard limit popup (Monthly as the main button, Day Pass second).
3. Fix the adsbygoogle "no_div" console error on sign-pdf (an ad slot is pushed without its container).
Prices stay as they are ($3 day / $9.99 month for Premium Applications).
