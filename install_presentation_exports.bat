@echo off
echo.
echo ============================================
echo   Install Presentation Export Libraries
echo ============================================
echo.

echo Installing PowerPoint export (python-pptx)...
pip install python-pptx>=0.6.23

echo.
echo Installing HTML/Markdown conversion (markdown2)...
pip install markdown2>=2.4.0 markdown>=3.5.0

echo.
echo Installing PDF export (weasyprint)...
pip install weasyprint>=60.0

echo.
echo ============================================
echo   Installation Complete!
echo ============================================
echo.
echo You can now export presentations to:
echo   - PowerPoint (.pptx)
echo   - HTML (.html)
echo   - PDF (.pdf)
echo   - Markdown (.md)
echo.
pause
