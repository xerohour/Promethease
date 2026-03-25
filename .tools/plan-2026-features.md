# 2026 Feature Plan: Promethease + Genetic Genie Parity

## Purpose
Build a 2026 report experience that preserves existing Promethease UI2 behavior while adding Genetic Genie style analysis views for methylation and detox panels.

## Assumptions
- Static HTML only (no build step, no backend).
- UI2 reports remain the primary interactive table for SNP findings.
- New Genetic Genie views are derived from existing findings JSON plus a curated panel mapping file.
- All new assets live inside `2026-promethease-*/` bundle folders.

## Goals
- Preserve Promethease UI2 behavior and styling (filters, sorting, table view, SNP detail links).
- Add Genetic Genie style panels (Detox, Methylation) with clear visual status and summary counts.
- Keep everything fully offline-capable and published via the existing GitHub Pages rsync rules.

## Non-Goals
- No medical interpretation beyond the existing report summaries.
- No new external dependencies beyond what is already vendored in `ui2libs/`.
- No changes to raw genome data or Promethease report generation.

## Deliverables
- New Genetic Genie panel page(s) per 2026 bundle.
- Shared mapping JSON for panel definitions and SNP annotations.
- Links between UI2 report and Genetic Genie views.
- Updated `all-reports.html` entry points for 2026 bundles.

## Feature Plan

### Phase 1: Promethease Parity Baseline
- Audit current 2026 UI2 report features and document gaps.
- Ensure the following are stable and themed:
  - Text search
  - Repute filter (Good/Bad/All)
  - Magnitude threshold
  - Sorting and pagination
  - SNP external links
- Add a small “Report Tools” nav link that will later point to Genetic Genie panels.

### Phase 2: Genetic Genie Parity (Core)
- Detox Panel view
  - Table of SNPs grouped by gene.
  - Status coding for homozygous/heterozygous/normal.
  - Summary counts per status.
- Methylation Panel view
  - Same structure as Detox with methylation-focused SNPs.
  - Grouped by pathway or gene family.
- Summary card
  - Counts by status
  - Top genes with most variants

### Phase 3: Integration and UX
- Add navigation between UI2 report and Genetic Genie panels.
- Ensure dark-mode theme is consistent with `openai-brand.css`.
- Mobile layout: stacked panels, collapsible groups, sticky summary.

### Phase 4: Validation
- Local HTML link validation.
- Manual smoke test of fetch paths from `promethease_data/`.

## Data and Mapping Plan
- Create a `panel_definitions.json` inside each 2026 bundle:
  - Panel name: `detox` or `methylation`
  - SNP list: `rsid`, gene, expected allele orientation if needed
  - Display labels and grouping keys
- Build a small transform script (optional) or inline JS that:
  - Reads existing findings JSON
  - Joins by `rsid`
  - Computes genotype state: `homozygous`, `heterozygous`, `normal` (or `unknown`)

## Open Questions
- Do we want panel definitions shared between John/Trina bundles or duplicated per bundle?
- Is any allele orientation correction needed (plus/minus strand) or do we accept Promethease genotype as-is?
- Preferred location of new pages (one per bundle vs shared static page with params)?

## Milestones
1. Parity audit + navigation link
2. Detox panel page + data mapping
3. Methylation panel page + data mapping
4. Theming + mobile polish
5. QA + link validation

## Next Actions
- Identify a canonical Genetic Genie SNP list for detox and methylation panels.
- Decide on shared vs per-bundle panel mapping file.
- Implement Phase 1 in the 2026 bundles.
