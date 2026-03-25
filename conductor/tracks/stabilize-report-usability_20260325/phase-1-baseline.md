# Phase 1 Baseline and UX Gap Audit

Date: 2026-03-25
Track: stabilize-report-usability_20260325

## Baseline Usability Checks (Current)
- Verify main entry navigation from `index.html` to primary reports.
- Verify discoverability of legacy/yeared bundles in `all-reports.html`.
- Verify representative wrapper redirects open expected UI2 pages.
- Verify basic mobile readability and tap-target behavior on top-level pages.

## Representative Pages
- `index.html`
- `all-reports.html`
- `2018-promethease/promethease.html`
- `2024-promethease/promethease.html`
- `2026-promethease-john/promethease.html`
- `2026-promethease-trina/promethease.html`
- `2026-promethease-john/Promethease_2026_03_03_genome_John_Stinson_Full_20260303020155_ui2.html`
- `2026-promethease-trina/Promethease_2026_03_03_genome_Trina_Toohey_Full_20260303020155_ui2.html`

## Desktop + Mobile Pain Points (Observed)
- Landing page lacks explicit quick links to year-based wrappers, forcing extra navigation.
- `all-reports.html` is long and dense with limited grouping aids for quick scanning.
- Top action button on `all-reports.html` is small on mobile.
- Redirect wrapper pages have minimal context and no clear fallback actions.

## Measurable Before/After Criteria
- Navigation efficiency: reduce clicks to reach yeared bundle entry points from top-level pages.
- Discoverability: ensure grouped sections and quick-jump links exist for key categories.
- Mobile usability: primary controls are easy to tap/read at narrow widths.
- Compatibility: no path changes that break offline loading for existing bundles.

## Residual Risks
- Large generated pages are intentionally untouched to avoid legacy regressions.
- Changes should focus on wrappers/top-level pages and shared CSS only.
