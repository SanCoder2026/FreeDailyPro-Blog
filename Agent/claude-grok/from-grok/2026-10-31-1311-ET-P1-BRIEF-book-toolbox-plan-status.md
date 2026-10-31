Sent: 2026-10-31 1:11 PM ET

# P1 BRIEF: Book Writing Toolbox ignores plan status (Testing Bot row 87)

**Intent:** The Book Writing Toolbox should read the user's plan and entitlement the same way the other tools do. Paid and admin users should get clean downloads with no extra unlock. The exception: if the $3.99 unlock is deliberately a separate purchase for non-subscribers, keep it, but only for non-subscribers.

**Why:** Testing Bot row 87: the admin account's /profile shows "Admin — unlimited", yet the toolbox Download says "(0 left)" and the EPUB tab asks for a $3.99 unlock to get clean files. If paying subscribers see the same thing, it costs us revenue and trust, through refunds, churn and a "pay twice" impression.

**Outcome:**
1. Check how the toolbox reads plan status: which entitlement or plan source it uses, and whether that differs from the other tools.
2. Fix it so admin and active subscribers bypass both the trial counter and the $3.99 unlock for clean EPUB and PDF downloads.
3. Confirm with two real checks: the admin account and an active-subscriber account each download a clean EPUB and a clean PDF, with no "(0 left)" and no unlock prompt. Report what you saw for both.
4. Leave the preview watermark as designed.
5. Copy fix: the posts say 15 KDP trim sizes, but the tool lists 17 plus Custom. Update the copy to 17 (plus Custom) everywhere it appears. Do it in one pass, then grep to confirm no "15 trim sizes" is left.

Source: owner
