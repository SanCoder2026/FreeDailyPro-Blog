Sent: 2026-11-21 12:15 ET

# FDP-59 Social Caption Generator: priorities (2026-11-21 EST)

| Pri | Item | Why it matters | Suggested fix |
|---|---|---|---|
| P1 | Never charges and never stops: full drafts and Copy at 10/10; 20 generations + 4 copies with uses left = 0 uses; no `usage.log` POST | Owner rule: full results at 0 trial uses = P1 gate gap; uncounted tools outside the Nov 20 list are a policy question | Owner decides: count it (charge Generate and Copy, cap dialog) or list it as uncounted on purpose and fix the copy. |
| P1 | No trial strip or Quick Buy on the page | No path to a pass from this tool; the business goal can't happen here | Show the standard strip, or (if uncounted) an AI Social Publisher / pass CTA. |
| P2 | "AI" on a template tool: thumbnail "AI CAPTIONS", VideoObject + blog clip "How to Generate AI Social Media Captions", old "AI-powered" subtitle in the video | Misleading vs the FAQ "Nothing is composed from scratch" | Retitle; keep "AI" for AI Studio and link AI Social Publisher for AI drafts. |
| P2 | Video outdated (old UI, "SEO Tools", "10 free uses daily", "Pro", fixed #fyp #viral #trending, "Free Step-by-Step", "PDF tools"/"#SEOTools" tags; personal bookmarks bar visible) | Shows features that changed; "free" wording | Re-record on the current UI with Professional Tools / trial-use wording. |
| P2 | Hindi/Indic hashtags broken (`#दवलसलशर #दव…`) | Unusable output for the hi audience | Include `\p{M}` in the `h()` word regex. |
| P3 | Punctuation-only topic ("!!!") gives empty drafts | Looks broken | Disable Generate unless the topic has a letter/digit. |
| P3 | Filler hashtags (#BigTips #BigLife) not disclosed | FAQ says "cut from your topic words" | Drop padding here or disclose it. |
| P3 | Blog errors: X example with hashtags; "kept exactly as written"; "SEO tools category"; "counts as one of your 10 trial usages" | Accuracy | Fix after the policy decision. |
| P3 | Meta description 70 chars, generic | SEO | Write a 140–155 char description (platforms, tones, character count). |
| P3 | Stopword-only topic → #The #And #Of; detail in Japanese gets a Latin "." | Polish | Skip stopword-only tags; respect CJK full stops. |
| P2 | axe button-name (critical): Platform and Tone selects have no accessible name; locale pages translate only nav/breadcrumb | Screen-reader users can't tell the two dropdowns apart; mixed-language page | Associate the labels (htmlFor/aria-labelledby); translate tool strings. Header overflow (iPhone SE 9 px) and ja 3 px are site-wide. |
