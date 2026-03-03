# Promethease Offline Report Bundles

This repository contains two self-contained Promethease report bundles:

- `2018-promethease/`
- `2024-promethease/`

## Open A Report

1. Open the desired folder.
2. Open `promethease.html` in a web browser.

If double-clicking shows a blank page, open your browser first and use `File -> Open...` to open that folder's `promethease.html`.

## Folder Layout

- `promethease.html`: Main entry point for the offline report viewer.
- `ui2libs/`: Local JS/CSS/font/image dependencies used for offline mode.
- `promethease_data/` (2024 bundle): Report data files and generated assets.
- `report_metadata.txt` (2018 bundle): Original metadata and notes.

## Notes

- Keep each bundle folder intact. Moving or deleting files can break local links.
- These reports can run fully offline using the bundled `ui2libs` assets.

## Release Notes

- [CHANGELOG.md](./CHANGELOG.md): Main user-facing changelog summary.
- [RELEASE_NOTES_2026-03-02.md](./RELEASE_NOTES_2026-03-02.md): Concise GitHub-style release notes.
- [CUSTOMER_UPDATE_2026-03-02.md](./CUSTOMER_UPDATE_2026-03-02.md): Customer-facing product update copy.
- [CHANGELOG_KEEPACHANGELOG.md](./CHANGELOG_KEEPACHANGELOG.md): Keep a Changelog + SemVer formatted changelog.
