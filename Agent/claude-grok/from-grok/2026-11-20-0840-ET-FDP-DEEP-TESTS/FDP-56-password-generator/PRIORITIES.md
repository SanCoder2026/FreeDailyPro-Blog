Sent: 2026-11-21 11:32 ET

# FDP-56 Password Generator: priorities (2026-11-21 EST)

| Pri | Item | Why it matters | Suggested fix |
|---|---|---|---|
| Policy (P1 if counted) | Uncounted: Copy works at 10/10 with no cap dialog and no usage.log; Generate is free; no trial strip | Not on the Nov 20 exempt list | Owner decides. If counted, make `gateShare` charge and block for this tool; if not, add it to the exempt list and remove the Privacy line. |
| RERUN-AFTER-RESET | Copy/Generate with trial uses left not observed (Firefox 8, WebKit 6, Chromium 6 fresh contexts all 10/10 on 2026-11-21) | Confirms whether Copy charges or logs when uses remain | After midnight UTC (7:00 PM ET; row in RERUN-AFTER-RESET.md): `TRIES=10 env -u BROWSER node px56-live.js left firefox`; expect L01–L07 per owner decision (uncounted: stays 0, no usage.log). |
| P2 | Privacy says usage is recorded on Copy; FAQ/How-to say never | Contradictory trust copy on a security page | Align the copy with the decision above. |
| P2 | Spaces-only "Symbols to use" box gives passwords with leading/trailing spaces while the alert says defaults are used | Invisible spaces → sign-up trims → lockouts; wrong message | Strip whitespace from the set; fall back to the default when nothing is left. |
| P2 | Video stale (old UI, "Text & Writing", "10 free uses daily", no passphrase) and "Free" in title/description; personal bookmarks bar visible | Wrong expectations; the owner avoids "free" wording | Re-record with the current UI; title without "Free"; clean browser profile. |
| P2 | Guides link chmod and cURL posts; the matching blog post isn't linked | Lost internal relevance for a GA-top page | Link /blog/password-generator-new-accounts (and the Welcome2026 strength post). |
| P2 | Locale pages: only the breadcrumb is translated; the tool UI, H1 and title stay English | Mixed-language page | Translate the tool strings (site-wide pattern). |
| P3 | Letters/digits typed into the symbols box are treated as "symbols" | Odd, but the maths stays right (dedup) | Restrict to non-alphanumerics or relabel "Extra characters". |
| P3 | "no bias towards any character" line | Digits appear more often by design (uniform over qualifying passwords) | Say "every qualifying password is equally likely". |
| P3 | iPhone SE: Feedback button covers "Hide" at the fold | Tap target overlap | Offset the FAB or add bottom padding. |
| P3 | Blog closing sentence garbled; no passphrase or symbols-box coverage | Copy quality | Edit the post. |
| P3 | password-strength meta "Generate strong passwords and check strength" | C50 keyword overlap | Rewrite as check-only. |
| P3 | axe: label-content-name-mismatch, region (desktop) | A11y polish | Fix the label. |
