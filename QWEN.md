# Promethease Offline Report Repository

## Project Overview

This is a **static HTML repository** hosting offline Promethease genome analysis reports. There is no build step, package.json, or bundler—all reports are pre-generated HTML files checked into git. The site deploys to GitHub Pages and can also be viewed locally by opening HTML files directly in a browser.

**Purpose:** Provide offline-accessible views of Promethease SNP (Single Nucleotide Polymorphism) analysis reports for two individuals (John Stinson and Trina Toohey) across multiple years (2015, 2018, 2024, 2026).

**Key Technologies:**
- **Frontend:** Vanilla HTML/CSS/JavaScript, Bootstrap 5 (CDN) for wrapper pages, Bootstrap 3 (vendored) for UI2 reports
- **Theming:** Custom `openai-brand.css` dark-mode overrides + DarkReader (CDN)
- **Visualization:** Three.js (ES module) for DNA particle animation on landing page
- **Data Tables:** jQuery + DataTables + Chosen (vendored in `ui2libs/`)
- **Bioinformatics Utility:** `genome_ops.py` (TensorFlow-IO) for FASTQ file operations (standalone, not used by web reports)

---

## Repository Structure

```
Promethease/
├── index.html                          # Landing page with Three.js DNA animation
├── all-reports.html                    # Full index of all report variants
├── openai-brand.css                    # Global dark-mode theme overrides
├── matrix-soundtrack.mp3               # Background audio for landing page
├── three.module.js                     # Three.js ES module for animation
├── genome_ops.py                       # TensorFlow-IO FASTQ utility (standalone)
│
├── 2018-promethease/                   # 2018 report bundle (John)
│   ├── promethease.html                # Entry point (redirects to UI2)
│   └── ui2libs/                        # Vendored JS/CSS dependencies
│
├── 2024-promethease/                   # 2024 report bundle (Trina)
│   ├── promethease.html
│   ├── promethease_data/               # Nested data directories
│   └── ui2libs/
│
├── 2026-promethease-john/              # 2026 report bundle (John, UI2 format)
│   ├── promethease.html
│   ├── *_ui2.html                      # Interactive UI2 report page
│   ├── promethease_data/               # JSON findings data
│   └── ui2libs/
│
├── 2026-promethease-trina/             # 2026 report bundle (Trina, UI2 format)
│   └── ... (same structure as John)
│
├── Promethease_2015_*.html             # Flat-root 2015 reports (both subjects)
├── Promethease_2024_*.html             # Flat-root 2024 reports (Trina)
├── file-*.html                         # F1 comparison reports
├── file-*-extra*.txt                   # SNP comparison data files
├── genome_*.txt                        # Raw genome data files
└── *.zip                               # Offline download bundles
```

---

## Report Bundle Architecture

### UI2 Report Pages (`*_ui2.html`)

Self-contained single-page applications with inline JavaScript:

1. **On Load:** `fetch()` companion `_findings_2026.json` from `promethease_data/`
2. **Data Model:** Each finding contains:
   - `rsid`: SNP identifier (e.g., "rs123456")
   - `genotype`: Observed genotype (e.g., "A/G")
   - `genes[]`: Associated genes
   - `repute`: "Good", "Bad", or null
   - `magnitude`: Float (importance score)
   - `summary`: Description text
   - `chromosome`, `position`: Genomic location
3. **Rendering:** Filterable/sortable `<table>` using DataTables
4. **Filter Panel:** Fixed right-side `<aside>` with Bootstrap offcanvas (`navmenu-fixed-right offcanvas`)
   - Text search input
   - Repute filter (Good/Bad/All)
   - Minimum magnitude slider
   - Guided intro.js help overlay

### Legacy Bundles (2018, 2024)

Older format viewers with data embedded in nested `promethease_data/` subdirectories. Use Bootstrap 3 UI components.

### Flat-Root Reports

Original Promethease export artifacts (2015, 2024) published as-is. The 2015 UI2 variants (`*_ui2.html`) apply `openai-brand.css` theming.

---

## Building and Running

### Local Development

No build required. Open any HTML file directly in a browser:

```bash
# Option 1: Direct file open
open index.html                    # macOS
start index.html                   # Windows
xdg-open index.html                # Linux

# Option 2: Local web server (recommended for fetch() calls)
python -m http.server 8000
# Then navigate to http://localhost:8000
```

**Note:** UI2 reports use `fetch()` to load JSON data. Some browsers block `file://` XHR requests—use a local server if the report doesn't load.

### Validation (CI Checks)

Run locally before committing:

```bash
# 1. HTML link validation
python - <<'PY'
from pathlib import Path
import re
import sys

root = Path(".").resolve()
skip_dirs = {".git", "node_modules", ".npm-cache", ".uv-cache"}
html_files = [p for p in root.rglob("*.html") if not any(part in skip_dirs for part in p.parts)]

pattern = re.compile(r"""(?:href|src)=['"]([^'"]+)['"]""", re.IGNORECASE)
errors = []
checked = 0

for html in html_files:
    text = html.read_text(encoding="utf-8", errors="ignore")
    for ref in pattern.findall(text):
        if ref.startswith(("http://", "https://", "mailto:", "tel:", "data:", "javascript:", "#")) or ref.startswith("//"):
            continue
        local = ref.split("#", 1)[0].split("?", 1)[0].strip()
        if not local or "${" in local or "{{" in local:
            continue
        target = (html.parent / local).resolve()
        checked += 1
        if not target.exists():
            errors.append(f"{html.relative_to(root)} -> missing: {local}")

print(f"Scanned {len(html_files)} HTML files; checked {checked} local refs.")
if errors:
    print("Broken local refs found:")
    for line in errors[:200]:
        print(f"- {line}")
    sys.exit(1)
print("All local HTML refs resolved.")
PY

# 2. Python syntax check
python -m py_compile genome_ops.py
```

### Deployment

**Automatic:** Pushing to `main` triggers `.github/workflows/static.yml`:
1. `rsync` builds `_site/` artifact with only included files
2. Deploys to GitHub Pages

**Manual:** Go to **Actions → Deploy static content to Pages → Run workflow**

**rsync Include Rules** (only these are published):
- `/index.html`, `/all-reports.html`, `/openai-brand.css`, `/matrix-soundtrack.mp3`
- `/Promethease_*` (flat-root reports)
- `/2018-promethease/***`, `/2024-promethease/***`, `/2026-promethease-john/***`, `/2026-promethease-trina/***`

**Excluded:** Raw genome `.txt`/`.zip` files, `agentic_kb/` submodule, local artifacts.

---

## Development Conventions

### Adding a New Report Bundle

1. Create bundle folder (e.g., `2026-promethease-<name>/`)
2. Include required files:
   - `promethease.html` (entry redirect)
   - `*_ui2.html` (main report page)
   - `promethease_data/<name>_findings_2026.json` (SNP data)
   - `ui2libs/` (vendored dependencies for offline mode)
   - `report_metadata.txt` (optional metadata)
3. Add folder to `.github/workflows/static.yml` rsync `--include` list
4. Add link from `all-reports.html` and/or `index.html`
5. Run HTML link validation

### Theming

All pages use `openai-brand.css`—a global dark-mode override with aggressive `!important` rules:
- CSS custom properties: `--oa-charcoal`, `--oa-slate`, `--oa-mist`, `--oa-green`, `--oa-azure`
- Targets both Bootstrap 3 (UI2 reports) and Bootstrap 5 (wrapper pages)
- DarkReader (CDN) loaded as fallback on every page

### File Naming

- **UI2 reports:** `Promethease_YYYY_MM_DD_genome_<Name>_Full_<timestamp>_ui2.html`
- **Legacy redirects:** Same name without `_ui2` suffix
- **Findings JSON:** `<report_name>_findings_2026.json`
- **Comparison reports:** `file-F1-*.html`

### Git Workflow

**Memento Notes Required:** PRs must include a memento note or be labeled `ignore-notes`.

Enforced by:
- `memento-note-gate.yml` — blocks merge if missing
- `memento-note-comments.yml` — posts note as PR comment
- `memento-notes-merge-carry.yml` — carries notes into merge commit

**Submodule Updates:**
```bash
git submodule update --remote agentic_kb
git add agentic_kb
git commit -m "Update: agentic_kb submodule to latest"
```

---

## Key Files Reference

| File | Purpose |
|------|---------|
| `index.html` | Landing page with Three.js DNA animation, links to primary reports |
| `all-reports.html` | Complete index of all report variants across years/subjects |
| `openai-brand.css` | Global dark-mode theme (CSS custom properties + `!important` overrides) |
| `genome_ops.py` | TensorFlow-IO utility for FASTQ file reading and one-hot DNA encoding |
| `2026-promethease-*/promethease.html` | Bundle entry point (redirects to versioned UI2 page) |
| `2026-promethease-*/promethease_data/*_findings_2026.json` | SNP findings data consumed by UI2 pages |
| `.github/workflows/static.yml` | GitHub Pages deployment configuration |
| `.github/workflows/ci.yml` | CI validation (HTML links + Python syntax) |

---

## Important Constraints

1. **Do not add files to repo root** beyond rsync include list—genome `.txt`/`.zip` files are large and already committed
2. **`AGENTS.md` is gitignored**—local-only, not tracked
3. **`promethease_data/` must be sibling** to the `*_ui2.html` that fetches it (relative path in `fetch()` call)
4. **Keep bundle folders intact**—moving/deleting files breaks local links
5. **External CDN dependencies:** Bootstrap 5, DarkReader, Google Fonts, Three.js (landing page only)
6. **Offline mode:** UI2 reports use vendored `ui2libs/` for all JS/CSS dependencies

---

## Related Documentation

- `README.md` — Quick-start guide for opening reports
- `CHANGELOG.md` — User-facing changelog
- `AGENTS.md` — WARP-specific agent instructions (local-only, not tracked)
- `RELEASE_NOTES_*.md` — GitHub-style release notes
- `CUSTOMER_UPDATE_*.md` — Customer-facing update copy
- `MEMENTO_*.md` — PR session/carry artifacts (informational only)
