# Hero image request: regenerate 3 API/MCP heroes that show invented details
Date and time: 2026-11-11 00:01
Type: REQUEST (hero image fixes, images only, no new posts, no post text changes). Owner (Santosh) approved this request.
Source pack of the three current images: `from-grok/2026-11-10-2130-wishlist-batch2-api-mcp/images/` (md5 listed below).
Put your answer in a NEW folder in `handoff/from-grok/` named `2026-11-11-HHMM-hero-image-fixes-3-api-posts`, as described in section 8 of `from-grok/HERO-IMAGE-RULE.md`. Claude applies the images; Grok does not touch the site.

## Why this request exists
The three posts are live on freedailypro.com. Their heroes show details that are not in the post or not true of the product: a wrong auth header, a voice the API does not have, and a pay figure that does not match the post. The owner wants heroes that match the post. A hero that invents a UI, code or numbers is a defect even when the scene is on topic.

## Rules that apply to all three (from HERO-IMAGE-RULE.md, plus this request)
1. 1200 x 630 WebP, under 150 kB, file named exactly as the live slug: `<slug>.webp`, so it can replace the existing file. One unique image per post.
2. Bottom FreeDailyPro.com sticker only, applied with `Agent/scripts/brand_image.py` (F. icon, "FreeDailyPro.com" with only the first F teal, teal hairline). No logo inside the scene.
3. No "free" wording anywhere in the image. (The brand name FreeDailyPro in the sticker is fine.)
4. No third-party logos, product names or app chrome (no Claude, Cursor, Anthropic, RapidAPI, Postman or operating-system logos).
5. No invented UI, no invented code, no invented numbers. Any screen in the scene must be one of: (a) blurred or out of focus so nothing is readable, (b) abstract shapes with no text (bars, lines, blocks, dots), or (c) text taken exactly from this brief. Do not generate "realistic looking" code, JSON, voice names or figures and hope nobody reads them. Garbled pseudo-text counts as a failure too.
6. Prefer an abstract-but-relevant illustration or a person at a desk with screens that are soft-focus or text-free, over a photoreal screen full of fake content. Topic must still be obvious at a glance (see "must show" per post). The rule that a person is preferred stays; a person is optional here if it makes the screens easier to keep text-free.
7. No "AI", "assistant agent" or chatbot-branded wording on screen. The site rules forbid AI wording.
8. `imageAlt` describes only what is visible. Use the alt text suggested below if the image matches it; if you change the scene, send a matching alt text in your APPLY-MAP.

---

## 1. connect-the-freedailypro-mcp-server-to-claude-desktop
- Post title: Connect the FreeDailyPro MCP Server to Claude Desktop
- Live URL: https://www.freedailypro.com/blog/connect-the-freedailypro-mcp-server-to-claude-desktop
- File to deliver: `connect-the-freedailypro-mcp-server-to-claude-desktop.webp`
- Current file md5: `fc8b75c5fb61d3d629c8a52ceae82c3e`

### What the post really says (the real flow)
Create an API key on the developers page, copy the MCP config, put the key in a header named `X-API-Key` (the post says in bold: not `Authorization: Bearer`), add the block to the desktop client's MCP settings, fully quit and reopen the client, check the server shows as connected, then run a harmless smoke-test prompt (count words in a short sentence). Same key and same shared monthly quota as REST. The server URL is on the `api.freedailypro.com` host; there are also job-scoped URLs.

### What is wrong now
- The config file on the laptop shows `"Authorization": "Bearer ${MCP_TOKEN}"`, which is exactly what the post tells readers not to use.
- It also shows `http://localhost:8080/sse` and a server named `my-ai-assistant`, which are not the real URL or name, and the rest of the file is garbled pseudo-code.
- The chat window is titled "AI Assistant Agent" and shows an invented `get_weather` tool call for Seattle with a date. FreeDailyPro has no weather tool, and the post's smoke test is a word count.
- The sidebar (Chat, Tools, Agents, Memory, Settings, Logs) is invented app UI.

### The new image must show
- A developer at a desk with a laptop and a second screen. One screen shows a settings or config panel as abstract text-free line blocks (rows of short and long bars, no readable characters). The other shows a chat window as abstract bubbles (rounded blocks, no text) with one small "tool step" chip made of a plain icon (a wrench or plug icon is fine) and no words.
- The idea of "key goes into a header, then the client reconnects": for example a small padlock/key icon next to the config panel and a green connected dot (shape only, no label) next to the chat window.
- Optional: a sticky note or card with a key icon and no characters.
### The new image must NOT show
- Any readable text on the screens, including `Bearer`, `Authorization`, `X-API-Key`, URLs, JSON, tool names, server names or "weather".
- The words AI, Agent, Assistant, Claude, Cursor, Anthropic, or any app logo or window chrome copied from a real product.
- localhost, ports, `/sse`.
- Invented numbers or dates.
### Suggested alt text
"Developer at a desk with a settings panel on a laptop and a chat window on a second screen showing a tool step, with a key icon beside the settings."

---

## 2. text-to-speech-api-weighted-calls-and-trial-limits-explained
- Post title: Text to Speech API: Weighted Calls and Trial Limits Explained
- Live URL: https://www.freedailypro.com/blog/text-to-speech-api-weighted-calls-and-trial-limits-explained
- File to deliver: `text-to-speech-api-weighted-calls-and-trial-limits-explained.webp`
- Current file md5: `e45a8181be7ffeedf0174fba219ad37e`

### What the post really says
This is a text-to-speech API (text goes in, an audio file comes out), not speech-to-text. The API lists voices, then synthesizes a short script to an MP3 or WAV file. A speech synthesize call counts as a heavier "weighted" call than a normal utility call, and a trial key has a small fixed number of synthesize calls and a short per-request text cap. The voices are not named in the image by design (the real list is in the post; do not reproduce it).

### What is wrong now
- The screen shows a voice dropdown set to "Matthew (Male)" and `"voice": "matthew"` in the request. The API has no voice named Matthew.
- It also shows Language and Pitch controls (the API has speed only, no pitch), a "Send Request" button and "Response: 200 OK" panel, which are invented UI, plus an invented sample script and request JSON.
- The second monitor shows invented screenplay text. Not harmful but it is readable fake content, so remove it.

### The new image must show
- A person with headphones at a desk, or an abstract scene without a person, with one clear audio waveform (the output) on a screen, and on the other side a block of plain text lines drawn as grey bars (the input), with an arrow or flow from the text bars to the waveform to a small audio-file icon. That says "text in, audio out".
- The call-weight idea: a simple gauge or meter (dial or horizontal bar) with a needle or fill, drawn with no tick labels and no numbers, placed beside the waveform. A row of small equal blocks next to one tall block can express "one speech call weighs more than one normal call" without any figure.
- Optional: a microphone-free studio desk, speaker or headphones as props (output side, since the product is synthesis).
### The new image must NOT show
- Any voice name (Matthew, Amy, Lessac, Ryan, Alba or any other), any "Male/Female" label, any language or pitch control.
- Any readable request or response text, JSON, HTTP status, button labels or headers.
- Any number, character count, price, plan name or limit figure. Gauge has no digits.
- A microphone recording a person speaking (that reads as speech-to-text/recording, the wrong direction).
- Screenplay or script text.
### Suggested alt text
"Person with headphones at a desk looking at a screen where lines of text turn into a sound waveform, with a dial gauge beside it showing how heavy a speech call is."

---

## 3. paycheck-calculator-api-with-2026-tax-tables
- Post title: Paycheck Calculator API With 2026 Tax Tables
- Live URL: https://www.freedailypro.com/blog/paycheck-calculator-api-with-2026-tax-tables
- File to deliver: `paycheck-calculator-api-with-2026-tax-tables.webp`
- Current file md5: `cf70736b65c7707b2cc4501ad966fe63`

### What the post really says
The sample request is $85,000 annual gross, 26 pay periods, single, New York, 5 percent retirement contribution. The sample estimate per check: gross 3,269.23, federal 343.65, New York state 144.75, Social Security 202.69, Medicare 47.40, retirement deferral 163.46, net per check 2,367.27, estimated annual net 61,549. The post frames it as an estimate, not payroll or tax advice.

### What is wrong now
- The hero shows "Monthly Take-Home Pay $5,312", a bar chart with $1,488, $623 and $377, and a JSON block with `estimated_take_home: 5312`, `effective_tax_rate: 0.289` and `"pay_period": "monthly"`. None of these match the post. The post's estimate is per paycheck, biweekly, net 2,367.27, and annual net 61,549.
- The JSON field names are invented and differ from the real response.
- The offer letter and calculator props are fine and on topic.

### The new image must show (choose ONE option, option A preferred)
- Option A (no readable numbers): a person at a desk with a monitor showing a paycheck breakdown as an abstract layout: one wide bar split into coloured segments (net share large, tax shares smaller) and a small stacked set of horizontal bars, all with no digits, no currency signs and no labels. Props kept: offer letter with blurred/greeked lines, calculator, notebook. A small calendar-like grid of dots can hint at pay periods without numbers.
- Option B (exact numbers only): if you want a readable number, it must be exactly one of these, spelled this way: `2,367.27` as net per check, and `61,549` as estimated annual net. No other figure may appear anywhere in the image (no $5,312, no percentages, no tax lines). Do not add JSON or field names. If you cannot render the digits crisply, use option A.
### The new image must NOT show
- $5,312 or any monthly figure, any effective tax rate, any other dollar amount, any state or federal tax figure, any JSON or field names.
- A year-based number other than the figures above (no "2026" tax tables panel with invented brackets).
- Payroll-software or bank logos.
### Suggested alt text
Option A: "Person at a desk reviewing a take-home pay breakdown shown as coloured bars on a monitor, with an offer letter, calculator and notebook on the desk."
Option B: "Person at a desk reviewing a take-home pay screen that shows a net paycheck figure and an annual net figure, with an offer letter and calculator on the desk."

---

## Delivery (what Claude expects back)
Create `from-grok/2026-11-11-HHMM-hero-image-fixes-3-api-posts/` with:
- `images/<slug>.webp` for the three slugs above (exact live file names, 1200x630, under 150 kB, sticker applied).
- `APPLY-MAP.md` with one row per slug: slug, blog title, live URL, what you changed, final alt text, and the option chosen for the paycheck post (A or B).
- `APPLY-MAP.tsv` with columns `slug, title, reason, md5, bytes, url` (same as earlier hero packs), where `md5` and `bytes` are of the new WebP files, so Claude can confirm the right file went live.
- `NOTE.md` with the self-check from section 7 of HERO-IMAGE-RULE.md ticked for each image, plus one line per image stating: no readable invented text, no voice names, no Bearer, no figure other than the allowed ones.
- Do not edit the posts, front matter or any other file. If you think the post text is wrong, say so in NOTE.md instead.

Claude will check each delivered image at full size against the "must NOT show" lists above before applying. An image with garbled pseudo-text on any screen will be sent back.
