@echo off
title UniBo AI Master Study Hub
cd /d "%~dp0\UniBo-Study-App"
echo Starting UniBo AI Master Study Server on http://localhost:3000...
start "" http://localhost:3000
node server.js
pause

