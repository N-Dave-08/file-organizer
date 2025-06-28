@echo off
echo Desktop File Organizer - Install Dependencies
echo =============================================
echo.

echo Installing required Python packages...
echo.

REM Install watchdog
echo Installing watchdog...
pip install watchdog

if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to install watchdog
    echo Please check your Python installation and internet connection.
    pause
    exit /b 1
)

echo.
echo SUCCESS: All dependencies installed successfully!
echo.
echo You can now run the file organizer with:
echo   python file_organizer.py
echo.
echo Optional: Install PyInstaller to create an executable:
echo   pip install pyinstaller
echo   build_exe.bat
echo.
pause 