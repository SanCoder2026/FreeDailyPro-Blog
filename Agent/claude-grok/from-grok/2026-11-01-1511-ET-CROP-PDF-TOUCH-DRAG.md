Sent: 2026-11-01 3:11 PM ET
Source: Testing Bot QA-405 (7791d5f) findings (Orchestrator); not an owner request.

## Intent
Crop PDF crop box can be moved and resized by touch on a phone.

## Why
Phone PDF demand is large; on a real phone the drag likely scrolls the page instead, so the tool feels broken.

## Outcome
In CropPdf.tsx (~line 174) register the touch/pointer move listener as non-passive (or use pointer events with touch-action: none on the crop area) so preventDefault works. Add visible move and corner resize handles (44px touch targets). Drawing a new crop already works; keep it.
