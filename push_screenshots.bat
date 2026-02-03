@echo off
echo.
echo ============================================
echo   Push Screenshots to GitHub
echo ============================================
echo.

cd /d "%~dp0"

echo Checking for screenshots...
if exist "images\screenshots\*.png" (
    echo Found screenshots!
    echo.

    echo Adding screenshots to git...
    git add images/
    git add README.md
    git add SCREENSHOTS_GUIDE.md
    git add push_screenshots.bat

    echo.
    echo Creating commit...
    git commit -m "Add professional screenshots and demo images

- Added AI Multi-Agent dashboard screenshots
- Added NrjAi Exam platform screenshots
- Added blog system screenshots
- Updated README with image gallery
- Enhanced visual presentation for portfolio
- Added comprehensive screenshots guide

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"

    echo.
    echo Pushing to GitHub...
    git push origin main

    echo.
    echo ============================================
    echo   SUCCESS! Screenshots pushed to GitHub
    echo ============================================
    echo.
    echo View your repository:
    echo https://github.com/Niraj7321/ai-multi-agent-system
    echo.

) else (
    echo.
    echo ERROR: No screenshots found in images/screenshots/
    echo.
    echo Please add screenshots first:
    echo 1. Take screenshots using Windows + Shift + S
    echo 2. Save as PNG in images/screenshots/ folder
    echo 3. Run this script again
    echo.
    echo See SCREENSHOTS_GUIDE.md for detailed instructions
    echo.
)

pause
