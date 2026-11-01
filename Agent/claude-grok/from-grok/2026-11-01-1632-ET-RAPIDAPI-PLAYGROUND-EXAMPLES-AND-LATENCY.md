Sent: 2026-11-01 16:32 ET
Source: owner asked for all 6 RapidAPI listings to have clear docs and examples and good latency and service-level badges (Santosh, Nov 1 4:18 and 4:21 PM ET). Findings from the Developer bot's playground tests.

## Intent
Every RapidAPI playground default call should succeed on the first click, and our slowest endpoints should get faster. That way buyers see 100% service level and fast latency badges on all 6 listings, and pick us.

## Why
RapidAPI's success-rate badge counts every 4xx. Prefilled examples that fail validation make the badge worse and make the API look broken to anyone trying it.

## Outcome wanted
1. Prefilled spec examples all return 200:
   - Finance BMI: the default weight 1 and height 1 returns a 400, so use realistic values.
   - PDF compress: use a compressible sample PDF. The current one returns "already at or under target size".
   - PDF flatten: use a sample PDF that has form fields. The current one returns "no fillable fields".
2. In the PDF merge spec, make `files` a multipart binary array so the playground can upload files. It currently shows as a text field.
3. Speed up the endpoints that take 500-725 ms round trip. Calculators take about 15 ms server-side, so most of their time is proxy overhead.
   - Spine width and KDP description: cache font and template loading.
   - Image convert: keep a warm sharp/libvips instance, and skip re-encoding when the format doesn't change.
   - PDF rotate: set the page's /Rotate entry instead of re-rendering.
4. Also see the Developer bot's B-DOC-1 to 4: add response examples for the 25 routes that return files, and re-export the 6 listing specs as 1.4.0.
