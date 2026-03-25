# Promethease Offline Genome Reports

A static repository hosting offline [Promethease](https://promethease.com/) genome analysis reports with full dark-mode theming and interactive filtering.

**Live Site:** [https://xerohour.github.io/Promethease/](https://xerohour.github.io/Promethease/)

---

## Quick Start

### View Reports Online
1. Visit the [landing page](https://xerohour.github.io/Promethease/) with Three.js DNA animation
2. Select a report: **John Stinson** or **Trina Toohey**
3. Browse all versions via [All Reports](https://xerohour.github.io/Promethease/all-reports.html)

### View Reports Offline
1. Clone or download this repository
2. Open any `*_ui2.html` file directly in your browser
3. For reports using `fetch()` (2026 bundles), use a local server:
   ```bash
   python -m http.server 8000
   # Navigate to http://localhost:8000
   ```

---

## Available Reports

| Year | Subject | Format | Entry Point |
|------|---------|--------|-------------|
| 2015 | John Stinson | UI2 + Legacy | [`Promethease_2015_02_07_genome_John_Stinson_Full_20150207073317_ui2.html`](Promethease_2015_02_07_genome_John_Stinson_Full_20150207073317_ui2.html) |
| 2015 | Trina Toohey | UI2 + Legacy | [`Promethease_2015_02_07_genome_Trina_Toohey_Full_20150207073527_ui2.html`](Promethease_2015_02_07_genome_Trina_Toohey_Full_20150207073527_ui2.html) |
| 2018 | John Stinson | Legacy Bundle | [`2018-promethease/promethease.html`](2018-promethease/promethease.html) |
| 2024 | Trina Toohey | Legacy Bundle | [`2024-promethease/promethease.html`](2024-promethease/promethease.html) |
| 2026 | John Stinson | UI2 + JSON Data | [`2026-promethease-john/promethease.html`](2026-promethease-john/promethease.html) |
| 2026 | Trina Toohey | UI2 + JSON Data | [`2026-promethease-trina/promethease.html`](2026-promethease-trina/promethease.html) |

### Comparison Reports
- **F1 Comparison (John vs Trina 2015):** [`file-F1-1570234575-28738809.html`](file-F1-1570234575-28738809.html)
- **F1 Comparison (Trina vs John 2015):** [`file-F1-28738809-1570234575.html`](file-F1-28738809-1570234575.html)

---

## Features

### UI2 Report Pages (2015, 2026)
- **Interactive SNP Table:** Sortable, filterable findings with DataTables
- **Right-Side Filter Panel:**
  - Text search across SNP summaries
  - Repute filter (Good / Bad / All)
  - Minimum magnitude slider (0.0–5.0)
  - Guided intro.js help overlay
- **Dark Mode:** Custom `openai-brand.css` theme + DarkReader fallback
- **SNPedia Links:** Click any rsID to view on SNPedia

### Landing Page
- **Three.js DNA Animation:** Vaporwave-style particle DNA strands with Matrix soundtrack
- **Quick Links:** Direct access to primary reports

### Offline Support
- All JS/CSS vendored in `ui2libs/` directories
- No external dependencies required for legacy bundles
- Download `.zip` bundles for complete offline viewing

---

## Repository Structure

```
Promethease/
├── index.html                          # Landing page with Three.js animation
├── all-reports.html                    # Complete report index
├── openai-brand.css                    # Global dark-mode theme
├── matrix-soundtrack.mp3               # Landing page audio
├── three.module.js                     # Three.js DNA animation
├── genome_ops.py                       # TensorFlow-IO FASTQ utility
│
├── 2018-promethease/                   # 2018 John bundle (legacy)
│   ├── promethease.html
│   └── ui2libs/
│
├── 2024-promethease/                   # 2024 Trina bundle (legacy)
│   ├── promethease.html
│   ├── promethease_data/
│   └── ui2libs/
│
├── 2026-promethease-john/              # 2026 John bundle (UI2 + JSON)
│   ├── promethease.html
│   ├── *_ui2.html
│   ├── promethease_data/*.json
│   └── ui2libs/
│
├── 2026-promethease-trina/             # 2026 Trina bundle (UI2 + JSON)
│   └── ... (same structure)
│
├── Promethease_2015_*.html             # Flat-root 2015 reports
├── Promethease_2024_*.html             # Flat-root 2024 reports
├── file-F1-*.html                      # Comparison reports
├── genome_*.txt                        # Raw genome data
└── *.zip                               # Offline download bundles
```

---

## Development

### Local Testing
```bash
# Start local server (required for 2026 UI2 reports with fetch())
python -m http.server 8000

# Open in browser
# http://localhost:8000/index.html
```

### Validation
Run CI checks locally before committing:
```bash
# HTML link validation
python -c "
from pathlib import Path
import re
root = Path('.')
html_files = list(root.rglob('*.html'))
pattern = re.compile(r'(?:href|src)=[\"']([^\"']+)[\"']')
for html in html_files:
    for ref in pattern.findall(html.read_text()):
        if not ref.startswith(('http', '#', 'data:', 'javascript:')):
            target = (html.parent / ref.split('#')[0]).resolve()
            if not target.exists():
                print(f'{html} -> missing: {ref}')
"

# Python syntax check
python -m py_compile genome_ops.py
```

### Deployment
Pushing to `main` automatically deploys to GitHub Pages via `.github/workflows/static.yml`.

Manual trigger: **Actions → Deploy static content to Pages → Run workflow**

---

## Adding a New Report Bundle

1. Create bundle folder: `2026-promethease-<name>/`
2. Include required files:
   - `promethease.html` (entry redirect)
   - `*_ui2.html` (main report page)
   - `promethease_data/<name>_findings_2026.json` (SNP data)
   - `ui2libs/` (vendored dependencies)
3. Add folder to `.github/workflows/static.yml` rsync `--include` list
4. Add link from `all-reports.html`
5. Run HTML link validation

---

## Documentation

| File | Description |
|------|-------------|
| [`QWEN.md`](./QWEN.md) | Comprehensive project documentation and agent instructions |
| [`AGENTS.md`](./AGENTS.md) | WARP-specific development notes (local-only, not tracked) |
| [`CHANGELOG.md`](./CHANGELOG.md) | User-facing changelog |
| [`RELEASE_NOTES_*.md`](./RELEASE_NOTES_2026-03-02.md) | GitHub-style release notes |
| [`CUSTOMER_UPDATE_*.md`](./CUSTOMER_UPDATE_2026-03-02.md) | Customer-facing update copy |

---

## Important Notes

- **Do not add files to repo root** beyond the rsync include list—genome `.txt`/`.zip` files are large
- **Keep bundle folders intact**—moving files breaks local `fetch()` paths
- **`promethease_data/` must be sibling** to the `*_ui2.html` that fetches it
- **`AGENTS.md` is gitignored**—local-only, not deployed

---

## License

This repository contains personal genome analysis reports. The code structure and theming (`openai-brand.css`, landing page) are original work. Promethease report formats are generated by [Promethease](https://promethease.com/).

---

**Last Updated:** March 2026
