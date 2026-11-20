Sent: 2026-11-20 08:40 ET

# FDP-21 Sign PDF: test cases for after the fix

| ID | Steps | Expected |
|---|---|---|
| SP-01 | contract.pdf, auto signature, Signature + Date + Full Name, record | all stamped where placed; record SHA-256 = input |
| SP-02 | Other-party Signature + Date | form fields in output; copy everywhere matches |
| SP-03 | Open SP-02 output as other party | "fields are waiting" toast; both signers in output |
| SP-04 | Keyboard only: add and place a Signature, download | possible without a mouse |
| SP-05 | Screen reader on style buttons | each named by style; selected state announced |
| SP-06 | Initial on All pages / range 2-3 | correct pages only |
| SP-07 | Rotated page | upright mark |
| SP-08 | Draw / Import PNG / Import JPG | each stamped |
| SP-09 | Missing signature / unplaced field | inline errors, announced |
| SP-10 | Password PDF, damaged PDF | prompt / repair hint |
| SP-11 | Existing AcroForm PDF | original fields kept |
| SP-12 | DD/MM/YYYY | 19/11/2026 style |
| SP-13 | With uses: Download ×2 | 1 use, no double charge, bytes match |
| SP-14 | At 0: Download | cap dialog → Premium Day Pass $3 → email prompt; work kept |
| SP-15 | iPhone SE | table fits; Download reachable |
| SP-16 | Video, FAQ, blog | current UI, trial-use wording, consistent other-party explanation |
