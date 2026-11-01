Sent: 2026-11-01 01:00 ET (Grok Orchestrator)

# QA 386: close gaps on high-demand tools (P2)

## Intent
These tools target large YouTube demand: sign PDF about 3.4M views, voice cleanup about 1.8M, PDF to Word about 0.6M. Each should beat the leaders, not just work.

## Why
QA 386: all four tools pass, but each has gaps against competitors.

## Outcome
1. sign-pdf: let each signature field use its own source, so drawn and typed can be mixed in one document.
2. noise-remover: add a strength slider and a before/after toggle; offer MP3 (and keep WAV) output; keep the input sample rate (Voice AI changes 44.1 kHz to 48 kHz). Don't change or add any AI model; this is UI and output only.
3. pdf-to-word: keep the original table widths (no narrow tables with wrapping cells); map headings to real Word heading styles.
4. ocr-pdf: check it on noisy real-world scans and tune if needed.

Source: owner
