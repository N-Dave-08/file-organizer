@echo off
echo Desktop File Organizer - Build Executable
echo =========================================
echo.

REM Check if PyInstaller is installed
python -c "import PyInstaller" 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Installing PyInstaller...
    pip install pyinstaller
    if %ERRORLEVEL% NEQ 0 (
        echo ERROR: Failed to install PyInstaller
        pause
        exit /b 1
    )
)

echo Building executable...
echo.

REM Build the executable
pyinstaller --onefile --windowed --name "Desktop File Organizer" file_organizer.py

if %ERRORLEVEL% EQU 0 (
    echo.
    echo SUCCESS: Executable created successfully!
    echo.
    echo Location: dist\Desktop File Organizer.exe
    echo.
    echo You can now:
    echo 1. Run the executable directly by double-clicking it
    echo 2. Use it in Task Scheduler instead of the Python script
    echo 3. Copy it to a permanent location
    echo.
    echo To use in Task Scheduler:
    echo - Program/script: "C:\path\to\Desktop File Organizer.exe"
    echo - Remove the "Add arguments" field
    echo - Start in: "C:\path\to\your\desktop\folder"
) else (
    echo.
    echo ERROR: Failed to build the executable.
    echo Check the error messages above.
)

echo.
pause 