# B-0319 cloud pickers: phased plan (Claude, 2026-10-31 12:50 ET)

Principle: tokens and files stay in the browser. No server copy, no refresh tokens stored. Sign-in per session; closing the tab forgets everything (matches our privacy promise).

## Phase 1: Google Drive (about 2-3 days of work)
- Google Identity Services token client, scope `drive.file` only (non-sensitive; no Google security review, appears per-file).
- Google Picker to choose files in; Drive upload (multipart) to save results out.
- Shared helper `lib/cloud/google.ts` + `<CloudPickerButton provider="google">` used by the shared file-drop component, so every tool gets it at once; each Save/Open still costs one trial use like any download.
- Owner steps: create a Google Cloud project, enable Drive API + Picker API, create OAuth Web client with origins https://www.freedailypro.com, create browser API key restricted to our domain, set consent screen (app name, privacy URL). Send me client id + API key (both public values).

## Phase 2: OneDrive / SharePoint (about 2-3 days)
- Microsoft Entra app registration (SPA, multi-tenant + personal accounts), MSAL.js popup, scopes Files.ReadWrite (and offline_access NOT requested).
- OneDrive File Picker v8 (iframe) to pick; Graph PUT `/me/drive/root:/{name}:/content` to save (4 MB simple upload, upload session above that).
- Owner steps: Entra app registration, redirect URI https://www.freedailypro.com/, Publisher domain verification (optional for small use; unverified apps show a warning, so verify the domain).

## Phase 3: Outlook attachments (last, optional)
- Graph Mail.Read incremental consent, list recent attachments, download one at a time. Sensitive scope, adds consent friction; do only if demand shows.

## Risks / warnings
- Google OAuth consent screen: with only `drive.file` no verification needed; adding broader Drive scope triggers a security assessment (do not).
- MSAL token caching must be set to memory, not localStorage, to honor "erased on close".
- Third-party cookies/popup blockers: use popup flow, show clear message.
- Privacy page needs a sentence naming Google/Microsoft file pickers (owner/Grok, I do not edit policy docs).
- Phase 1 alone delivers most of the value; ship it, measure use, then decide on 2 and 3.

## Needs Santosh
Approve phase 1 now and create the Google Cloud project (I will give click-by-click steps when you say go).
