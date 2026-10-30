Sent: 2026-10-30 08:19 ET
# B-0107 Paycheck: local tax, state insurance, W-4 inputs, caps — reach SmartAsset parity
Priority: P2      Estimated effort: 1–2 days      Report: #92      Source: Testing Bot (capability-gap sweep, owner rule 30 Oct)

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
Make the take-home figure trustworthy for every US worker, including those in cities and states with extra payroll taxes. The tool should look the rates up itself, which answers ApyHub's "caller must send the rate" point on the site too.

## Why
- Report #92: federal and FICA are correct for $75k single. But FDP says city/local tax and SDI aren't included, so NYC/CA/NJ results are too high. SmartAsset covers local, SDI, SUI, family leave and W-4 inputs.
- The state "Custom rate…" option means some states may still need the user to enter a rate.

## Who uses this
Job-offer comparers, people relocating, hourly workers, HR/recruiters sharing take-home estimates.

## Outcomes (ranked)
1. **SS wage-base cap ($184,500 for 2026) and Additional Medicare 0.9%** applied and shown. Verify first; low effort.
2. **State SDI/PFL/SUI** (CA, NJ, NY, WA, MA, RI, HI…). Medium effort.
3. **Local/city income tax** (NYC, Yonkers, PA locals, OH/MD counties). Medium effort.
4. **W-4 inputs**: dependents credit, other income, extra withholding, multiple jobs. Low/medium effort.
5. **Post-tax deductions / Roth 401(k)**; hourly overtime. Low effort.
6. Label the data year and a "rates checked on" date. Low effort.

## Constraints
Not tax advice; trial-use rules unchanged.

## Test cases
| # | Inputs | Expected |
|---|---|---|
| 1 | $75k single bi-weekly, FL | $2,368.94 (unchanged) |
| 2 | $250k single | SS stops at $184,500 (= $11,439); Additional Medicare on $50k |
| 3 | $75k, NY + NYC | city tax and NY SDI/PFL line items shown |
| 4 | 2 dependents under 17 | federal tax reduced by the child tax credit |
