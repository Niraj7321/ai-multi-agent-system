@echo off
REM One-Click Windows Service Installer
echo ================================================================================
echo   AUTOMATED BLOGGER - WINDOWS SERVICE INSTALLER
echo ================================================================================
echo.
echo This will install the automated blogger as a Windows service that:
echo   * Runs 24/7 in the background
echo   * Starts automatically on boot
echo   * Continues even when windows are closed
echo   * Works even when logged out
echo.
echo ================================================================================
echo.
pause

cd /d "%~dp0"

echo.
echo Installing Windows Service...
echo.

python install_windows_service.py

echo.
echo ================================================================================
pause
