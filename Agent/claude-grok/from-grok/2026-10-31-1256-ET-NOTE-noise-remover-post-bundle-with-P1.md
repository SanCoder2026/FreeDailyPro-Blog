Sent: 2026-10-31 12:56 PM ET

# NOTE: bundle the noise-remover blog overclaim with the noise-remover P1 tool fix

**Intent:** The blog post must not promise more than the tool delivers. Readers who try hum removal after reading it get almost nothing, and that costs us trust and conversions.

**What's wrong:** https://www.freedailypro.com/blog/noise-remover claims the tool is built for hum, hiss and fan noise. It gives 12/20/35 dB ceilings and an example of about 18 dB. Measured: Standard and Aggressive cut 60 Hz hum by only about 1.3–2 dB, and the two modes give identical output. Only Voice gave real cuts (12.8 dB and 8.0 dB). Sources: the "Noise-remover post vs our measurements" section of 2026-10-31-1255-ET-QA-REPORT-331.md (QA reports 331–333), QA-REPORT-218, admin row 63 in report 252 and row 84 in report 260.

**Do this as one item with the existing noise-remover P1 tool fix (QA #218), not as a separate brief:**
1. **Now, until the tool is fixed:** rewrite the post to lead with **Voice mode** for hum and fan noise. Remove the 12/20/35 dB ceilings and the 18 dB example, or soften them to "targets", and don't state a dB figure you haven't measured. Keep the fair parts: the Voice guidance and the warnings about music and multiple passes.
2. **After the tool fix ships:** re-measure Standard, Aggressive and Voice on the same hum and fan test clips. Only then put dB figures back in the post and on the page, using the measured numbers.
3. Report both steps back under the noise-remover P1 item.

Source: owner
