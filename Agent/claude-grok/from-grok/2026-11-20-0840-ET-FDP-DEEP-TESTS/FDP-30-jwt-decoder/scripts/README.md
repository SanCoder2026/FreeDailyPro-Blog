Sent: 2026-11-21 00:18 ET

# Scripts (Playwright 1.65, Node)

Output paths point at our box (`/workspace/deep/30-jwt-decoder/…`). Run with `env -u BROWSER node <script>`. All scripts are guest-only: they never sign in, never pay, never type an email or card, and never click ads. Tokens are synthetic (`evidence/testfiles/tokens.json`).

- `jd-probe.js`: starting count, chunks, controls.
- `jd-copy.js`: expands the page copy; saves the text and JSON-LD.
- `jd-live.js [ids] [out]`: token cases J01–J23; records alerts, rendered text, page errors, and checks every request for payload fragments (`leaks`); selection-copy gate check.
- `jd-gate.js`: Copy result / Save as text / Print at 0 and with uses (max 6 contexts). At 0 it would follow a cap dialog to the email prompt and stop (none appeared).
- `jd-misc.js`: head tags, keyboard order, print PDF of a decoded token.
- `jd-share.js`: pastes a token, clicks Share, records what was copied.
- `jd-blog.js`, `jd-blog2.js`: text of `/blog/jwt-decoder` and `/blog/jwt-decoder-debug-tokens`.
- `run-matrix.js config.json`: 10 devices, 11 locales (incl. /ar probe), 6 geo contexts, axe.
