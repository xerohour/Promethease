# Contributing

Thanks for contributing to this static Promethease report viewer repository.

## Scope and Approach

- Prefer minimal, targeted edits over broad rewrites.
- Treat generated report artifacts as sensitive; avoid mass-formatting report HTML.
- Keep changes focused by concern (UI changes, workflow changes, release docs).

## Development Workflow

1. Create a branch with a concise, descriptive name.
2. Make focused edits.
3. Serve locally with `python -m http.server 8000`.
4. Verify changed pages in a browser.
5. Run `git status --short` and stage only intended files.

## Validation Expectations

- Manually render changed report pages (`promethease.html`, `*_ui2.html`).
- For 2026 UI2 pages, test filter/search interactions after JS/CSS edits.
- Confirm linked assets still resolve in offline mode (especially `ui2libs/`).

## Documentation and Release Hygiene

- Update `CHANGELOG.md` for user-facing behavior changes.
- Keep `CHANGELOG_KEEPACHANGELOG.md` aligned with released versions.
- Add or update `RELEASE_NOTES_YYYY-MM-DD.md` and `CUSTOMER_UPDATE_YYYY-MM-DD.md` for release communication.

## Pull Requests

Include:

- A short summary of user-visible impact.
- Affected paths.
- Screenshots for UI changes.
- Linked issue/ticket when available.

## Security

- Never commit secrets or credentials.
- Keep bundles self-contained to preserve offline functionality.
- If CI note checks apply, push git notes when required: `git push origin refs/notes/commits`.
