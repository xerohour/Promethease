# Memento: GitHub Pages Deployment Recovery

Date: 2026-03-05
Deployment: https://github.com/xerohour/Promethease/deployments/github-pages

## Context

GitHub Pages deployments were failing with upstream transport/reset errors and then `actions/configure-pages` failures.

## Work Performed

1. Updated `.github/workflows/static.yml` to avoid uploading the full repository.
2. Added a build step that creates `_site` and includes only required site assets and report bundles.
3. Changed `actions/upload-pages-artifact` path from `.` to `_site`.
4. Added `enablement: true` for `actions/configure-pages@v5`.
5. Enabled Pages via API with workflow build type (`build_type: workflow`) for `xerohour/Promethease`.
6. Re-ran failed deployment workflow run `22738323485`.

## Outcome

- Pages deployment workflow completed successfully.
- Deploy job ID: `65946459038`
- Successful run: https://github.com/xerohour/Promethease/actions/runs/22738323485

## Related Commits

- `3b4cc6f` Limit Pages artifact to site assets only
- `9cc725e` Enable GitHub Pages during deploy workflow
