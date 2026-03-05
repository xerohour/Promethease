# Memento: GitHub Pages Deployment Transport Failure Mitigation

Date: 2026-03-05
Related issue: https://github.com/xerohour/Promethease/deployments/github-pages
Related commit: fb52c73

## Context

GitHub Pages deployment reported upstream transport failure (`upstream connect error`, `connection refused`, delayed connect).

## Investigation

1. Reviewed Pages workflow configuration in `.github/workflows/static.yml`.
2. Confirmed workflow uploaded the entire repository (`path: '.'`).
3. Measured repository size locally (~3.27 GB), including large cache/artifact directories not needed for site hosting.
4. Determined full-repo upload likely exceeded practical Pages artifact constraints and increased probability of opaque deploy transport failures.

## Fix Applied

1. Added a build step to create a minimal `_site` publish artifact.
2. Included only required Pages assets:
   - `index.html`, `all-reports.html`, `openai-brand.css`
   - `matrix-soundtrack.mp3`, `matrix-theme.mid`
   - root `Promethease_*` files referenced by report navigation
   - report bundle directories: `2018-promethease/`, `2024-promethease/`, `2026-promethease-john/`, `2026-promethease-trina/`
3. Updated `actions/upload-pages-artifact` path from `.` to `_site`.

## Outcome

- Workflow now publishes a constrained site payload instead of full repository contents.
- This reduces deployment artifact size and should mitigate upstream transport failures during Pages deploy.

## Notes

- Push/merge actions were blocked temporarily by GitHub auth/web login instability during this session and need completion once auth is stable.
