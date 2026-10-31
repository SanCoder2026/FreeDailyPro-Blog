# Hero priority list (live heroes to replace)

Live URL pattern: `https://freedailypro.com/blog/{slug}.webp`

## P1: Third-party / competitor logos (legal risk)
| slug | problem | source |
|---|---|---|
| capture-booth-leads-in-ten-seconds | Vodafone / Nokia / Office 365 logos in scene | QA reports 296, 298 |
| publish-event-share-guest-app | Eventcube logo | QA reports 296, 298 |

## P2: Off-topic (image does not show this tool's task)
| slug | source |
|---|---|
| extract-audio-track-from-video-to-mp3 | hero CSV + live review |
| meme-generator | hero CSV + live review |
| bmr-and-macro-targets-from-your-stats | hero CSV + live review |
| branded-custom-qr-codes-with-logo-and-colors | hero CSV + live review |
| bulk-qr-codes-from-a-url-list-as-zip | hero CSV + live review |
| travel-packing-list | hero CSV + live review |
| trim-video | hero CSV + live review |
| vat-calculator | hero CSV + live review |
| audio-merger | hero CSV + live review |
| base64 | hero CSV + live review |
| calorie-calculator | hero CSV + live review |
| send-price-quotation-pdf-to-clients | hero CSV + live review |
| split-image-into-instagram-grid-tiles | hero CSV + live review |
| annotate-pdf-pages-with-text-shapes-highlights | hero CSV + live review |
| contract-templates | owner steering 2026-10-31 |
| emoji-unicode-converter | owner steering |
| event-checklist-planner | owner steering |
| find-replace | owner steering |
| inventory-tracker | owner steering |
| keyword-density | owner steering |

## P3: Baked-in text
| slug | problem | source |
|---|---|---|
| favicon-generator | "Free Favicon Generator" text painted in image | owner steering |

## P4: Duplicate / shared images (each slug needs its own)
| slugs | problem | source |
|---|---|---|
| bmi-calculator / body-fat-calculator | same image | live og:image scan |
| monthly-budget-planner / expense-tracker | same image | live og:image scan |
| travel-budget-planner / travel-itinerary-planner | same image | live og:image scan |
| brochure-flyer-maker, gradient-generator, image-filters | 3-image near-duplicate cluster | pHash scan |
| 16-slug placeholder cluster | same generic placeholder | pHash scan; all are in the 120-slug hero CSV |

The remaining slugs are in the 120-slug CSV at `Agent/claude-grok/from-claude/2026-10-29-hero-list-for-blog-bot.csv`.
