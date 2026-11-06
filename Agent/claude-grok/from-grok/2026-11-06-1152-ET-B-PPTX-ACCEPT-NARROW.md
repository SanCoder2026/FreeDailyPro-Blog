Sent: 2026-11-06 11:52 AM ET (America/New_York) — Orchestrator hourly feed
Source: owner

# B — Narrow PowerPoint dropzone accept lists to formats the engine actually processes

## Intent
Stop users from picking legacy `.ppt` / `.odp` files on tools that only process `.pptx` XML, so they do not hit a dead end after choosing a file the page advertised as accepted.

## Why
SEO live audit `freedailypro-seo-engine/hourly/2026-11-06-1100-four-page-upgrades-k.md` (~11:00 AM ET Nov 6) against live JS chunks:

- `/tool/add-slide-numbers` — dropzone `accept=".pptx,.ppt,.odp"` (acceptLabel still `.pptx`), but tip says convert legacy `.ppt` → `.pptx` first and processing is `.pptx` XML only.
- `/tool/compress-powerpoint` — same pattern: `accept=".pptx,.ppt,.odp"` / acceptLabel `.pptx`; tip tells users to save old `.ppt` as `.pptx` first.

Same class as replace-fonts-powerpoint (called out in SEO 1000-j A3). Title/meta/H1 rewrites from that SEO batch are **not** in scope here (those wait on Santosh). This brief is accept-list only.

## Outcomes
1. On add-slide-numbers and compress-powerpoint (and replace-fonts-powerpoint if the same accept string is still live), file picker / dropzone `accept` (and any acceptLabel / picker copy) lists **`.pptx` only**.
2. Keep the existing tip that tells users to convert `.ppt` → `.pptx` in PowerPoint first.
3. No pricing, trial, ad, or title/meta/H1 changes in this brief.
4. After deploy, picking a `.ppt` or `.odp` from the OS file dialog is blocked by the accept filter; `.pptx` still works end-to-end.

## Suggested direction
Inspect the shared PowerPoint tool dropzone / ToolPage accept props. Prefer one shared fix if these tools share a constant; otherwise patch each tool’s accept prop. Interpret freely; match prior FreeDailyPro patterns for accept narrowing.

## Constraints
- Do not change titles, metas, H1s, or brand suffix in this brief.
- Do not remove or turn off ads.
- Never say "free tools"; leave Professional Tools / trial copy alone.
- Source: owner.

## Process
Inspect live accept props → restate the mismatch → implement accept narrow → verify picker + tip still coherent → note pages touched in your next from-claude status.
