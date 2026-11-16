const http = require('http');
const fs = require('fs');
const path = require('path');
const url = require('url');
const os = require('os');

const PORT = process.env.PORT || 3000;
// Resolve UNIBO_ROOT whether executed from UniBo root or UniBo-Study-App subdirectory
const UNIBO_ROOT = fs.existsSync(path.join(__dirname, 'Exam_Strategy_Dashboard.html'))
  ? __dirname
  : (fs.existsSync(path.join(__dirname, '..', 'Exam_Strategy_Dashboard.html')) ? path.resolve(__dirname, '..') : __dirname);
const PROGRESS_FILE = path.join(UNIBO_ROOT, 'progress.json');
const APP_PROGRESS_FILE = path.join(__dirname, 'progress.json');
const BACKUPS_DIR = path.join(__dirname, 'backups');
const REVISION_NOTES_DIR = path.join(__dirname, 'revision_notes');

if (!fs.existsSync(BACKUPS_DIR)) {
  fs.mkdirSync(BACKUPS_DIR, { recursive: true });
}
if (!fs.existsSync(REVISION_NOTES_DIR)) {
  fs.mkdirSync(REVISION_NOTES_DIR, { recursive: true });
}


function getLocalIpAddress() {
  const nets = os.networkInterfaces();
  for (const name of Object.keys(nets)) {
    for (const net of nets[name]) {
      // Skip over non-IPv4 and internal (i.e. 127.0.0.1) addresses
      if (net.family === 'IPv4' && !net.internal) {
        return net.address;
      }
    }
  }
  return '192.168.1.54';
}

// MIME types dictionary
const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.pdf': 'application/pdf',
  '.py': 'text/plain; charset=utf-8',
  '.txt': 'text/plain; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.svg': 'image/svg+xml'
};

function getProgress() {
  try {
    const target = fs.existsSync(PROGRESS_FILE) ? PROGRESS_FILE : APP_PROGRESS_FILE;
    if (fs.existsSync(target)) {
      return JSON.parse(fs.readFileSync(target, 'utf-8'));
    }
  } catch (err) {
    console.error('Error reading progress:', err);
  }
  return { completed: {}, notes: {}, starred: {}, lastUpdated: new Date().toISOString() };
}

function saveProgress(data) {
  try {
    data.lastUpdated = new Date().toISOString();
    const str = JSON.stringify(data, null, 2);
    
    // Save to primary progress file in UniBo root
    fs.writeFileSync(PROGRESS_FILE, str, 'utf-8');
    // Save to app copy
    fs.writeFileSync(APP_PROGRESS_FILE, str, 'utf-8');
    
    // Save rolling backup (keep last 20 backups)
    const backupFile = path.join(BACKUPS_DIR, `progress-${Date.now()}.json`);
    fs.writeFileSync(backupFile, str, 'utf-8');

    // Clean old backups if > 20
    const files = fs.readdirSync(BACKUPS_DIR).filter(f => f.startsWith('progress-')).sort();
    if (files.length > 20) {
      for (let i = 0; i < files.length - 20; i++) {
        try { fs.unlinkSync(path.join(BACKUPS_DIR, files[i])); } catch(e) {}
      }
    }
    return true;
  } catch (err) {
    console.error('Error saving progress:', err);
    return false;
  }
}

const server = http.createServer((req, res) => {
  const parsedUrl = url.parse(req.url, true);
  let pathname = decodeURIComponent(parsedUrl.pathname);

  // CORS headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  // API Endpoints
  if (pathname === '/api/ping' || pathname === '/healthz' || pathname === '/health') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ status: 'ok', app: 'UniBo AI Master Tactical Glass', version: 4 }));
    return;
  }

  // API Config (Gemini API key & default model synchronization)
  if (pathname === '/api/config' && req.method === 'GET') {
    const progress = getProgress();
    const envKey = (process.env.GEMINI_API_KEY || '').trim();
    const diskKey = (progress.geminiApiKey || '').trim();
    const resolvedKey = diskKey || envKey;
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({
      hasKey: !!resolvedKey,
      defaultModel: progress.selectedModel || 'gemini-3.5-flash-lite',
      maskedKey: resolvedKey ? `${resolvedKey.slice(0, 6)}...${resolvedKey.slice(-4)}` : null,
      apiKey: resolvedKey || ''
    }));
    return;
  }

  if (pathname === '/api/config' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => { body += chunk; });
    req.on('end', () => {
      try {
        const payload = JSON.parse(body);
        const progress = getProgress();
        if (payload.apiKey !== undefined) {
          progress.geminiApiKey = (payload.apiKey || '').trim();
        }
        if (payload.selectedModel) {
          progress.selectedModel = payload.selectedModel;
        }
        saveProgress(progress);
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ 
          success: true, 
          hasKey: !!progress.geminiApiKey,
          maskedKey: progress.geminiApiKey ? `${progress.geminiApiKey.slice(0, 6)}...${progress.geminiApiKey.slice(-4)}` : null
        }));
      } catch (e) {
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: 'Invalid JSON' }));
      }
    });
    return;
  }

  if (pathname === '/api/progress' && req.method === 'GET') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify(getProgress()));
    return;
  }

  if (pathname === '/api/progress' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => { body += chunk; });
    req.on('end', () => {
      try {
        const payload = JSON.parse(body);
        const ok = saveProgress(payload);
        res.writeHead(ok ? 200 : 500, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ success: ok, progress: getProgress() }));
      } catch (e) {
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: 'Invalid JSON' }));
      }
    });
    return;
  }

  // Revision Notes API
  if (pathname === '/api/revision-notes' && req.method === 'GET') {
    const targetFile = parsedUrl.query.file;
    const progress = getProgress();
    if (!progress.revisionNotes) progress.revisionNotes = {};

    if (targetFile) {
      const notes = progress.revisionNotes[targetFile];
      if (notes) {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ exists: true, notes }));
        return;
      } else {
        res.writeHead(404, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ exists: false }));
        return;
      }
    } else {
      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify(progress.revisionNotes));
      return;
    }
  }

  if (pathname === '/api/revision-notes' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => { body += chunk; });
    req.on('end', () => {
      try {
        const payload = JSON.parse(body);
        if (!payload.filePath || !payload.markdown) {
          res.writeHead(400, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ error: 'Missing filePath or markdown' }));
          return;
        }

        const progress = getProgress();
        if (!progress.revisionNotes) progress.revisionNotes = {};

        const noteObj = {
          filePath: payload.filePath,
          courseId: payload.courseId || '',
          title: payload.title || path.basename(payload.filePath),
          markdown: payload.markdown,
          model: payload.model || 'gemini-3.5-flash-lite',
          stats: payload.stats || {},
          generatedAt: new Date().toISOString()
        };

        progress.revisionNotes[payload.filePath] = noteObj;
        saveProgress(progress);

        // Also save clean standalone .md file
        try {
          const safeName = path.basename(payload.filePath).replace(/\.[a-zA-Z0-9]+$/i, '') + '_Revision_Notes.md';
          const mdPath = path.join(REVISION_NOTES_DIR, safeName);
          fs.writeFileSync(mdPath, payload.markdown, 'utf-8');
        } catch(err) {
          console.error('Error writing standalone .md:', err);
        }

        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ success: true, notes: noteObj }));
      } catch (e) {
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: 'Invalid JSON' }));
      }
    });
    return;
  }

  if (pathname === '/api/courses' && req.method === 'GET') {
    const coursesFile = path.join(UNIBO_ROOT, 'scratch_courses_complete.json');
    if (fs.existsSync(coursesFile)) {
      res.writeHead(200, { 'Content-Type': 'application/json' });
      fs.createReadStream(coursesFile).pipe(res);
      return;
    }
  }

  // Root, dashboard, or multi-tab course study room routes
  if (pathname === '/' || pathname === '/index.html' || pathname === '/dashboard' || pathname.startsWith('/room') || pathname.startsWith('/study')) {
    const dashboardFile = path.join(UNIBO_ROOT, 'Exam_Strategy_Dashboard.html');
    if (fs.existsSync(dashboardFile)) {
      res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
      fs.createReadStream(dashboardFile).pipe(res);
      return;
    }
  }

  // Serve static files from UNIBO_ROOT
  // Remove leading slash
  let safeRel = pathname.replace(/^\/+/, '');
  let filePath = path.join(UNIBO_ROOT, safeRel);

  // Security check to avoid directory traversal outside UNIBO_ROOT
  const normalized = path.normalize(filePath);
  if (!normalized.startsWith(UNIBO_ROOT)) {
    res.writeHead(403, { 'Content-Type': 'text/plain' });
    res.end('Access denied');
    return;
  }

  if (fs.existsSync(filePath) && fs.statSync(filePath).isFile()) {
    const ext = path.extname(filePath).toLowerCase();
    const contentType = MIME_TYPES[ext] || 'application/octet-stream';
    const stat = fs.statSync(filePath);

    // Support byte ranges for PDF scrubbing
    const range = req.headers.range;
    if (range && ext === '.pdf') {
      const parts = range.replace(/bytes=/, "").split("-");
      const start = parseInt(parts[0], 10);
      const end = parts[1] ? parseInt(parts[1], 10) : stat.size - 1;
      const chunksize = (end - start) + 1;
      const fileStream = fs.createReadStream(filePath, { start, end });
      res.writeHead(206, {
        'Content-Range': `bytes ${start}-${end}/${stat.size}`,
        'Accept-Ranges': 'bytes',
        'Content-Length': chunksize,
        'Content-Type': contentType,
      });
      fileStream.pipe(res);
      return;
    }

    res.writeHead(200, {
      'Content-Type': contentType,
      'Content-Length': stat.size,
      'Accept-Ranges': 'bytes'
    });
    fs.createReadStream(filePath).pipe(res);
    return;
  }

  res.writeHead(404, { 'Content-Type': 'text/plain' });
  res.end('404 Not Found: ' + pathname);
});

const HOST = process.env.HOST || '0.0.0.0';
server.listen(PORT, HOST, () => {
  const localIp = getLocalIpAddress();
  console.log(`=======================================================`);
  console.log(` UniBo AI Master – Tactical Obsidian Study Hub Online!`);
  console.log(` 👉 Open in Desktop Browser: http://localhost:${PORT}`);
  console.log(` 📱 Open on Mobile (Same Wi-Fi): http://${localIp}:${PORT}`);
  console.log(` 💾 Auto-saving to disk: ${PROGRESS_FILE}`);
  console.log(`=======================================================`);
});
