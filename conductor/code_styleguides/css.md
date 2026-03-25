# CSS Style Guide

## Formatting
- Use 2-space indentation.
- Prefer class-based selectors over deep descendant chains.
- Keep rules grouped by component/section.

## Design Constraints
- Preserve existing visual behavior unless explicitly changing UX.
- Prefer additive overrides over destructive refactors.
- Maintain responsive behavior for desktop and mobile widths.

## Maintainability
- Keep selectors specific enough to avoid regressions.
- Minimize `!important`; use only when compatibility requires it.
