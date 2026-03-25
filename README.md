# Promethease Report Viewer Repository

Static HTML/CSS/JS project for hosting and opening Promethease report bundles online and offline.

**Live Site:** [https://xerohour.github.io/Promethease/](https://xerohour.github.io/Promethease/)

## Quick Start

### View Online
1. Open [index.html](https://xerohour.github.io/Promethease/) or [all-reports.html](https://xerohour.github.io/Promethease/all-reports.html).
2. Choose a report bundle (John or Trina, 2018/2024/2026 variants).

### View Offline
1. Clone/download the repository.
2. Open a target bundle `promethease.html` or `*_ui2.html` file directly.
3. For pages using `fetch()` (notably 2026 bundles), run:

```bash
python -m http.server 8000
# http://localhost:8000/
```

## Included Report Bundles

- `2018-promethease/`
- `2024-promethease/`
- `2026-promethease-john/`
- `2026-promethease-trina/`

## Features

- Static/offline-friendly report hosting
- UI2 report pages with search/filter controls
- Shared styling in `openai-brand.css`
- Landing and navigation pages: `index.html`, `all-reports.html`
- F1 comparison reports at repo root (`file-F1-*.html`)

## Repository Layout

- `index.html`: Landing page.
- `all-reports.html`: Aggregated report navigation.
- `openai-brand.css`: Shared visual styling.
- `20xx-promethease*/`: Versioned report bundles and assets.
- `.github/workflows/`: Pages deployment and CI workflows.
- `CHANGELOG*.md`, `RELEASE_NOTES_*.md`, `CUSTOMER_UPDATE_*.md`: Release communications.
- `agentic_kb/`: Knowledge-base submodule (managed separately).

## Local Validation Checklist

- Open changed pages in desktop and mobile widths.
- Verify UI2 filter/search behavior on 2026 pages.
- Preserve offline integrity; do not move/remove `ui2libs/` dependencies.

## Development

No build step is required; this is a static site.

```bash
# serve locally
python -m http.server 8000

# inspect local changes
git status --short
```

## Deployment

GitHub Pages deploys from `main` via `.github/workflows/static.yml`.

You can monitor CI checks with:

```bash
gh pr checks <PR_NUMBER> --watch --interval 10
```

## Documentation Map

- [CHANGELOG.md](./CHANGELOG.md)
- [CHANGELOG_KEEPACHANGELOG.md](./CHANGELOG_KEEPACHANGELOG.md)
- [RELEASE_NOTES_2026-03-02.md](./RELEASE_NOTES_2026-03-02.md)
- [RELEASE_NOTES_2026-03-03.md](./RELEASE_NOTES_2026-03-03.md)
- [CUSTOMER_UPDATE_2026-03-02.md](./CUSTOMER_UPDATE_2026-03-02.md)
- [CUSTOMER_UPDATE_2026-03-03.md](./CUSTOMER_UPDATE_2026-03-03.md)

## Contribution Notes

See [CONTRIBUTING.md](./CONTRIBUTING.md) for editing conventions, validation expectations, and PR guidance.