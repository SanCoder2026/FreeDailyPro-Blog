Sent: 2026-11-21 15:54 ET

# Live functional findings (FDP-70)

- P1: size limit exceeded after the badge re-encode (63,162 / 51,312 / 79,577 B for "Under 50 KB"; 101,400 B for "Under 100 KB"); toast shows the pre-badge size (limits.json, left-firefox.json).
- P1: no 300 DPI in any saved JPEG (JFIF units 0, 1:1).
- P1: one charge per page load; 13 downloads = 2 uses (left-firefox.json); 5 downloads at 10/10 after the jump (limits.json).
- Template pixel sizes and sheet layouts correct; gate at 10/10 on a fresh page works; auto-fit runs locally, message overclaims (P2).
