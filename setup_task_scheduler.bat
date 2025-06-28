@echo off
echo Desktop File Organizer - Task Scheduler Setup
echo =============================================
echo.

REM Get the current directory
set "SCRIPT_DIR=%~dp0"
set "PYTHON_SCRIPT=%SCRIPT_DIR%file_organizer.py"

REM Check if the Python script exists
if not exist "%PYTHON_SCRIPT%" (
    echo ERROR: file_organizer.py not found in the current directory.
    echo Please run this batch file from the same directory as file_organizer.py
    pause
    exit /b 1
)

echo Creating Windows Task Scheduler task...
echo.

REM Create the scheduled task
schtasks /create /tn "Desktop File Organizer" /tr "python \"%PYTHON_SCRIPT%\"" /sc onstart /ru "%USERNAME%" /rl highest /f

if %ERRORLEVEL% EQU 0 (
    echo.
    echo SUCCESS: Task Scheduler task created successfully!
    echo.
    echo Task Name: Desktop File Organizer
    echo Trigger: At system startup
    echo User: %USERNAME%
    echo.
    echo The file organizer will now start automatically when you log in.
    echo To disable it, open Task Scheduler and delete the "Desktop File Organizer" task.
) else (
    echo.
    echo ERROR: Failed to create the scheduled task.
    echo You may need to run this as Administrator.
    echo.
    echo Manual setup instructions:
    echo 1. Open Task Scheduler (Win+R, type: taskschd.msc)
    echo 2. Create Basic Task
    echo 3. Name: Desktop File Organizer
    echo 4. Trigger: When the computer starts
    echo 5. Action: Start a program
    echo 6. Program: python
    echo 7. Arguments: "%PYTHON_SCRIPT%"
    echo 8. Start in: "%SCRIPT_DIR%"
)

echo.
pause 