Sent: 2026-10-30 11:18 ET

# B-0144 Passport photo: labelled controls, more countries, pixel readout
Priority: P2 · Estimated effort: S–M · Report: #109 · Source: QA sweep + live competitor fetch 2026-10-30 11:16 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Help people get an accepted photo the first time, for their country, with an exact pixel size.

## Why
There are 8 presets. IDPhoto4You and Persofoto cover many countries and run biometric checks. Our two comboboxes have no accessible name, and the output pixel size is not shown before the gated download.

## Who uses this
Travellers and visa applicants (989 GSC impressions).

## Outcomes (ranked)
1. Label the Photo Size and File size limit controls. 2. Show the output pixels and DPI (e.g. US 600×600 at 300 dpi) before download. 3. Add the next most-requested countries with their head-size rules.

## Constraints
Keep the head-guide percentages (US 50–69%, EU 70–80%); runs on device.

## Test cases
get_by_label("Photo Size") finds the control. The US preset shows 600×600. The EU preset shows 413×531 at 300 dpi.
