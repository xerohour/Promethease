#!/usr/bin/env python3
"""
SNPedia Scraper - Downloads SNP data from SNPedia using their API.

Based on: https://github.com/jaykobdetar/SNPedia-Scraper

This tool scrapes SNPedia to build a local database of SNP information
including magnitude, repute, summary, and other clinical annotations.

Usage:
    python snpedia_scraper.py [--output DB_PATH] [--resume]

Example:
    python snpedia_scraper.py --output snpedia_data/mydb.sqlite
"""

import sqlite3
import requests
import time
import threading
import os
import sys
from datetime import datetime

class SNPediaScraper:
    """Scraper for SNPedia.com using their bot API."""
    
    API_URL = "https://bots.snpedia.com/api.php"
    USER_AGENT = "SNPedia-Scraper/1.0 ( genome research tool )"
    
    def __init__(self, db_path="snpedia_data.db", status_callback=None, log_callback=None):
        self.db_path = db_path
        self.status_callback = status_callback
        self.log_callback = log_callback
        self._headers = {'User-Agent': self.USER_AGENT}
        self._stop_event = threading.Event()
        self._pause_event = threading.Event()
        self._pause_event.set()  # Not paused initially
        
        # Ensure database directory exists
        db_dir = os.path.dirname(db_path)
        if db_dir and not os.path.exists(db_dir):
            os.makedirs(db_dir)
        
        self._init_db()
    
    def _log(self, message):
        """Log message via callback or print."""
        if self.log_callback:
            self.log_callback(message)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")
    
    def _status(self, message):
        """Update status via callback."""
        if self.status_callback:
            self.status_callback(message)
    
    def _init_db(self):
        """Initialize SQLite database with required tables."""
        conn = sqlite3.connect(self.db_path)
        try:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS snps (
                    rsid TEXT PRIMARY KEY,
                    content TEXT,
                    scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.execute('''
                CREATE TABLE IF NOT EXISTS progress (
                    key TEXT PRIMARY KEY,
                    value TEXT
                )
            ''')
            conn.commit()
        finally:
            conn.close()
    
    def get_scraped_count(self):
        """Get the number of SNPs already scraped."""
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.execute('SELECT COUNT(*) FROM snps')
            count = cursor.fetchone()[0]
        finally:
            conn.close()
        return count
    
    def get_continue_token(self):
        """Get the continue token for resuming."""
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.execute("SELECT value FROM progress WHERE key = 'cmcontinue'")
            result = cursor.fetchone()
            return result[0] if result else None
        finally:
            conn.close()
    
    def save_continue_token(self, token):
        """Save the continue token for resuming."""
        conn = sqlite3.connect(self.db_path)
        try:
            conn.execute("INSERT OR REPLACE INTO progress (key, value) VALUES ('cmcontinue', ?)", (token,))
            conn.commit()
        finally:
            conn.close()
    
    def is_rsid_scraped(self, rsid):
        """Check if an rsid has already been scraped."""
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.execute('SELECT 1 FROM snps WHERE rsid = ?', (rsid,))
            return cursor.fetchone() is not None
        finally:
            conn.close()
    
    def save_snp(self, rsid, content):
        """Save SNP content to database."""
        conn = sqlite3.connect(self.db_path)
        try:
            conn.execute(
                'INSERT OR IGNORE INTO snps (rsid, content, scraped_at) VALUES (?, ?, ?)',
                (rsid, content, datetime.now())
            )
            conn.commit()
        finally:
            conn.close()
    
    def fetch_snp_list(self, continue_token=None):
        """Fetch list of SNPs from Is_a_snp category."""
        params = {
            'action': 'query',
            'list': 'categorymembers',
            'cmtitle': 'Category:Is_a_snp',
            'cmlimit': '500',
            'format': 'json'
        }
        if continue_token:
            params['cmcontinue'] = continue_token
        
        response = requests.get(self.API_URL, params=params, headers=self._headers)
        data = response.json()
        
        members = data.get('query', {}).get('categorymembers', [])
        continue_info = data.get('continue', {})
        
        return members, continue_info.get('cmcontinue')
    
    def fetch_snp_content(self, rsid):
        """Fetch raw wiki content for a specific SNP."""
        params = {
            'action': 'query',
            'prop': 'revisions',
            'rvprop': 'content',
            'format': 'json',
            'titles': rsid
        }
        
        response = requests.get(self.API_URL, params=params, headers=self._headers)
        data = response.json()
        
        pages = data.get('query', {}).get('pages', {})
        for page_id, page_data in pages.items():
            if page_id == '-1':  # Page doesn't exist
                return None
            revisions = page_data.get('revisions', [])
            if revisions:
                return revisions[0].get('*')
        
        return None
    
    def _scrape_loop(self):
        """Main scraping loop running in background thread."""
        continue_token = self.get_continue_token()
        total_scraped = self.get_scraped_count()
        
        self._log(f"Starting scrape (already have {total_scraped} SNPs)")
        
        while not self._stop_event.is_set():
            # Check pause
            self._pause_event.wait()
            
            if self._stop_event.is_set():
                break
            
            # Fetch batch of SNPs
            members, continue_token = self.fetch_snp_list(continue_token)
            
            if not members:
                self._log("No more SNPs to fetch")
                break
            
            self._status(f"Fetching batch, continue token: {continue_token[:50] if continue_token else 'None'}...")
            
            # Process each SNP
            for member in members:
                if self._stop_event.is_set():
                    break
                
                self._pause_event.wait()
                
                rsid = member['title']
                
                # Skip already scraped
                if self.is_rsid_scraped(rsid):
                    continue
                
                # Fetch content
                content = self.fetch_snp_content(rsid)
                
                if content:
                    self.save_snp(rsid, content)
                    total_scraped += 1
                    
                    if total_scraped % 100 == 0:
                        self._status(f"Progress: {total_scraped} SNPs scraped")
                
                # Rate limiting - be respectful to SNPedia
                time.sleep(3)
            
            # Save continue token
            if continue_token:
                self.save_continue_token(continue_token)
            else:
                self._log("Scraping complete!")
                break
        
        self._log(f"Scraping finished. Total SNPs: {total_scraped}")
    
    def start(self):
        """Start scraping in background thread."""
        self._stop_event.clear()
        self._pause_event.set()
        self.thread = threading.Thread(target=self._scrape_loop, daemon=True)
        self.thread.start()
        return self
    
    def pause(self):
        """Pause scraping."""
        self._pause_event.clear()
        self._log("Paused")
    
    def resume(self):
        """Resume scraping."""
        self._pause_event.set()
        self._log("Resumed")
    
    def stop(self):
        """Stop scraping."""
        self._log("Stopping...")
        self._stop_event.set()
        self._pause_event.set()  # Unpause to allow thread to exit
        if hasattr(self, 'thread'):
            self.thread.join(timeout=5)
        self._log("Stopped")


def main():
    """CLI entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Scrape SNPedia for SNP data')
    parser.add_argument('--output', '-o', default='snpedia_data.db', 
                        help='Output database path (default: snpedia_data.db)')
    parser.add_argument('--resume', '-r', action='store_true',
                        help='Resume from previous run')
    parser.add_argument('--count', '-c', action='store_true',
                        help='Just show current count and exit')
    
    args = parser.parse_args()
    
    if args.count:
        scraper = SNPediaScraper(args.output)
        count = scraper.get_scraped_count()
        print(f"Database contains {count} SNPs")
        return
    
    scraper = SNPediaScraper(args.output)
    
    print(f"SNPedia Scraper")
    print(f"===============")
    print(f"Output: {args.output}")
    print(f"Already have: {scraper.get_scraped_count()} SNPs")
    print()
    print("Press Ctrl+C to stop (scraping continues in background)")
    print()
    
    scraper.start()
    
    try:
        while scraper.thread.is_alive():
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping...")
        scraper.stop()
    
    print(f"Final count: {scraper.get_scraped_count()} SNPs")


if __name__ == '__main__':
    main()