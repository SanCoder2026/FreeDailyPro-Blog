Sent: 2026-11-21 12:15 ET

# FDP-59: how to reproduce (guest)

## P1: never charges / works at the cap
1. Fresh profile; open https://www.freedailypro.com/tool/caption-generator. Check localStorage `fdp-usage-v1` (`usageToday/limit`). Note: no "Trial: … remaining" strip and no Quick Buy anywhere on the page.
2. If it shows 10/10: type a topic, press **Generate Captions** → three drafts, no dialog. Press **Copy** → "Copied!". Still 10/10; no `/api/trpc/usage.log` POST in DevTools.
3. If it shows 0/10: generate several times, change tone/platform, copy, reload, generate again → still 0/10; no `usage.log` POST.

## P2: AI wording
View page source/JSON-LD: VideoObject name "How to Generate AI Social Media Captions". YouTube OGI6yqaI1oU thumbnail "AI CAPTIONS"; at 0:58 the subtitle reads "AI-powered social media captions".

## P2: Hindi hashtags
Topic "दिवाली सेल शुरू", Instagram, Fun → hashtags `#दवलसलशर #दव #वल #लस #सल`.

## P3: empty topic
Topic "!!!" → "Today's little joy:  ✨", "Save this one:  🤍"…

## P3: filler hashtags
Topic "Big news!!!", Instagram, Bold → "#BigNews #Big #News #BigTips #BigLife".

## P3: blog X example
X, Professional, topic "Oat milk latte now on the menu" → "New: Oat milk latte now on the menu." with no hashtags (blog says "#OatMilkLatteNowMenu #Oat").
