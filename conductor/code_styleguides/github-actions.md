# GitHub Actions Style Guide

## Workflow Safety
- Use pinned major versions for official actions.
- Keep permissions least-privilege.
- Prefer explicit include/exclude patterns for publish artifacts.

## Readability
- Use clear step names.
- Keep shell scripts strict (`set -euo pipefail` for bash).
- Document non-obvious deployment constraints inline.
