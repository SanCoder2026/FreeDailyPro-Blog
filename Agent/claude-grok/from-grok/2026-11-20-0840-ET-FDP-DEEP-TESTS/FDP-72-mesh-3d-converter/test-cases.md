Sent: 2026-11-21 16:17 ET

# FDP-72 test cases

| ID | Input / action | Expected | Result |
|---|---|---|---|
| Z01–Z02 | 10/10: cube OBJ → STL; scan → GLB 50 % | Report; Download gated | Report shown; cap dialog (PASS) |
| C01–C02 | .gltf; non-mesh .stl | Refuse / message | PASS |
| C03–C05 | Open box report; fill; fin | Open/non-manifold counts; fill | PASS |
| C06–C08 | BE PLY, 3MF, GLB reports | Correct counts/units | PASS (GLB in metres) |
| C09 | Scale factor 0 | Blocked | PASS |
| X-carry | Scan 50 % → new file cube | Reset to 100 % | **Carried; cube → 6 tris (P2)** |
| X-drive/cloud | Save to Google Drive / cloud at 10/10 | Gate / sign-in | Cap dialog / sign-in + add-on |
| L01–L06 | 0/10: cube OBJ → 6 other formats | Exact; 1 use each | Exact; **1 POST total (P1)** |
| L07–L09 | 3MF→OBJ, GLB→STL, BE PLY→ASCII STL | Exact | PASS |
| L10–L11 | Fill hole; reduce 50 % | Watertight; half tris | PASS |
| L12–L14 | ×25.4; largest 50 → 3MF; inches → GLB | Scaled cube | Scale PASS; **cut to 6 tris by carried 50 % (P2)** |
| L15–L16 | Reload → Download | Gate at 10/10 | Cap dialog (PASS) |
| Q / Drive | Quick Buy; Open from Google Drive | Email / Stripe; sign-in | Stopped; popup closed |
| M | 10 devices, 10 locales + /ar, 6 geo, axe | Usable | iPhone SE overflow (P2); rest PASS |
