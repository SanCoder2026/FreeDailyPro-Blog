# B-0077 Mobile load layout shift on Tip, Book Writing Toolbox and Magazine Maker
Priority: P2      Estimated effort: 30–60 min      Report: #81, #82  ·  Related: B-0072, B-0041      Source: Testing Bot

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
Tool pages on phones should not jump while they load, especially paid workflow products where a jump can push the user's tap onto the wrong control or an ad.

## Why
Load with no input, 3 loads each, 390 px, 00:05 ET:
- Tip Calculator: 0.19, 0.55, 0.19. Result/action row (`no-print mt-6 flex`, `grid grid-cols-3`) moves at about 280 ms.
- Magazine Maker: 0.28, 0.26, 0.26. The upload field (`file:text-foreground`) moves at about 300 ms.
- Book Writing Toolbox: 0.06, 0.29, 0.29. The toolbar moves at about 295 ms.
- Shared: a 0.05–0.09 shift of `container py-6 md:py-8` at about 800 ms on almost every tool tested (Find & Replace 0.089, Percentage 0.083, Tip 0.089, Book 0.062). It looks like a common layout component, so one fix may help the whole site.
- Desktop is fine for Tip and Magazine (≤ 0.07). Google counts > 0.1 as poor.

## Outcomes
Mobile load CLS < 0.1 on these three pages in 5 of 5 loads; the shared ~800 ms container shift is gone site-wide.

## Constraints
Keep ads and their count. Coordinate with B-0072 (same class of issue on Mortgage and /tools).

## Test cases
PerformanceObserver over 5 loads at 390 and 1280 per page: every run < 0.1.
