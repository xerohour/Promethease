# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

No changes yet.

## [1.2.0] - 2026-03-03

### Added

- Added a right-side Search + Filters panel for 2026 UI2 report pages.
- Added guided help steps for filter usage in 2026 UI2 pages.

### Changed

- Refreshed index, all-reports, and 2026 UI2 pages with shared OpenAI-branded styling.
- Improved 2026 UI2 filter interactions to better match classic Promethease behavior.

### Fixed

- Removed Intro.js runtime-only classes from static filter markup to avoid overlay/tooltip render conflicts.

## [1.1.0] - 2026-03-02

### Added

- Added 2026 Promethease report bundles for John and Trina.
- Added an aggregated reports index page for navigation.
- Added offline report archives and offline usage documentation.
- Added a vaporwave/Matrix-themed landing experience.

### Changed

- Reorganized Promethease report assets and UI2 viewer bundle structure.
- Improved deployment workflow with GitHub Actions and explicit Vercel deploy triggers.

### Fixed

- Fixed 2026 UI2 page JavaScript/CSS brace syntax issues affecting rendering.

[Unreleased]: https://github.com/xerohour/Promethease/compare/v1.2.0...HEAD
[1.2.0]: https://github.com/xerohour/Promethease/releases/tag/v1.2.0
[1.1.0]: https://github.com/xerohour/Promethease/releases/tag/v1.1.0
