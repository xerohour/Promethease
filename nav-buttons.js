// Navigation buttons for all Promethease report pages
// Automatically adds Home and All Reports buttons to any page

(function() {
  'use strict';

  // Determine paths based on current location
  const path = window.location.pathname;
  
  // Calculate correct relative paths from any depth
  const depth = (path.match(/\//g) || []).length - 1;
  const upDir = depth > 1 ? '../'.repeat(depth - 1) : './';
  
  const HOME_PATH = upDir + 'index.html';
  const ALL_REPORTS_PATH = upDir + 'all-reports.html';
  
  // Only add buttons if not already on index or all-reports
  const isIndex = path.endsWith('/index.html') || path === '/' || path.endsWith('/');
  const isAllReports = path.includes('all-reports.html');
  
  if (isIndex && !isAllReports) return;

  // Create the navigation container
  function createNavButtons() {
    // Check if buttons already exist (either via ID or by class)
    if (document.getElementById('promethease-nav-buttons')) return;
    if (document.querySelector('.nav-home-btn')) return;
    
    const container = document.createElement('div');
    container.id = 'promethease-nav-buttons';
    container.style.cssText = `
      position: fixed;
      top: 12px;
      right: 12px;
      z-index: 99999;
      display: flex;
      gap: 8px;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    `;

    // Home button
    const homeBtn = document.createElement('a');
    homeBtn.href = HOME_PATH;
    homeBtn.innerHTML = '🏠 Home';
    homeBtn.style.cssText = `
      background: #2d2d2d;
      color: #e0e0e0;
      border: 1px solid #444;
      padding: 6px 12px;
      border-radius: 6px;
      text-decoration: none;
      font-size: 13px;
      transition: all 0.2s;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    `;
    homeBtn.onmouseover = function() {
      this.style.background = '#444';
      this.style.color = '#fff';
    };
    homeBtn.onmouseout = function() {
      this.style.background = '#2d2d2d';
      this.style.color = '#e0e0e0';
    };

    // All Reports button
    const allBtn = document.createElement('a');
    allBtn.href = ALL_REPORTS_PATH;
    allBtn.textContent = 'All Reports';
    allBtn.style.cssText = `
      background: #1a1a2e;
      color: #4fc3f7;
      border: 1px solid #4fc3f7;
      padding: 6px 12px;
      border-radius: 6px;
      text-decoration: none;
      font-size: 13px;
      transition: all 0.2s;
      display: inline-flex;
      align-items: center;
    `;
    allBtn.onmouseover = function() {
      this.style.background = '#4fc3f7';
      this.style.color = '#1a1a2e';
    };
    allBtn.onmouseout = function() {
      this.style.background = '#1a1a2e';
      this.style.color = '#4fc3f7';
    };

    container.appendChild(homeBtn);
    container.appendChild(allBtn);
    
    return container;
  }

  // Try to add buttons, with retries for dynamic pages
  function addButtons() {
    const container = createNavButtons();
    if (container) {
      document.body.appendChild(container);
    }
  }

  // Run immediately
  if (document.body) {
    addButtons();
  } else {
    // Wait for body to be ready
    document.addEventListener('DOMContentLoaded', addButtons);
  }

  // Also try after a delay for dynamically loaded content
  setTimeout(addButtons, 1000);
  setTimeout(addButtons, 3000);
})();