# Grok workspace

Grok may create, overwrite and delete any file under this folder.

Layout (all folders are tracked with .gitkeep so they exist after every pull):
- posts/        new or rewritten posts
- images/       hero images for those posts
- scripts/      helper scripts
- deploy-notes/ CLAUDE-*.md handoffs

Paths, relative to the repo root (in Grok's sandbox the repo is /workspace/artifacts/FreeDailyPro-Blog):
- Agent/site/grok-workspace/
- Agent/site/tool-heroes/   (tool hero images)
- Agent/images/             (shared images)
- site-blog-pack/           (rules and uniqueness scripts, repo root)

Always run commands from the repo root and use these relative paths.
