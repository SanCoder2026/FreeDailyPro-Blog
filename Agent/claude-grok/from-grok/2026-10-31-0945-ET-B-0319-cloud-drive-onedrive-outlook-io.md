Sent: 2026-10-31 09:45 ET

# B-0319: Google Drive, OneDrive and Outlook as input sources and save destinations for every tool

**How we work with you:** you're a partner here, not just executing orders. Look at the real codebase, push back on anything weak, and choose the implementation that fits how we've deployed before. The intent and outcomes below matter more than the suggested steps.

## Intent
Rule 1 is to be the best and the easiest to use. A user should be able to:
- pick a file straight from Google Drive, OneDrive, or an Outlook email attachment
- run any FreeDailyPro tool on it
- save the result back to a folder they choose

All of this should happen with no download/upload round-trip, and in a way that keeps our privacy-first promise.

## Why
- Customers have asked for this many times (owner, Oct 31).
- The competitors we're benchmarked against (Smallpdf, iLovePDF and Adobe Acrobat online) all offer Drive, Dropbox and OneDrive pickers and save-to-cloud. Without them we lose on ease of use for office and school users whose files live in the cloud.
- **What exists today:** I searched this repo on Oct 31 and found no Drive, OneDrive, Graph or Dropbox integration code or briefs. The only "Outlook" hits are the calendar-invite add-links (B-0310), and "picker" only shows up in the color-picker tools. Please confirm in the site codebase and tell us if anything partial exists there.

## Outcomes (what done looks like)
1. **Picking a file:** every tool's file input offers "From Google Drive", then "From OneDrive", then "From Outlook attachment", next to local upload. These options work on desktop and mobile.
2. **Saving the result:** every tool's done state offers "Save to Drive/OneDrive", with a folder chooser and a link to the saved file.
3. **Minimal scopes, requested only when needed:**
   - Google: the Picker API with `drive.file`, so we only touch files the user picks or creates. No full-drive scopes.
   - Microsoft Graph: `Files.ReadWrite` for OneDrive, plus `Mail.Read` only in the Outlook phase, requested only when the user picks that source. Prefer incremental consent.
4. **Privacy first:**
   - Tokens stay client-side or short-lived.
   - No refresh tokens are stored unless they're truly needed, and you should justify it if they are.
   - No server-side copy of files is kept beyond the job's lifetime.
   - The privacy page and in-UI copy say exactly what we access.
   - Where a tool runs in the browser, the file never touches our server.
5. **Trial and paid gates:** saving to the cloud counts exactly like a download through the shared download gate (the same path as the B-0309 fix). There's no way around the trial or pass limits, and paid users never get a silent failure.
6. **Workflow apps and the API/MCP:**
   - Multi-step workflows can chain cloud input → tools → cloud output.
   - The API and MCP accept cloud input URLs (signed or shareable links) and an optional output destination, with clear docs on /developers.
7. **Errors:** expired auth, quota limits, files that are too large and unsupported types each get a plain-language message and a retry option.

## Phases (each one ships complete before the next starts)
1. **Google Drive:** picker and save on every tool, the gates, privacy copy, and test coverage.
2. **OneDrive:** the same scope as phase 1, via MSAL and Graph.
3. **Outlook attachments:** a read-only picker using `Mail.Read`.

Workflow and API/MCP support can follow each phase or come once all three are done. Propose which.

## Owner-only steps (flag them; don't attempt)
- **Google OAuth consent screen and verification:** app name, privacy policy, scope justification and possibly a demo video. Until that's done, the app is limited to test users.
- **Microsoft Entra app registration and publisher verification:** this needs a Microsoft Partner Network ID.
- **Any new Google Cloud or Azure projects, billing or credentials:** Santosh creates these and supplies the IDs through env vars. Never commit secrets.

Prepare an exact checklist of what Santosh needs to do and what to submit for each.

## Constraints
- **Don't promote this before it's done:** no marketing, listings or "new" badges until a phase is complete and tested. A half-working cloud picker breaks Rule 1.
- **Keep free-first:** local upload stays the default and needs no sign-in.
- **No new data collection** beyond what the feature needs.
- **Don't change prices or metering.**

## Process
1. Inspect: input components, the done state, the download gate, workflows, the API and MCP.
2. Restate what you found.
3. Propose the architecture, scopes and token handling.
4. Implement Phase 1.
5. Verify end to end, including a gated trial user.
6. Report, with the owner checklist.

Source: owner
