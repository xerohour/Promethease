# JavaScript Style Guide

## Scope and Safety
- Prefer minimal, targeted patches.
- Do not break legacy UI2 library assumptions.
- Keep existing public/global behavior stable.

## Formatting
- Use 2-space indentation.
- Prefer `const`/`let` over `var` in new code when safe.
- Keep functions small and focused.

## Reliability
- Add guard clauses for missing DOM nodes/data.
- Avoid introducing build-step dependencies.
- Preserve offline behavior and local path assumptions.
