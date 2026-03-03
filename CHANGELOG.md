# Changelog

All notable user-facing changes to this project are documented here.

## 2026-03-03

### New

- Added a full right-side Search + Filters panel to 2026 UI2 report pages, including text search, repute filter, and minimum magnitude filter.
- Added in-page guided help for the new filter workflow on 2026 UI2 report views.

### Improvements

- Refreshed report pages with consistent OpenAI-branded styling across index, all-reports, and 2026 UI2 experiences.
- Improved 2026 UI2 layout behavior to better match classic Promethease-style filter interactions.

### Fixes

- Removed transient Intro.js runtime state classes from static filter markup so controls render and behave correctly when Intro.js styles load.

### Notes

- Added release-note and customer-update artifacts for this release.

## 2026-03-02

### New

- Added 2026 Promethease report bundles for John and Trina.
- Added an aggregated reports index page to navigate available report sets.
- Added offline report archives and documentation for offline usage.
- Added a vaporwave-style landing/index experience with Matrix-themed media.

### Improvements

- Reorganized Promethease report assets and UI2 viewer bundles for cleaner structure.
- Improved deploy flow with GitHub Actions and explicit Vercel deployment triggers.

### Fixes

- Fixed 2026 UI2 page JavaScript/CSS brace syntax issues that could break page rendering.

### Notes

- Internal/session artifact commits were intentionally excluded from user-facing notes.
