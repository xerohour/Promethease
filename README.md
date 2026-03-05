# Promethease Report Viewer Repository

Static HTML/CSS/JS project for hosting and opening Promethease report bundles both online and offline.

## Included Report Bundles

- `2018-promethease/`
- `2024-promethease/`
- `2026-promethease-john/`
- `2026-promethease-trina/`

## Quick Start

1. From the repository root, run `python -m http.server 8000`.
2. Open `http://localhost:8000/`.
3. Use `index.html` or `all-reports.html` to open a report.

Direct file open also works for most pages: open the target bundle's `promethease.html` in your browser.

## Repository Layout

- `index.html`: Home/landing page.
- `all-reports.html`: Aggregated report navigation.
- `openai-brand.css`: Shared brand styling tokens.
- `20xx-promethease*/`: Versioned report bundles and UI2 assets.
- `.github/workflows/`: Pages deployment and note-check automation.
- `CHANGELOG*.md`, `RELEASE_NOTES_*.md`, `CUSTOMER_UPDATE_*.md`: Release communications.
- `agentic_kb/`: Knowledge-base submodule (managed separately).

## Local Validation Checklist

- Open each changed page in desktop and mobile widths.
- Verify UI2 filter/search behavior for `2026-promethease-*` pages after JS/CSS edits.
- Confirm offline integrity: do not remove/move `ui2libs/` dependencies inside bundles.

## Documentation Map

- [CHANGELOG.md](./CHANGELOG.md): Human-readable user-facing change summary.
- [CHANGELOG_KEEPACHANGELOG.md](./CHANGELOG_KEEPACHANGELOG.md): Keep a Changelog + SemVer format.
- [RELEASE_NOTES_2026-03-02.md](./RELEASE_NOTES_2026-03-02.md): Release notes snapshot.
- [RELEASE_NOTES_2026-03-03.md](./RELEASE_NOTES_2026-03-03.md): Release notes snapshot.
- [CUSTOMER_UPDATE_2026-03-02.md](./CUSTOMER_UPDATE_2026-03-02.md): Customer communication draft.
- [CUSTOMER_UPDATE_2026-03-03.md](./CUSTOMER_UPDATE_2026-03-03.md): Customer communication draft.

## Contribution Notes

See [CONTRIBUTING.md](./CONTRIBUTING.md) for editing conventions, validation expectations, and PR guidance.
