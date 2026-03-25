# Tech Stack

## Overview
This project is a static-site repository for hosting and viewing Promethease report bundles online and offline, with a compatibility-first approach across legacy and UI2 report formats.

## Core Architecture
- **Type:** Static HTML/CSS/JS repository (no application build pipeline required)
- **Delivery model:** File-based bundles + GitHub Pages publishing
- **Organization:** Versioned report bundle directories with shared top-level navigation and styling

## Frontend Technologies
- **HTML5** for report and navigation pages
- **CSS** for shared theming and presentation (`openai-brand.css` plus bundled styles)
- **JavaScript** for interactive filtering/search/navigation behavior in report UI pages

## UI Compatibility Layer (Vendored Libraries)
To preserve historical bundle behavior and offline reliability, the project retains vendored UI dependencies, including:
- **Bootstrap 3**
- **Jasny Bootstrap**
- **Intro.js**
- **jQuery / jQuery UI**
- **DataTables and related filtering plugins**
- **Chart.js / Chartist** (where present in bundle assets)

## Report Bundle Model
- Multiple bundle eras are maintained side-by-side (e.g., 2018, 2024, 2026 variants).
- Bundles are designed to remain self-contained for offline usage.
- Some newer pages rely on local fetch behavior and should be served locally for full functionality.

## Local Development and Validation Tooling
- **Python stdlib HTTP server** for local serving:
  - `python -m http.server 8000`
- **Git** for source control and change review
- **Manual browser validation** for user-visible behavior checks (desktop/mobile and UI2 filter/search behavior)

## Automation and Deployment
- **GitHub Actions** workflows for CI checks and Pages deployment
- **GitHub Pages** for static hosting/publishing
- Deployment workflow includes curated publish artifact selection for required site/report assets

## Data and Asset Strategy
- Report artifacts, supporting HTML pages, and assets are stored in-repo.
- UI/library assets are vendored to preserve offline and compatibility behavior.
- Bundle path integrity is treated as a technical requirement (avoid moving/removing required sibling dependencies).

## Supporting Scripts and Utilities
- Repository includes lightweight Python utilities (e.g., genome operations helper scripts) for ancillary tasks.
- No server runtime framework, package manager lockchain, or compiled runtime is required for core report hosting.

## Constraints and Compatibility Commitments
- Maintain compatibility with legacy UI2 pages and their dependency expectations.
- Prefer minimal, targeted edits over broad refactors of generated report files.
- Preserve offline-friendly bundle structure and pathing.
