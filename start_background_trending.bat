@echo off
REM Start Trending Blogger in Background
echo Starting Trending Topics Blogger in background...
cd /d "%~dp0"
start /B pythonw trending_blogger_background.py
echo.
echo Background service started!
echo Check logs at: logs\app.log
echo To stop: run stop_background.bat
pause
