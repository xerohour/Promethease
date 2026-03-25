#!/usr/bin/env python3
"""
Generate complete genome reports from raw 23andMe genome files.

This script processes all SNPs from genome files (not just SNPedia hits) to create
comprehensive JSON reports that include the full genetic inventory.

Usage: python generate_full_genome_report.py <genome_file> <output_json> <person_name> <year>

Example: 
  python generate_full_genome_report.py genome_John_Stinson_Full_20150207073317.txt 2025-john.json "John Stinson" 2025
"""

import json
import sys
import os
from datetime import datetime, timezone

def parse_genome_file(input_file):
    """Parse 23andMe format genome file and return all SNPs."""
    snps = []
    
    print(f"Reading {input_file}...")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            
            # Skip header lines (lines starting with #)
            if line.startswith('#'):
                continue
            
            # Skip empty lines
            if not line:
                continue
            
            # Parse tab-separated line: rsid, chromosome, position, genotype
            parts = line.split('\t')
            
            if len(parts) < 4:
                continue
            
            rsid = parts[0].strip()
            chromosome = parts[1].strip()
            position = parts[2].strip()
            genotype = parts[3].strip()
            
            # Create SNP entry
            snp = {
                "rsid": rsid,
                "chromosome": chromosome,
                "position": position,
                "genotype": genotype,
                "genes": [],
                "repute": "neutral",
                "magnitude": "0",
                "summary": f"Position {chromosome}:{position}",
                "is_snpedia_hit": False
            }
            
            snps.append(snp)
            
            if line_num % 100000 == 0:
                print(f"  Processed {line_num:,} SNPs...")
    
    return snps

def generate_report(genome_file, output_file, person_name, year, compact=True):
    """Generate a complete genome report JSON file."""
    
    print(f"\nGenerating report for {person_name} ({year})")
    print(f"Source: {genome_file}")
    print(f"Output: {output_file}")
    
    # Parse the genome file
    snps = parse_genome_file(genome_file)
    total_snps = len(snps)
    
    print(f"Total SNPs parsed: {total_snps:,}")
    
    # Group SNPs by chromosome for summary
    chromosomes = {}
    for snp in snps:
        chr = snp['chromosome']
        if chr not in chromosomes:
            chromosomes[chr] = 0
        chromosomes[chr] += 1
    
    # Create report structure (without the redundant is_snpedia_hit field)
    report = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
        "person": person_name,
        "genome_file": genome_file,
        "report_year": year,
        "snpedia_online_hits": 0,
        "findings_count": total_snps,
        "total_snps": total_snps,
        "data_source": "raw_genome",  # Indicates this is raw genome data without SNPedia enrichment
        "chromosome_summary": dict(sorted(chromosomes.items(), key=lambda x: (not x[0].isdigit(), x[0]))),
        "findings": snps
    }
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file) if os.path.dirname(output_file) else '.', exist_ok=True)
    
    # Write the report - use compact JSON for large files
    print(f"Writing report to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        if compact:
            json.dump(report, f, separators=(',', ':'))  # Compact JSON
        else:
            json.dump(report, f, indent=2)
    
    print(f"Report generated successfully!")
    print(f"  - Total SNPs: {total_snps:,}")
    print(f"  - File size: {os.path.getsize(output_file) / (1024*1024):.2f} MB")
    
    return report

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python generate_full_genome_report.py <genome_file> <output_json> <person_name> <year>")
        print("Example: python generate_full_genome_report.py genome_John_Stinson_Full_20150207073317.txt 2025-john.json \"John Stinson\" 2025")
        sys.exit(1)
    
    genome_file = sys.argv[1]
    output_file = sys.argv[2]
    person_name = sys.argv[3]
    year = sys.argv[4]
    
    if not os.path.exists(genome_file):
        print(f"Error: Genome file not found: {genome_file}")
        sys.exit(1)
    
    generate_report(genome_file, output_file, person_name, year)