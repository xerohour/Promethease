# Promethease Report Viewer Repository

Static HTML/CSS/JS project for hosting and opening Promethease report bundles online and offline.

**Live Site:** [https://xerohour.github.io/Promethease/](https://xerohour.github.io/Promethease/)

## Quick Start

### View Online
1. Open [index.html](https://xerohour.github.io/Promethease/) or [all-reports.html](https://xerohour.github.io/Promethease/all-reports.html).
2. Choose a report bundle (John or Trina, 2018/2024/2026 variants).

### View Offline
1. Clone/download the repository.
2. Open a target bundle `promethease.html` or `*_ui2.html` file directly.
3. For pages using `fetch()` (notably 2026 bundles), run:

```bash
python -m http.server 8000
# http://localhost:8000/
```

## Included Report Bundles

- `2018-promethease/`
- `2024-promethease/`
- `2026-promethease-john/`
- `2026-promethease-trina/`

## Features

- Static/offline-friendly report hosting
- UI2 report pages with search/filter controls
- Shared styling in `openai-brand.css`
- Landing and navigation pages: `index.html`, `all-reports.html`
- F1 comparison reports at repo root (`file-F1-*.html`)
- Cross-report comparison tool (`compare-reports.html`)
- SNPedia data enrichment for full genome reports

## SNPedia Data Enrichment

This repository includes tools to generate enriched genome reports using SNPedia data:

### Scripts

- **`snpedia_scraper.py`** - Scrape SNPedia directly using their API (based on [SNPedia-Scraper](https://github.com/jaykobdetar/SNPedia-Scraper))
- **`generate_full_genome_report.py`** - Converts raw 23andMe genome files to JSON with all SNPs
- **`enrich_with_snpedia.py`** - Enriches genome reports with SNPedia data (magnitude, genes, summary)
- **`download_snpedia_dump.py`** - Downloads SNPedia data dump (may require manual download due to protection)

### Data Sources

- **Zenodo**: SNPedia 2025 dump (111,727 SNPs) - [https://zenodo.org/records/16053572](https://zenodo.org/records/16053572)
- **GitHub**: SNPedia-Scraper tool - [https://github.com/jaykobdetar/SNPedia-Scraper](https://github.com/jaykobdetar/SNPedia-Scraper)

### Usage

```bash
# Option 1: Use existing pre-downloaded database (fast!)
# The SNPedia2025.db database is already available in this repository
python snpedia_scraper.py --output snpedia_data/SNPedia2025/SNPedia2025.db --count
# Output: Database contains 111,727 SNPs

# Option 2: Scrape SNPedia directly (slow but fresh data)
# WARNING: This takes ~90 days for all SNPs due to 3-second rate limiting
python snpedia_scraper.py --output snpedia_data/my_scraped.db

# Check current count in default database
python snpedia_scraper.py --count

# For testing with a small sample, see "Test Scrape Example" below

# Generate full genome report from raw 23andMe genome file
python generate_full_genome_report.py genome_John_Stinson_Full_20150207073317.txt output.json "John Stinson" 2025

# Enrich genome report with SNPedia data
python enrich_with_snpedia.py input.json output.json
```

**Test Scrape Example:**
To test the scraper with a small sample, you can manually insert a test SNP into the existing database:

```python
import sqlite3
# Add to existing SNPedia database
conn = sqlite3.connect('snpedia_data/SNPedia2025/SNPedia2025.db')
# Use a placeholder RSID for testing (format matches SNPedia templates)
conn.execute('INSERT OR IGNORE INTO snps (rsid, content) VALUES (?, ?)', 
    ('Rs99999999', '{{Rsnum|magnitude=5|gene=TEST|Geno2}}Test SNP for validation'))
conn.commit()
print("Added test SNP - verify with enrich script")
conn.close()

# Then run enrichment to test it works:
python enrich_with_snpedia.py input.json output.json
# Check output for Rs99999999 with magnitude=5
```

**Note:** The scraper uses a 3-second delay between API calls to be respectful to SNPedia. For ~110K SNPs, full scraping takes approximately 90 days. Use the pre-downloaded Zenodo dump for faster results.

### 2025 Enriched Reports

The repository includes 2025 enriched genome reports for John Stinson and Trina Toohey with:
- ~600,000 SNPs from raw genome data
- ~4,871 SNPs enriched with SNPedia magnitude data
- SNPedia 2025 database (July 2025)

## Repository Layout

- `index.html`: Landing page.
- `all-reports.html`: Aggregated report navigation.
- `openai-brand.css`: Shared visual styling.
- `20xx-promethease*/`: Versioned report bundles and assets.
- `.github/workflows/`: Pages deployment and CI workflows.
- `CHANGELOG*.md`, `RELEASE_NOTES_*.md`, `CUSTOMER_UPDATE_*.md`: Release communications.
- `agentic_kb/`: Knowledge-base submodule (managed separately).

## Local Validation Checklist

- Open changed pages in desktop and mobile widths.
- Verify UI2 filter/search behavior on 2026 pages.
- Preserve offline integrity; do not move/remove `ui2libs/` dependencies.

## Development

No build step is required; this is a static site.

```bash
# serve locally
python -m http.server 8000

# inspect local changes
git status --short
```

## Deployment

GitHub Pages deploys from `main` via `.github/workflows/static.yml`.

You can monitor CI checks with:

```bash
gh pr checks <PR_NUMBER> --watch --interval 10
```

## Documentation Map

- [CHANGELOG.md](./CHANGELOG.md)
- [CHANGELOG_KEEPACHANGELOG.md](./CHANGELOG_KEEPACHANGELOG.md)
- [RELEASE_NOTES_2026-03-02.md](./RELEASE_NOTES_2026-03-02.md)
- [RELEASE_NOTES_2026-03-03.md](./RELEASE_NOTES_2026-03-03.md)
- [CUSTOMER_UPDATE_2026-03-02.md](./CUSTOMER_UPDATE_2026-03-02.md)
- [CUSTOMER_UPDATE_2026-03-03.md](./CUSTOMER_UPDATE_2026-03-03.md)

## Contribution Notes

See [CONTRIBUTING.md](./CONTRIBUTING.md) for editing conventions, validation expectations, and PR guidance.