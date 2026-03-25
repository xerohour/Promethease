# Initial Concept

Static HTML/CSS/JS project for hosting and opening Promethease report bundles online and offline.

# Product Guide

## Product Vision
Create a polished, trustworthy Promethease report viewer repository that lets people open, search, filter, and compare genome reports with minimal friction, whether they are online or fully offline.  
The product should feel stable over time: existing report bundles must continue to work, and maintainers must be able to add/update bundles without introducing regressions in legacy UI2 behavior.

## Problem Statement
Promethease report artifacts are large, heterogeneous, and often generated in formats that are not ideal for modern navigation. Users need a way to reliably access findings without breaking report structure, while maintainers need predictable release and deployment workflows that avoid accidental breakage.

## Product Objectives
1. Make report access and navigation fast and intuitive for end users.
2. Preserve broad compatibility with legacy and UI2 bundle formats.
3. Keep every distributed bundle usable in offline/local environments.
4. Reduce maintenance risk through explicit constraints and lightweight validation practices.
5. Provide clear release communication so changes are understandable to non-technical stakeholders.

## Primary User Groups

### 1) Individuals and Families Reviewing Their Reports
These users want quick access to specific reports and findings with minimal setup.

Needs:
- Clear entry points (`index.html`, `all-reports.html`, bundle landing pages).
- Reliable search/filter interactions for finding relevant SNP entries.
- Confidence that links and report pages load consistently.

### 2) Repository Maintainers
These users curate bundles, update styling/navigation, and ship pages safely.

Needs:
- Guardrails against broad rewrites of generated report files.
- Repeatable deployment behavior with visible CI/check outcomes.
- Documentation patterns for communicating what changed and why.

### 3) Power Users Comparing Report Versions
These users evaluate differences across years/subjects and often cross-reference pages.

Needs:
- Predictable naming/version organization.
- Stable report linking across bundles.
- Consistent filtering/search behavior regardless of report vintage.

## Core Outcomes (What "Good" Looks Like)

### Outcome A0: Complete SNP Inventory Access
- Users can access complete SNP inventory (all ~600K SNPs)
- Full genome data exports available even for SNPs without SNPedia interpretations
- JSON-based reports with complete genotype data

### Outcome A: Reliable Offline Viewing
- Report bundles remain self-contained.
- Critical local paths (e.g., `ui2libs/`, `promethease_data/`) are preserved.
- Pages that rely on local fetch patterns still work when served locally.

### Outcome B: Fast, Usable Navigation and Filtering
- Users can quickly locate desired report entry points.
- UI2 pages provide dependable search/filter workflows.
- Common user actions (open bundle, filter by criteria, inspect entries) are friction-light.

### Outcome C: Safe, Low-Risk Maintenance
- Changes are scoped and patch-oriented.
- Compatibility constraints are respected (Bootstrap 3/Jasny/Intro.js in UI2 paths).
- Release communications track meaningful user-visible differences.

## In-Scope Capabilities

### Navigation and Entry
- Repository-level launch points (`index.html`, `all-reports.html`).
- Bundle-specific entry pages (`promethease.html`).
- Organized versioned bundle directories.

### UI2 Experience
- Search/filter controls that remain operational in target report pages.
- Compatibility-safe updates that do not assume modern framework rewrites.
- Visual consistency through shared CSS where appropriate.

### Structure and Compatibility
- Preservation of generated report artifacts.
- Consistent file placement expectations for assets and data directories.
- Backward-compatible evolution of top-level navigation and styling.

## Out of Scope (for this phase)
- Rebuilding Promethease report generation itself.
- Re-architecting UI2 pages into a new frontend framework.
- Broad normalization/refactoring of generated historical report files.
- Replacing bundled vendor libraries with modern equivalents unless required for defect fixes.

## Non-Functional Requirements

### Compatibility & Stability
- Avoid broad rewrites of generated files.
- Preserve historical report behavior across 2018/2024/2026 bundles.
- Treat legacy UI conventions as compatibility contracts unless explicitly changed.

### Portability & Offline Integrity
- Keep bundles self-contained and movable.
- Do not remove/move local dependencies that offline pages require.
- Maintain local-serving behavior for pages that use resource fetching.

### Maintainability
- Prefer minimal, targeted edits.
- Keep filenames and release docs date-scoped and traceable.
- Ensure modifications are easy to audit in PRs.

### Communication Quality
- Keep changelog, release notes, and customer updates aligned with shipped behavior.
- Emphasize user-visible impact and risk notes in release communications.

## Primary Success Metric
**End-user report usability** is the primary metric.

Operationally, this means:
- Users can identify and open the correct report path quickly.
- Users can successfully execute key find/filter flows in UI2 pages.
- Navigation confusion and broken-path incidents are minimized.

## Secondary Health Indicators
- Offline bundle integrity remains intact after updates.
- CI/deploy checks remain stable for release changes.
- Maintenance work stays focused, with limited unintended file churn.

## Guiding Principles
1. **Do no harm to historical bundles.**
2. **Prefer compatibility over novelty in report viewers.**
3. **Optimize for user clarity at entry and filter points.**
4. **Keep updates incremental, reviewable, and reversible.**
5. **Document decisions in release artifacts for long-term maintainability.**
