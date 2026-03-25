# Product Guidelines

## Purpose and Scope
These guidelines define how Promethease report viewer experiences should be written, structured, and validated so users can work effectively with complex genetic report content across desktop and mobile contexts.  
They apply to:
- Top-level navigation pages (`index.html`, `all-reports.html`)
- Bundle entry pages (`promethease.html`)
- UI2 report pages and their filtering/search interactions
- User-facing release communication artifacts

The goal is not visual novelty; it is confidence, clarity, and compatibility.

## Audience-Centered Communication Model

### Primary Audiences
- End users reviewing personal/family reports
- Maintainers shipping updates safely
- Power users performing cross-version comparisons

### Writing Priority
When content targets mixed audiences, optimize for end-user clarity first, then layer in technical depth for advanced readers.

## Voice and Tone

### Core Voice
Use a **friendly and supportive** tone while maintaining **expert-level precision**.

### Tone Characteristics
- Calm, direct, and non-alarmist
- Respectful and confidence-building
- Transparent about limitations and uncertainty
- Precise when describing behavior, constraints, and risks

### Tone Do/Don’t
Do:
- “Use the report filters to narrow to high-magnitude findings.”
- “This update keeps legacy UI2 behavior unchanged.”

Don’t:
- “Obviously, just use the controls correctly.”
- “Everything is fixed now.” (without evidence/scope)

## Communication Hierarchy

### Default Structure (Required)
1. **User impact first**
   - What changed
   - Why it matters
   - Who is affected
2. **Technical detail second**
   - File/system behavior details
   - Constraints/compatibility notes
   - Validation performed

### Optional Maintainer-First Addendum
For maintainer-heavy updates, include a separate technical-first subsection while preserving a user-impact summary at the top.

## UX and Layout Principles

### Information-Dense but Scannable
Report pages can be dense, but must remain navigable:
- Use strong heading hierarchy and section grouping.
- Keep primary controls visually obvious and predictably placed.
- Reduce cognitive load with consistent labeling and grouping.

### Consistency Across Bundles
- Preserve equivalent interaction patterns across 2018/2024/2026 bundles where technically feasible.
- Avoid unnecessary changes to familiar controls, order, or terminology.
- Treat legacy behavior as part of the user contract unless explicitly changed.

### Progressive Disclosure
- Show essential controls by default.
- Place advanced/rare options where discoverable but non-disruptive.
- Avoid overwhelming first-time users with implementation-heavy language.

## Responsive Design (Required)

### Baseline Requirement
All key navigation and report interaction surfaces must support mobile viewing.

### Practical Requirements
- Preserve core tasks at narrow widths: open report, search, filter, inspect entries.
- Ensure controls remain operable with touch (tap targets, spacing, focus).
- Avoid horizontal overflow traps for primary interaction paths.
- Maintain readable text hierarchy and contrast on small screens.
- Prioritize resilient layout behavior over pixel-perfect parity with desktop.

### Responsive QA Expectations
For modified pages, verify at minimum:
- Desktop width
- Tablet-ish width
- Mobile width (narrow portrait)

## Content and Labeling Standards

### Plain-Language First
- Write labels/actions in plain language, then add technical context where needed.
- Prefer explicit action labels over shorthand.

### Technical Context
When technical terms are necessary:
- Explain once near first use.
- Keep definitions concise and context-bound.
- Avoid repeated glossary-like interruptions.

### Naming Stability
- Keep version/report naming conventions stable and predictable.
- Avoid renaming user-facing report labels unless there is a strong benefit and clear communication.

## Warning-First Safety Messaging

### When Required
Use warning-first messaging before:
- Destructive actions
- Changes that can break offline behavior
- Edits that can alter legacy UI2 functionality
- Workflow changes affecting deployment or release behavior

### Warning Content Minimum
- What could break
- Who/what is affected
- How to mitigate or recover
- Validation steps to confirm safety

## Accessibility Baseline

### Standard
Target **WCAG AA** as the baseline.

### Implementation Expectations
- Adequate color contrast for text and controls
- Clear focus states and keyboard reachability where feasible
- Semantic heading/order structure for scanability
- Non-color-only communication of critical states
- Legible typography and spacing under responsive layouts

### Accessibility as Maintenance
Accessibility is not a one-time pass; each UI change should preserve or improve baseline usability.

## Compatibility and Legacy Protection

### Compatibility-First Principle
- Preserve existing generated report behavior.
- Avoid broad rewrites of generated files unless absolutely necessary.
- Favor minimal, targeted, reversible edits.

### Dependency/Path Integrity
- Keep local asset paths and bundle-relative references intact.
- Avoid moving/removing files that offline workflows depend on.

### UI2 Constraints
Respect compatibility assumptions around Bootstrap 3/Jasny/Intro.js within UI2 surfaces unless a deliberate migration is planned and documented.

## Release Communication Guidelines

### Required Sections
- User-visible changes
- Compatibility/risk notes
- Validation summary (what was checked)
- Follow-up or known limitations (if any)

### Style Expectations
- Keep statements verifiable.
- Separate “done now” from “planned next.”
- Avoid overpromising language.

## Decision-Making Heuristics
When tradeoffs appear, prioritize in this order:
1. Prevent regressions in user-critical flows
2. Preserve offline reliability and path integrity
3. Maintain cross-bundle behavioral consistency
4. Improve clarity/usability
5. Optimize maintainability and polish

## Quality Gate Checklist
Before finalizing changes, confirm:
- Voice is supportive, clear, and technically accurate.
- User impact is summarized before technical detail.
- Mobile/responsive behavior supports key tasks.
- Labels are plain-language and consistent.
- Risky operations include warning-first messaging.
- Accessibility intent meets WCAG AA baseline.
- Compatibility and offline path integrity are preserved.
