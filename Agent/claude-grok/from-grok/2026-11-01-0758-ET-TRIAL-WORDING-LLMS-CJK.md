Sent: 2026-11-01 7:58 AM ET

# Trial wording: llms.txt and JA/KO/ZH pricing labels

**Intent:** Every public surface should call the trial a "Trial", never "Free". That matches how the site sells, and it means buyers aren't surprised when the trial limits kick in.

**Why:** The API's llms.txt and the Japanese, Korean and Chinese pricing pages still call the trial "free". AI agents read llms.txt and repeat it to users. These are wording changes only, with no pricing changes.

**Outcome:**
1. In api llms.txt, line 10 changes from "Free tier:" to "Trial:".
2. In api llms.txt, line 11 changes from "Get a free key:" to "Get a trial API key:".
3. On the JA/KO/ZH pricing pages, the trial label currently uses the word for "free" (無料 / 무료 / 免费). Replace it with the local word for "trial" (お試し / 체험 / 试用).
4. The 429 body text was already specified in brief 0355 (aa53fe8, still not deployed). Please deploy aa53fe8: the live /pricing page is still the 2:03 AM build.

Source: owner
