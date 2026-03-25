#!/usr/bin/env python3
"""
Download SNPedia data dump for local processing.

SNPedia provides data dumps at: https://www.snpedia.com/index.php/SNPedia:Data_dumps
The data is typically available as a gzip-compressed JSON file.

Usage: python download_snpedia_dump.py [--output_dir DIR]
"""

import os
import sys
import argparse
import urllib.request
import gzip
import json
from datetime import datetime

# SNPedia data dump URL (check for latest)
SNPEDIA_DUMP_URLS = [
    "https://www.snpedia.com/snpdump.json.gz",  # Main dump
    "https://gist.githubusercontent.com/snpedia/snpedia-mirror/master/snpdump.json.gz",  # Mirror
]

DEFAULT_OUTPUT_DIR = "snpedia_data"


def download_file(url, output_path, chunk_size=8192):
    """Download a file with progress indication."""
    print(f"Downloading from: {url}")
    print(f"Saving to: {output_path}")
    
    try:
        with urllib.request.urlopen(url, timeout=300) as response:
            total_size = response.headers.get('Content-Length')
            if total_size:
                total_size = int(total_size)
                print(f"Total size: {total_size / (1024*1024):.1f} MB")
            
            downloaded = 0
            with open(output_path, 'wb') as f:
                while True:
                    chunk = response.read(chunk_size)
                    if not chunk:
                        break
                    f.write(chunk)
                    downloaded += len(chunk)
                    if total_size:
                        progress = (downloaded / total_size) * 100
                        print(f"\rProgress: {progress:.1f}%", end='', flush=True)
        
        print(f"\nDownload complete: {output_path}")
        return True
        
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return False


def extract_json(gz_path, output_path):
    """Extract JSON from gzip file."""
    print(f"Extracting {gz_path} to {output_path}")
    
    try:
        with gzip.open(gz_path, 'rt', encoding='utf-8') as gz:
            # Count lines to show progress
            content = gz.read()
            
        # Try to parse as JSON array or JSONL
        try:
            data = json.loads(content)
        except json.JSONDecodeError:
            # Try JSONL format
            lines = content.strip().split('\n')
            data = []
            for line in lines:
                if line.strip():
                    data.append(json.loads(line))
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        
        print(f"Extracted {len(data)} SNP records to {output_path}")
        return True
        
    except Exception as e:
        print(f"Error extracting: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Download SNPedia data dump")
    parser.add_argument('--output_dir', default=DEFAULT_OUTPUT_DIR, help='Output directory')
    parser.add_argument('--skip_download', action='store_true', help='Skip download, just try extract')
    args = parser.parse_args()
    
    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)
    
    gz_path = os.path.join(args.output_dir, "snpdump.json.gz")
    json_path = os.path.join(args.output_dir, "snpdump.json")
    
    # Try downloading
    if not args.skip_download:
        success = False
        for url in SNPEDIA_DUMP_URLS:
            if download_file(url, gz_path):
                success = True
                break
        
        if not success:
            print("\nFailed to download from all URLs.")
            print("Please manually download from: https://www.snpedia.com/index.php/SNPedia:Data_dumps")
            print(f"Place the file at: {gz_path}")
            sys.exit(1)
    
    # Extract if exists
    if os.path.exists(gz_path):
        extract_json(gz_path, json_path)
        print(f"\nSNPedia data ready at: {json_path}")
    else:
        print(f"\nNo dump file found at: {gz_path}")
        sys.exit(1)


if __name__ == "__main__":
    main()