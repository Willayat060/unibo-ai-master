@echo off
title UniBo AI Master - Remote Mobile Tunnel
echo ===================================================================
echo  UniBo AI Master Study Hub - Mobile & Remote Tunnel Launcher
echo ===================================================================
echo.
echo [1/2] Starting local Node.js server...
start "UniBo Study Server" /b node UniBo-Study-App\server.js
timeout /t 2 >nul
echo.
echo [2/2] Generating secure HTTPS tunnel for your phone...
echo.
echo ===================================================================
echo  INSTRUCTIONS:
echo  1. Open the URL shown below on your phone (e.g. https://xxxx.loca.lt)
echo  2. If prompted for "Friendly Tunnel Password", your IP is shown in the terminal.
echo  3. Enjoy reading your lecture slides and asking AI Copilot on your phone!
echo ===================================================================
echo.
npx localtunnel --port 3000
pause
