Sent: 2026-10-30 08:31 ET
Supersedes 2026-10-30-0829-ET-B-0118-password-generator.md
# B-0118 Password Generator: show a result before the trial wall, strength/entropy readout, labels on two controls, merge with the duplicate tool
Priority: P2      Estimated effort: 0.5–1 day      Report: #96      Source: Testing Bot (capability-gap sweep)

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
Be as good as the Bitwarden, 1Password and LastPass generators: instant result, strength shown, nothing sent anywhere.

## Why
- GA: password-generator 63 views (#33 page, 11s avg) per the analytics file. 11 seconds suggests people leave quickly.
- Report #96: clicking "Generate Password" at 0 trial uses showed no password. Competitors generate on page load with no limit. The output was verified earlier in the admin session (L-152, #86), so the logic works; the problem is the gate.
- Live competitor fetch (30 Oct, 08:30 ET):
  - **1Password** (1password.com/password-generator): choose password type (characters/memorable words), numbers and symbols toggles, generates with no limit or sign-in.
  - Bitwarden's generator page timed out on fetch, so it is not cited.
- Two controls have no accessible name: the "Exclude look-alike characters" switch (role=switch, no label) and the "How many" select (no label association).
- There is no entropy/strength readout or "time to crack". The passphrase mode exists but shows no word count or separator options in the static read.
- There is a duplicate "Password Generator & Checker" (/tool/password-strength) in the same category, which splits search intent.

## Who uses this
People creating a new account, IT admins issuing temporary passwords, and anyone replacing a reused password after a breach notice.

## Outcomes (ranked)
1. Show one password on load and on Generate without using a trial use (owner decision; same question as B-0115). Gate only bulk/copy if needed.
2. Label the switch and the "How many" select.
3. Add an entropy bits + strength bar; for passphrases, word-count and separator options.
4. Decide on one canonical tool, or cross-link the two clearly with distinct intents (generate vs check).
5. Note that generation is local (crypto.getRandomValues) next to the result.

## Constraints
Say "trial uses"/"professional tools". Never send passwords to a server.

## Test cases (ET)
- 08:27 TC-1: page 200, options visible (length 16, sets, symbols list, How many 1/3/5/10). PASS
- 08:27 TC-2: Generate at 0 trial uses → no password shown. FAIL (gate) — carry-over to admin session
- 08:27 TC-3: unlabeled controls = 2 (switch, How many select). FAIL
- 08:27 TC-4: strength/entropy readout. ABSENT
