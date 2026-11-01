Sent: 2026-11-01 00:55 ET (Grok Orchestrator)

# Redirect /tool/fill-pdf-form

## Intent
People searching "fill PDF form" land on the working tool.

## Why
QA 385: /tool/fill-pdf-form returns 404, while /tool/fillable-forms passes (partial fill keeps the other fields, no null/undefined values).

## Outcome
301 redirect /tool/fill-pdf-form to /tool/fillable-forms. Also confirm how blank fields appear in the filled output (QA couldn't test it, because the test form came prefilled).

Source: owner
