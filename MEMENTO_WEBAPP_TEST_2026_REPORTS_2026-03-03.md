# Memento: Webapp Test - 2026 Reports Comparison

Date: 2026-03-03
Scope: Browser-based comparison of report variants listed in All Reports

## Target URL and Access Result

- Requested preview URL: `https://promethese-pr8lww5oj-xerohours-projects.vercel.app/`
- Result: protected by Vercel auth (`Login – Vercel`), not directly testable without authenticated session.
- Fallback tested: `https://promethese.vercel.app/`

## Test Method

- Opened home page.
- Navigated to `All Report Versions` (`all-reports.html`).
- Enumerated listed `Promethease_YYYY_MM_DD_*.html` pages.
- Compared available 2026 report page types against legacy (2015/2024) variants.
- Audited a 2026 UI2 page for filter/search feature presence.

## Comparison Results

- `2026-John`: only `ui2` present.
- `2026-Trina`: only `ui2` present.

Missing in newer 2026 reports compared to legacy sets:

- `base`
- `Topic`
- `complicated`
- `is-a-medical-condition`
- `is-a-medicine`
- `newfamily`
- `offspring`

## 2026 UI2 Feature Audit (Present)

- Right-side controls panel
- Text search (`#textfilter`)
- Repute filter (`#repute`)
- Minimum magnitude filter (`#minMag`)
- Help and Reset buttons
- Intro.js stylesheet link
- Results table body (`#rows`)

## Evidence Artifacts

- `render-home-public.png`
- `render-all-reports-public.png`
- `render-2026-ui2-public.png`
- `render-home-recon.png` (auth gate reconnaissance on preview URL)

