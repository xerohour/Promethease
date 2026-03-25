# Phase 4 Residual Risks and Follow-up

## Residual Risks
- Older generated 2018/2024 report internals remain largely untouched, so mobile ergonomics there may still be uneven.
- Validation focused on changed surfaces and representative 2026 UI2 pages rather than every generated page.
- The untracked `nul` file remains in the working tree and was intentionally left untouched because it is unrelated to this track.

## Follow-up Tasks
- Extend safe mobile hardening patterns to older non-generated wrappers where useful.
- Add browser-based screenshot checks for top-level navigation pages.
- Consider a small smoke-test checklist for 2026 JSON-backed UI2 pages.
