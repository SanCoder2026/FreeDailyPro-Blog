Sent: 2026-11-20 08:40 ET

# FreeDailyPro device / platform / locale / a11y matrix

`run-matrix.js` loads one tool page on 10 device/browser profiles, every hreflang language version, six country/timezone contexts and two axe-core runs. It writes screenshots and one JSON result file per run.

## Setup (already done on this box)
```
cd /workspace/deep/tools-env
npm i playwright axe-core          # already installed
npx playwright install chromium firefox webkit
```
WebKit needs some system libraries that `playwright install-deps` could not get, because apt's Debian mirror was failing signature checks. Instead:
- The missing `.so` files were taken from Debian trixie `.deb`s in `debs/`, extracted into `wklibs/`, and copied into `~/.cache/ms-playwright/webkit-2388/minibrowser-wpe/sys/lib/`.
- WebKit's TLS comes from `giomods/libgiognutls.so`. The script sets `GIO_EXTRA_MODULES` to `./giomods` automatically.

If Playwright updates WebKit to a new build folder, repeat the copy into the new `minibrowser-wpe/sys/lib`.

## Run
```
cd /workspace/deep/tools-env
node run-matrix.js <config.json>                         # everything
node run-matrix.js <config.json> --only=devices          # or locales,geo,a11y
node run-matrix.js <config.json> --only=devices "--devices=iPhone SE,Pixel 7"
```
Output goes to `<outDir>/devices|locales|geo|a11y/*.png` and `<outDir>/matrix-results[-only].json`. A full run takes about 8 minutes.

## Config (copy `config.roman-numeral-converter.json` for the next tool)
- `url`: the English tool URL. hreflang alternates are discovered from its server HTML.
- `outDir`: the tool's folder, e.g. `/workspace/deep/02-<slug>`.
- `keySelectors`: CSS for the main inputs and buttons. These are checked for ad overlap and font size.
- `resultSelectors`: CSS for the result element(s). These are used for above-the-fold and overlap checks.
- `functional[]`: typing-only steps. Each step has:
  - `fill` (selector) and `value`
  - either `expectValueOf` (an input's value) or `expectTextIn` (an element's text; `>> nth=N` is allowed)
  - `expect`
  - `match`: `exact` (default), `includes`, or `digits` (compares digits only, e.g. "2,026" vs "2026")
- `trialRegex`: text that identifies the trial-uses strip.
- `extraLocaleUrls`: URLs to probe even if they are not in hreflang, e.g. `/ar/` for an RTL check.
- Optional:
  - `devices[]`: overrides the default device matrix.
  - `geoContexts[]`: overrides the default locale/timezone contexts.
  - `adSelectors`, `mainSelector`, `settleMs`.

## Safety rules built in
- The script only navigates, types and reads.
- It never clicks ads, Copy, Download, Buy, Pass or Checkout. It never signs in and makes no API calls.
- Each fresh context is a new guest device. Typing alone does not spend a trial use on tools that charge on export. For tools that charge on Run or Generate, leave `functional` empty or accept that each context spends one trial use.

## Known limits
- This is headless emulation: device UA, viewport, DPR and touch, on Linux engines. It is not real iOS Safari or real Android hardware.
- CLS is measured only where `layout-shift` is supported (Chromium). Firefox and WebKit show `null`.
- Geo contexts change locale, timezone, geolocation and Accept-Language only. The egress IP stays in the US, so IP-based geo (real EU consent, currency by IP) is not tested.
