@echo off
title Sync UniBo Changes to GitHub
echo ========================================================
echo  Syncing local updates to GitHub (Willayat060/unibo-ai-master)...
echo ========================================================
echo.
git add .
git commit -m "Sync progress, notes, and curriculum updates: %date% %time%"
git push origin main
echo.
echo ========================================================
echo  Synced successfully to https://github.com/Willayat060/unibo-ai-master!
echo ========================================================
pause
