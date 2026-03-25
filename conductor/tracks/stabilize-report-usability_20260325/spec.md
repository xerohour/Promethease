# Specification: Stabilize and improve report usability across all bundles (desktop + mobile) while preserving legacy UI2 compatibility and offline behavior.

## Objective
Improve end-user report usability and navigation consistency across the repository while preserving legacy compatibility and offline reliability.

## Scope
- Top-level navigation surfaces (index.html, ll-reports.html).
- Bundle entry points (promethease.html in versioned directories).
- UI2 report usability behavior that affects find/filter flows.
- Responsive/mobile usability improvements for key entry and control surfaces.

## Non-Goals
- Rebuilding report generation pipelines.
- Large-scale rewrites of generated historical report files.
- Migrating legacy UI2 libraries/frameworks.

## Requirements
- Preserve existing offline path integrity and bundle self-containment.
- Preserve Bootstrap 3/Jasny/Intro.js compatibility assumptions in UI2 pages.
- Keep changes minimal, targeted, and review-friendly.
- Provide user-impact-first release communication notes for shipped updates.

## Acceptance Criteria
- Users can find and open desired reports quickly from top-level navigation pages.
- Key filter/search flows remain functional across representative bundles.
- Mobile layouts for key pages remain usable without blocking core tasks.
- No regressions in local/offline loading for edited surfaces.

## Risks and Mitigations
- Risk: Breaking legacy behavior in generated pages.
  - Mitigation: Constrain edits to non-generated wrappers/entry points where possible.
- Risk: Offline breakage due to path changes.
  - Mitigation: Validate asset/path assumptions after each phase.
- Risk: Inconsistent behavior across bundles.
  - Mitigation: Validate representative pages from each bundle era.
