#!/usr/bin/env node
/**
 * Download campaign assets using replicate-predictions-downloader
 * Part of the Creative Production Pipeline
 */

const { spawn } = require('child_process');
const path = require('path');

// Configuration
const DOWNLOAD_CONFIGS = {
  'recent': '--since "1 hour ago"',
  'today': '--since "today"',
  'yesterday': '--since "yesterday"',
  'week': '--since "1 week ago"',
  'incremental': '--last-run'
};

function downloadAssets(timeframe = 'recent') {
  console.log('🔄 Downloading campaign assets...');
  console.log(`📅 Timeframe: ${timeframe}`);

  const config = DOWNLOAD_CONFIGS[timeframe] || DOWNLOAD_CONFIGS.recent;

  // Run the downloader
  const downloader = spawn('npx', [
    'replicate-predictions-downloader',
    ...config.split(' ')
  ], {
    shell: true,
    stdio: 'inherit'
  });

  downloader.on('close', (code) => {
    if (code === 0) {
      console.log('\n✅ Assets downloaded successfully!');
      console.log('📁 Check the replicate_outputs_* directory for your files');
    } else {
      console.error(`\n❌ Download failed with code ${code}`);
    }
  });

  downloader.on('error', (err) => {
    console.error('❌ Failed to start downloader:', err);
    console.log('\n💡 Install it with: npm install -g replicate-predictions-downloader');
  });
}

// CLI interface
if (require.main === module) {
  const args = process.argv.slice(2);
  const timeframe = args[0] || 'recent';

  console.log(`
╔════════════════════════════════════════════╗
║     CREATIVE ASSET DOWNLOADER              ║
║     Powered by replicate-predictions-      ║
║     downloader (npm)                       ║
╚════════════════════════════════════════════╝
`);

  if (args[0] === '--help') {
    console.log('Usage: node download_assets.js [timeframe]');
    console.log('\nTimeframes:');
    Object.keys(DOWNLOAD_CONFIGS).forEach(key => {
      console.log(`  ${key.padEnd(12)} - ${DOWNLOAD_CONFIGS[key]}`);
    });
    process.exit(0);
  }

  downloadAssets(timeframe);
}

module.exports = { downloadAssets };