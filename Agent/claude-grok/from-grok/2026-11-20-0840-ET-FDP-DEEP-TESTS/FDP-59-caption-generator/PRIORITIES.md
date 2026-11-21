Sent: 2026-11-21 12:34 ET

# FDP-59 Social Caption Generator: priorities (2026-11-21 EST, -v2 12:15 EST)

| Pri | Item | Why it matters | Suggested fix |
|---|---|---|---|
| — | (-v2) No P1 items. The "never charges / works at 10/10" and "no trial strip or Quick Buy" items moved to REPORT.md Owner questions 1–2: policy question held for Santosh (not one of the three exempt tools). | | |
| P2 | "AI" on a template tool: thumbnail "AI CAPTIONS", VideoObject + blog clip "How to Generate AI Social Media Captions", old "AI-powered" subtitle in the video | Misleading vs the FAQ "Nothing is composed from scratch" | Retitle; keep "AI" for AI Studio and link AI Social Publisher for AI drafts. |
| P2 | Video outdated (old UI, "SEO Tools", "10 free uses daily", "Pro", fixed #fyp #viral #trending, "Free Step-by-Step", "PDF tools"/"#SEOTools" tags; personal bookmarks bar visible) | Shows features that changed; "free" wording | Re-record on the current UI with Professional Tools / trial-use wording. |
| P2 | Hindi/Indic hashtags broken (`#दवलसलशर #दव…`) | Unusable output for the hi audience | Include `\p{M}` in the `h()` word regex. |
| P3 | Punctuation-only topic ("!!!") gives empty drafts | Looks broken | Disable Generate unless the topic has a letter/digit. |
| P3 | Filler hashtags (#BigTips #BigLife) not disclosed | FAQ says "cut from your topic words" | Drop padding here or disclose it. |
| P3 | Blog errors: X example with hashtags; "kept exactly as written"; "SEO tools category"; "counts as one of your 10 trial usages" | Accuracy | Fix after the policy decision. |
| P3 | Meta description 70 chars, generic | SEO | Write a 140–155 char description (platforms, tones, character count). |
| P3 | Stopword-only topic → #The #And #Of; detail in Japanese gets a Latin "." | Polish | Skip stopword-only tags; respect CJK full stops. |
| P2 | axe button-name (critical): Platform and Tone selects have no accessible name; locale pages translate only nav/breadcrumb | Screen-reader users can't tell the two dropdowns apart; mixed-language page | Associate the labels (htmlFor/aria-labelledby); translate tool strings. Header overflow (iPhone SE 9 px) and ja 3 px are site-wide. |
