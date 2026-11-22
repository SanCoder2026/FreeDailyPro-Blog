Sent: 2026-11-21 19:08 ET

# Live functional findings (FDP-83, guest)

- Chromium and Firefox: paywall only; CTA "Start 7-day trial · $29.99/mo" → /profile sign-in (email field). Stopped.
- `?checkout=success` → guest sees the Stripe-confirming message; 20 status polls; message gone at 70 s.
- All 11 page links 200; Workflow Products card and UFC cross-links present.
- Studio behaviour untested (entitlement needed).
