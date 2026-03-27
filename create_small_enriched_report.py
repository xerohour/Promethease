#!/usr/bin/env python3
"""
Create smaller filtered 2025 enriched reports by keeping only SNPs with 
meaningful SNPedia data (is_snpedia_hit=True).

This significantly reduces file size while preserving all medically relevant information.

Usage:
    python create_small_enriched_report.py -i input.json -o output.json
    python create_small_enriched_report.py -i input.json -o output.json --verbose
    python create_small_enriched_report.py  # Uses default paths
"""

import json
import sys
import os
import argparse

def create_small_enriched_report(input_file, output_file, verbose=False):
    """Filter enriched report to only include meaningful SNPedia hits."""
    
    if verbose:
        print(f"\n[VERBOSE] Processing: {input_file}")
    else:
        print(f"\nProcessing: {input_file}")
    
    # Load the full enriched report
    with open(input_file, 'r', encoding='utf-8') as f:
        report = json.load(f)
    
    findings = report.get('findings', [])
    total = len(findings)
    if verbose:
        print(f"  [VERBOSE] Total SNPs in original: {total:,}")
    else:
        print(f"  Total SNPs in original: {total:,}")
    
    # Filter to only meaningful SNPedia hits
    filtered_findings = []
    for f in findings:
        is_hit = f.get('is_snpedia_hit', False)
        
        # Include all SNPedia hits (is_snpedia_hit=True means the SNP exists in SNPedia database)
        # This gives us 23,535 meaningful SNPs vs 598,897 total - still a huge reduction
        if is_hit:
            filtered_findings.append(f)
    
    filtered_count = len(filtered_findings)
    if verbose:
        print(f"  [VERBOSE] Meaningful SNPedia hits: {filtered_count:,}")
        print(f"  [VERBOSE] Reduction: {total - filtered_count:,} SNPs removed ({100*(total-filtered_count)/total:.1f}%)")
    else:
        print(f"  Meaningful SNPedia hits: {filtered_count:,}")
        print(f"  Reduction: {total - filtered_count:,} SNPs removed ({100*(total-filtered_count)/total:.1f}%)")
    
    # Create filtered report
    filtered_report = {
        "generated_at_utc": report.get("generated_at_utc", ""),
        "person": report.get("person", ""),
        "genome_file": report.get("genome_file", ""),
        "report_year": report.get("report_year", ""),
        "snpedia_online_hits": filtered_count,
        "findings_count": filtered_count,
        "total_snps": total,
        "data_source": "filtered_enriched_genome",
        "chromosome_summary": report.get("chromosome_summary", {}),
        "enriched_at_utc": report.get("enriched_at_utc", ""),
        "snpedia_database": report.get("snpedia_database", ""),
        "enrichment_summary": {
            "total_snps": total,
            "snpedia_hits": filtered_count,
            "note": "Filtered to meaningful hits only (magnitude > 0 or non-neutral repute)"
        },
        "findings": filtered_findings
    }
    
    # Write filtered report
    if verbose:
        print(f"  [VERBOSE] Writing to: {output_file}")
    else:
        print(f"  Writing to: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(filtered_report, f, separators=(',', ':'))
    
    file_size = os.path.getsize(output_file)
    if verbose:
        print(f"  [VERBOSE] New file size: {file_size / (1024*1024):.2f} MB")
    else:
        print(f"  New file size: {file_size / (1024*1024):.2f} MB")
    
    return filtered_report

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create smaller filtered enriched genome reports",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python create_small_enriched_report.py -i full.json -o small.json
    python create_small_enriched_report.py -i input.json -o output.json --verbose
    python create_small_enriched_report.py  # Uses default hardcoded paths
        """
    )
    parser.add_argument('-i', '--input', type=str, default=None,
                        help='Input JSON file path (default: uses built-in defaults)')
    parser.add_argument('-o', '--output', type=str, default=None,
                        help='Output JSON file path (default: uses built-in defaults)')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Enable verbose output')
    
    args = parser.parse_args()
    
    # If both input and output provided, process single file
    if args.input and args.output:
        if os.path.exists(args.input):
            create_small_enriched_report(args.input, args.output, verbose=args.verbose)
        else:
            print(f"Error: Input file not found: {args.input}")
            sys.exit(1)
    # Otherwise use default hardcoded paths
    elif args.input or args.output:
        parser.error("Both --input and --output must be specified together")
    else:
        # Process both 2025 reports (default behavior)
        reports = [
            ("2025-promethease-john/promethease_data/John_Stinson_2025_enriched.json", 
             "2025-promethease-john/promethease_data/John_Stinson_2025_enriched_small.json"),
            ("2025-promethease-trina/promethease_data/Trina_Toohey_2025_enriched.json",
             "2025-promethease-trina/promethease_data/Trina_Toohey_2025_enriched_small.json")
        ]
        
        for input_file, output_file in reports:
            if os.path.exists(input_file):
                create_small_enriched_report(input_file, output_file, verbose=args.verbose)
            else:
                print(f"Skipping {input_file} - file not found")
        
        print("\nDone!")