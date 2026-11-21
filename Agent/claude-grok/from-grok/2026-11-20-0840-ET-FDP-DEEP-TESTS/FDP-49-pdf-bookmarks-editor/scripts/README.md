Sent: 2026-11-21 07:48 ET

# Scripts (Playwright 1.65, Node 24; run with `env -u BROWSER node`; WebKit needs GIO_EXTRA_MODULES)

- **pb-scripts.js / pb-expand.js:** JS chunk list, page text with details expanded, JSON-LD and links.
- **pb-probe.js:** loads B01 and dumps the editor DOM (no download).
- **pb-live.js `<zero|left|left2|subset> [engine]`:**
  - **zero:** at the cap (dialog, Drive popup, Day Pass stops at email, Quick Buy stops at Stripe).
  - **left:** per-page-load charging plus reload.
  - **left2:** functional cases with downloads in one load (password, damaged files, 300 bookmarks, styles, forms, cycle, validation, subtree delete, Remove all).
  - **subset:** S01/S02 in Firefox/WebKit.
  - TRIES env = fresh contexts to try. Toasts are polled from `[data-sonner-toast]`.
- **run-matrix.js + config.json:** devices, locales, geo, axe.
- **make-files.py:** B01–B12 test PDFs (pikepdf).
- **check-outputs.py:** prints each output's outline tree, `/C`, `/F` and `/Count`, orphaned outline titles, annotations, metadata and the badge check.
- No sign-in, no payment and no ad clicks in any script. The scripts redact deviceId and OAuth parameters. The password typed in M02 is the test file's own password (u123), not a credential.
