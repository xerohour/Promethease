#!/usr/bin/env python3
"""
Enrich genome reports with SNPedia data from SQLite database.

This script reads the SNPedia2025.db database and enriches the existing
genome reports with SNPedia annotations (magnitude, repute, summary).

Usage: python enrich_with_snpedia.py <genome_report_json> <output_json>

Example:
  python enrich_with_snpedia.py 2025-promethease-john/promethease_data/John_Stinson_2025_findings.json 2025-promethease-john/promethease_data/John_Stinson_2025_enriched.json
"""

import json
import sqlite3
import re
import sys
import os
from datetime import datetime, timezone

SNPEDIA_DB = "snpedia_data/SNPedia2025/SNPedia2025.db"

def parse_snpedia_content(content):
    """
    Parse SNPedia wiki content to extract magnitude, repute, and summary.
    
    SNPedia uses wiki templates with format: {{Rsnum |param=value}}
    """
    result = {
        "magnitude": "0",
        "repute": "neutral",
        "summary": "",
        "genes": []
    }
    
    if not content:
        return result
    
    # Parse Rsnum template - extract parameters from {{Rsnum |...}}
    rsnum_match = re.search(r'\{\{Rsnum\s*\|(.+?)\}\}', content, re.DOTALL | re.IGNORECASE)
    if rsnum_match:
        template_content = rsnum_match.group(1)
        
        # Extract magnitude from template
        mag_match = re.search(r'\|magnitude=(\d+)', template_content, re.IGNORECASE)
        if mag_match:
            result['magnitude'] = mag_match.group(1)
        
        # Extract repute from template
        rep_match = re.search(r'\|repute=(\w+)', template_content, re.IGNORECASE)
        if rep_match:
            rep_val = rep_match.group(1).lower()
            if rep_val in ['good', 'bad', 'neutral', 'mixed']:
                result['repute'] = rep_val
        
        # Extract genes
        gene_match = re.search(r'\|gene=([^|\n]+)', template_content, re.IGNORECASE)
        if gene_match:
            result['genes'] = [gene_match.group(1).strip()]
    
    # Also check for standalone magnitude patterns
    if result['magnitude'] == '0':
        magnitude_match = re.search(r'M=(\d+)', content, re.IGNORECASE)
        if magnitude_match:
            result['magnitude'] = magnitude_match.group(1)
    
    # Extract summary - first non-template line
    lines = content.split('\n')
    for line in lines:
        line = line.strip()
        # Skip templates, headers, empty lines
        if line and not line.startswith('{{') and not line.startswith('|') and not line.startswith('='):
            # Clean up wiki markup
            line = re.sub(r'\[\[|\]\]', '', line)
            line = re.sub(r'\{\{.*?\}\}', '', line)
            if len(line) > 10:
                result['summary'] = line[:200]
                break
    
    return result

def load_snpedia_database(db_path):
    """Load SNPedia database and return a dictionary of rsid -> data."""
    print(f"Loading SNPedia database from {db_path}...")
    
    if not os.path.exists(db_path):
        print(f"Error: Database not found: {db_path}")
        return {}
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Get all SNPs
    cursor.execute("SELECT rsid, content FROM snps")
    rows = cursor.fetchall()
    
    snpedia_data = {}
    for rsid, content in rows:
        # Store with lowercase key for case-insensitive lookup
        snpedia_data[rsid.lower()] = parse_snpedia_content(content)
        # Also store with original key
        snpedia_data[rsid] = parse_snpedia_content(content)
    
    conn.close()
    
    print(f"Loaded {len(snpedia_data)} SNPedia entries")
    return snpedia_data

def enrich_report(input_file, output_file, snpedia_data):
    """Enrich a genome report with SNPedia data."""
    
    print(f"\nEnriching report: {input_file}")
    
    # Load existing report
    with open(input_file, 'r', encoding='utf-8') as f:
        report = json.load(f)
    
    findings = report.get('findings', [])
    total = len(findings)
    
    print(f"Processing {total:,} SNPs...")
    
    enriched_count = 0
    
    for i, finding in enumerate(findings):
        rsid = finding.get('rsid', '')
        rsid_lower = rsid.lower()
        
        # Check both original and lowercase versions
        snp_data = snpedia_data.get(rsid) or snpedia_data.get(rsid_lower)
        
        if snp_data:
            
            # Only update if SNPedia has meaningful data
            if snp_data['magnitude'] != '0' or snp_data['repute'] != 'neutral':
                finding['magnitude'] = snp_data['magnitude']
                finding['repute'] = snp_data['repute']
                
                if snp_data['summary']:
                    finding['summary'] = snp_data['summary']
                
                if snp_data['genes']:
                    finding['genes'] = snp_data['genes']
                
                finding['is_snpedia_hit'] = True
                enriched_count += 1
        
        if (i + 1) % 100000 == 0:
            print(f"  Processed {i+1:,} / {total:,} SNPs...")
    
    # Update report metadata
    report['snpedia_online_hits'] = enriched_count
    report['enriched_at_utc'] = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    report['snpedia_database'] = "SNPedia2025.db (July 2025)"
    
    # Count by repute
    repute_counts = {'good': 0, 'bad': 0, 'neutral': 0, 'mixed': 0}
    magnitude_counts = {}
    
    for f in findings:
        rep = f.get('repute', 'neutral')
        if rep in repute_counts:
            repute_counts[rep] += 1
        
        mag = f.get('magnitude', '0')
        magnitude_counts[mag] = magnitude_counts.get(mag, 0) + 1
    
    report['enrichment_summary'] = {
        'total_snps': total,
        'snpedia_hits': enriched_count,
        'repute_distribution': repute_counts,
        'magnitude_distribution': magnitude_counts
    }
    
    # Save enriched report
    print(f"Writing enriched report to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, separators=(',', ':'))
    
    print(f"\nEnrichment complete!")
    print(f"  - Total SNPs: {total:,}")
    print(f"  - SNPedia matches: {enriched_count:,}")
    print(f"  - Good repute: {repute_counts['good']:,}")
    print(f"  - Bad repute: {repute_counts['bad']:,}")
    print(f"  - File size: {os.path.getsize(output_file) / (1024*1024):.2f} MB")
    
    return report

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python enrich_with_snpedia.py <input_json> <output_json>")
        print("Example: python enrich_with_snpedia.py 2025-john.json 2025-john-enriched.json")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    if not os.path.exists(input_file):
        print(f"Error: Input file not found: {input_file}")
        sys.exit(1)
    
    # Load SNPedia data
    snpedia_data = load_snpedia_database(SNPEDIA_DB)
    
    if not snpedia_data:
        print("Error: Could not load SNPedia data")
        sys.exit(1)
    
    # Enrich the report
    enrich_report(input_file, output_file, snpedia_data)