Sent: 2026-11-21 16:17 ET

# FDP-72 3D Mesh Converter (mesh-3d-converter): deep test report for Claude

- **Written:** 2026-11-21 16:16 EST (box `date`, ET). Testing ran 2026-11-21 16:04–16:14 EST.
- **Tool:** https://www.freedailypro.com/tool/mesh-3d-converter
  - TEST-ORDER row 72: **Professional Tool**, 3D & CAD Files. Plan note "test-plan (unranked): GSC top-50 SEO backfill 13". **Duplicate group C46** (with stl-ascii-binary-converter #67 and mesh-3d-viewer #386).
  - Trial strip "Trial: 10 uses/day"; Quick Buy Day Pass $1 / Monthly $4.99 (all 6 geo contexts).
  - Video VmKe3Isdqh8 (embedded, 78 s, uploaded 2026-09-23). The page links blogs /blog/stl-ascii-binary-converter and /blog/mesh-3d-viewer (both 200, written for the sibling tools). The tool's own post **/blog/mesh-3d-converter** "Converting 3D Print Files Between STL, OBJ, and PLY" exists (200) but is **not linked** from the page.
  - **GSC data is not available.** No API/MCP testing.
- **How it works (live + `Mesh3DConverter-CXAH8d0k.js`, shared `mesh3d-C14zW8wv.js` (same file as #67), `MeshReport`, `threemf`):**
  - Drop one file (drop zone `gateAtDownload`); the format comes from the extension. Choose **Convert to** (7 outputs) and **Model units**; for OBJ/PLY the units are guessed from size.
  - Options: **Reduce triangles** (100→5 %), **Repair** "Fill small holes" (shown only when not watertight), **Scale** (keep / factor / largest side).
  - **Convert** (no usage call) shows the report: vertices, triangles, bbox in units + inches/mm, watertight, volume/area, print-bed fit, note, output size.
  - **Download** (gated), **Save to Google Drive** (gated), **Save to my cloud storage** (sign-in + add-on).
- **Testers:**
  - Desk: page copy (7 FAQs, how-to, when/when not, tips, limitations, privacy), JSON-LD, 3 blogs, JS.
  - Playwright, guest contexts. Test meshes generated with trimesh (make-testfiles.py):
    - 20 mm cube; icosphere 1,280 tris; 81,920-tri scan sphere; open box (1 hole); cube with a fin (non-manifold edge);
    - each in STL bin/ASCII, OBJ, PLY bin (LE + BE)/ASCII, GLB, 3MF; plus a .gltf and a non-mesh file.
  - Runs: `zero.json` (at 10/10), `cases.json` (at 10/10, report only), `extra.json` (setting carry-over; Drive/cloud buttons at 10/10), `left-firefox.json` (start 0/10, 16 jobs in one page), `quickbuy.json`, `drive.json`.
  - Every output was re-read with trimesh + raw header checks (px72-analyze.py).
  - Video frame sheet; matrix: 10 devices, 10 locales + /ar probe, 6 geo contexts, axe.
  - **Banner, layout and locale findings were checked against the screenshots, not the script flags.**
- **Constraints kept:** guest only. No sign-in, card or email entered (Quick Buy stopped at the email box and at Stripe; the cloud dialog stopped at "Sign in"). No ad clicks. No site or repo changes. Downloads parsed, never executed.
- **Sign-in (untested):** Open from Google Drive (Google sign-in popup, closed); Save to my cloud storage (sign-in + $4.99/month add-on); Save to Google Drive with uses left; paid-pass output. Rows added to SIGNIN-NEEDED.md.
- **RERUN-AFTER-RESET:** none needed.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders. Each item says why it matters for a maker who needs an STL for the slicer, a GLB for the web or a lighter scan, and whether the page is set up to turn that into a pass.

**Owner context:** copy and results count as trial uses (Oct 30). Per-page-load charging is P1; a full-quality result at 0 is a pending owner question; a real save or download at 0 is P1 (Nov 21, corrected 1:19 PM).

**P0:** none.

**P1:**
1. **Charging happens once per page load; after it, every conversion in that page downloads free.**
   - left-firefox.json (start 0/10): the first Download sends one `usage.log` POST. The local counter then shows **10/10** (the device's server count).
   - The same page then saved **13 more files with no POST and no dialog at 10/10**: all 7 output formats, 3MF→OBJ, GLB→STL, big-endian PLY→STL, hole fill, 50 % reduction, ×25.4 scale, largest-side 50 mm → 3MF, and inches → GLB.
   - After a reload, Download opens the cap dialog (L15). Same pattern as #67 (shared code).
   - **Fix direction:** charge per Download of a new result, not per page load.

**Owner question:** none.
- At the cap the report (counts, bbox, watertight, volume) is visible, but no geometry or preview is shown, so this is not a full result. Download and Save to Google Drive are gated on a fresh page.

**P2 — where to look:**
- **The Reduce-triangles setting carries over to the next file and silently ruins simple models** (extra.json, X-keep50-carried-to-cube.png).
  - Scan at keep 50 % → Change file → 20 mm cube. The label still says "keep 50 %". Convert gives **5 vertices, 6 triangles, volume 2,963 mm³** (the cube is 8,000 mm³), still marked "✓ Watertight", with only a small "Reduced from 12 to 6 triangles" note.
  - In the left run, three later jobs (×25.4 STL, largest-side 3MF, inches GLB) were all cut from 12 to 6 triangles this way.
  - Reset Reduce to 100 % on a new file, as the page already does for Scale and Repair. Consider refusing reductions that change volume by more than a few percent, or warning when they do. The slider copy "keeping the shape, the outline and closed surfaces" overpromises on low-poly parts.
- **The page contradicts itself and the live tool:**
  - FAQ "Can this convert a file into GLB and then back out again? **Not yet — GLB is currently export-only**". GLB input works (sphere.glb → STL, L08), and another FAQ says it reads GLB.
  - "When not to use it": "**It also will not fix holes it reports**". "Fill small holes" exists and worked (open box → watertight, 8,000 mm³).
  - Two colour FAQs say the same thing ("Does this preserve materials…" / "Will I keep my colours…").
- **Blogs:** /blog/mesh-3d-converter is orphaned (not linked from the page). It says the converter "tells you this; it does not repair it", which is outdated (Fill small holes) and omits Scale/Repair. The two linked blogs belong to the sibling tools.
- **iPhone SE (320 px): 95 px horizontal overflow.** The long H1 "3D Mesh Converter (STL/OBJ/PLY/GLB/3MF)" pushes the share and install icons off-screen (only the star is visible in iphone-se-fold.png; scrollWidth 415). Wrap the action icons under the H1 on narrow screens.
- **Video VmKe3Isdqh8** shows an older UI: "Source format" selector, no 3MF, no units/reduce/repair/scale/bed check, H1 without 3MF, "Search 200+ tools". Title "Free Step-by-Step Walkthrough", "Try … free", tags "free online tools", "PDF tools", end card "200+ Free Productivity Tools". VideoObject name "…online & no-login".
- **Duplicate group C46:** stl-ascii-binary-converter (#67) does a subset of this tool (STL bin↔ASCII) with the same `mesh3d` code. Merging it as a mode, or cross-linking it as "STL only", is reasonable.
- **SEO:** the title "Convert 3D Mesh Files Online - STL, OBJ, PLY, GLB, 3MF" lacks the "| FreeDailyPro" suffix used elsewhere. The meta is fine.

**P3:**
- Units are always "Millimetres" for STL input (no guess, unlike OBJ/PLY). This is fine, but the report shows "20 × 20 × 20 m" for a GLB until changed (correct for glTF).
- "Couldn't read" vs "No triangles found…" messages are clear. A .gltf gets a toast "can't be used here"; the copy could suggest packing it to .glb.
- axe desktop label-content-name-mismatch (serious), region (moderate); Pixel 7 color-contrast ×1 (ad caption; keep reserved ad slots, fix the caption colour). ja desktop 1369 px. de-DE/fr-FR consent banner.

## Intent

A maker or developer needs the same geometry in another format, at the right scale, with a quick printability check. Conversions are exact and the report is accurate; the gate charges once per page, and a leftover slider setting can ruin the next file.

## What works (verified with trimesh)

- **All 7 outputs from the cube OBJ:** STL binary (84 + 50×12 bytes, normals set) and ASCII; PLY binary little-endian and ASCII (8 verts, merged); GLB scaled mm→m (extents 0.02); 3MF `unit="millimeter"`. Each is 12 tris, watertight, 8,000 mm³.
- **Inputs:** 3MF → OBJ (642 v / 1,280 f, no vn/vt); GLB → STL; big-endian binary PLY → ASCII STL. All are exact (sphere volume 4,152.74 = source).
- **Report accuracy:** counts, bbox, volume and area match trimesh for every case. Open box "4 open edges"; fin "2 open edges and 1 edge(s) shared by 3+ faces" + "can't be fixed by filling holes".
- **Repair:** open box → 14 tris, watertight, 8,000 mm³ ("Filled 1 hole (4 triangles added)").
- **Reduce:** scan 81,920 → 40,960 tris, still watertight, volume 523,494 vs 523,528 source (−0.01 %).
- **Scale:** ×25.4 → 508 mm; largest side 50 → 2.5×; inches → GLB 0.508 m. Factor 0 → "Enter a number above zero.", Convert disabled.
- **Guards:** .gltf refused (toast); non-mesh → "No triangles found in this file…".
- **Gate on a fresh page at 10/10:** Download and Save to Google Drive open the cap dialog. Quick Buy: Day Pass → email (stopped), Monthly → Stripe (stopped).

## 22 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Capability | PASS | 5 inputs, 7 outputs, units, reduce, repair, scale, report. |
| 2 | Completeness | PASS (minor) | Geometry only (documented). |
| 3 | Ease of use | PARTIAL | Reduce setting carries to the next file. |
| 4 | Layout | PARTIAL | iPhone SE 95 px overflow (header icons off-screen). |
| 5 | Payment process | PASS | Strip + Quick Buy; email/Stripe reached (stopped). |
| 6 | Information correct | **FAIL** | "GLB export-only", "will not fix holes" false. |
| 7 | Indexing | PASS | 200, canonical self, hreflang set. |
| 8 | SEO | PASS (minor) | Title suffix missing. |
| 9 | Blog | PARTIAL | Own blog orphaned and outdated; linked blogs are the siblings'. |
| 10 | YouTube video | PASS | VmKe3Isdqh8 embedded. |
| 11 | FAQ / guide correct | FAIL | GLB FAQ contradicts the tool; duplicate colour FAQ. |
| 12 | Video shows current capability | FAIL | Old UI; "free" wording. |
| 13 | Storage | N/A (sign-in) | Cloud storage needs sign-in + add-on. |
| 14 | Sharing | N/A (tool link) | "Share this tool" only. |
| 15 | Downloads | PASS | All formats exact. |
| 16 | Usage count | **FAIL (P1)** | One charge per page load. |
| 17 | Categorization in section | PASS | 3D & CAD Files / Professional. |
| 18 | Correct section of site | PASS | Links 200 (mesh-3d-viewer, stl-ascii-binary-converter, category). |
| 19 | AI need and demand | PASS | "obj to stl", "stl to glb", "3mf converter". |
| 20 | Merge better? | Partly | Absorb stl-ascii-binary-converter as a mode (C46). |
| 21 | Remove? | No | GSC top-50 backfill; main tool of C46. |
| 22 | Duplicates | C46 | See 20. |

## After fixes, rerun

- `TRIES=40 px72-live.js left` (each download charged) and `px72-extra.js` (Reduce resets to 100 % on a new file).
