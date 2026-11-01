Sent: 2026-11-01 08:26 AM ET

# P1 sign-in: signed-out /profile auto-redirects to Google OAuth

**Intent:** Signing in with an email link has to work for users who can't, or don't want to, use Google.

**Why:** When you're signed out, /profile shows the email-link form ("or, if Google isn't available where you are"). Then, 1-3 seconds after the page loads, it navigates by itself to accounts.google.com (redirect_uri /api/oauth/callback) without any click. Anyone typing an email loses the form. Our Testing Bot was blocked by this on Nov 1 at 8:25 AM ET.

**Outcome:** No automatic redirect. Google OAuth starts only when someone clicks Continue with Google. The email field stays usable, and it sends the magic link. Also check for a One Tap or auto-select prompt, or an effect that fires a redirect when there's no session.

Source: owner
