Sent: 2026-11-20 08:40 ET

# Reproduce: unit-converter

Guest browser, https://www.freedailypro.com/tool/unit-converter. Nothing here costs a trial use.

- **R1 (first screen):**
  1. Open the page in iPhone SE emulation (320×568), or on a real small phone.
  2. Don't scroll. Neither the Value box nor the answer is visible.
  3. `node scripts/uc-kbd.js` reports `phone_iPhone SE.valueY` 644 and `resultY` 818 (vh 584).
- **R2 (ft + in):** open Length → the From list. It has foot and inch but no "ft + in". Try 5'10": you need two separate conversions.
- **R3 (precision):** `?c=length&from=nanometer&to=mile&v=1` shows 6.213712e-13 (expected 6.213711922e-13).
- **R4 (negatives):** `?c=length&from=meter&to=foot&v=-5` shows −16.40419948 with no message. `?c=fuel&from=miles%2Fgallon%20(US)&to=liters%2F100%20km&v=-30` shows −7.840486111.
- **R5 (⅓ cup):** open /tool/unit-converter/cups-to-ml. The table row reads "0.33 | 78.07411805".
- **R6 (meta):** view the source of /tool/unit-converter/celsius-to-fahrenheit. The meta description says "1 celsius = 33.8 fahrenheit".
- **R7 (screen reader):** change the Value with a screen reader on. Nothing is announced. `kbd.json` → `live.ariaLive` is [] and `status` is 0.
- **R8 (video):** play the embedded video at 0:20–0:30. It shows 4 tabs and the old breadcrumb.
- **R9 (blog):** in /blog/unit-converter, under "Category: converters", it says "Browser tools list 10 trial usages a day". Compare: at 0 remaining, Copy result, Save as text and Print still work (`node scripts/uc-gate.js`).
