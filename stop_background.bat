@echo off
REM Stop Background Blogger Service
echo Stopping background blogger service...
python run_background.py --stop
pause
