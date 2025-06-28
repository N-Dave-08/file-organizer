# Desktop File Organizer - PowerShell Task Scheduler Setup
# Run this script as Administrator for best results

param(
    [switch]$UseExecutable,
    [string]$ExecutablePath = "",
    [switch]$Force
)

Write-Host "Desktop File Organizer - Task Scheduler Setup" -ForegroundColor Green
Write-Host "=============================================" -ForegroundColor Green
Write-Host ""

# Get the current directory
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$PythonScript = Join-Path $ScriptDir "file_organizer.py"

# Check if we should use executable
if ($UseExecutable) {
    if ($ExecutablePath -eq "") {
        $ExecutablePath = Join-Path $ScriptDir "dist\Desktop File Organizer.exe"
    }
    
    if (-not (Test-Path $ExecutablePath)) {
        Write-Host "ERROR: Executable not found at: $ExecutablePath" -ForegroundColor Red
        Write-Host "Please build the executable first using build_exe.bat" -ForegroundColor Yellow
        exit 1
    }
    
    $Action = New-ScheduledTaskAction -Execute $ExecutablePath
    $WorkingDirectory = Split-Path -Parent $ExecutablePath
} else {
    # Check if the Python script exists
    if (-not (Test-Path $PythonScript)) {
        Write-Host "ERROR: file_organizer.py not found in the current directory." -ForegroundColor Red
        Write-Host "Please run this script from the same directory as file_organizer.py" -ForegroundColor Yellow
        exit 1
    }
    
    $Action = New-ScheduledTaskAction -Execute "python" -Argument "`"$PythonScript`"" -WorkingDirectory $ScriptDir
    $WorkingDirectory = $ScriptDir
}

# Create trigger (at startup)
$Trigger = New-ScheduledTaskTrigger -AtStartup

# Create principal (current user with highest privileges)
$Principal = New-ScheduledTaskPrincipal -UserId "$env:USERDOMAIN\$env:USERNAME" -LogonType Interactive -RunLevel Highest

# Create settings
$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable

# Check if task already exists
$ExistingTask = Get-ScheduledTask -TaskName "Desktop File Organizer" -ErrorAction SilentlyContinue

if ($ExistingTask -and -not $Force) {
    Write-Host "Task 'Desktop File Organizer' already exists." -ForegroundColor Yellow
    $Response = Read-Host "Do you want to replace it? (y/N)"
    if ($Response -ne "y" -and $Response -ne "Y") {
        Write-Host "Setup cancelled." -ForegroundColor Yellow
        exit 0
    }
}

try {
    # Register the task
    if ($ExistingTask) {
        Unregister-ScheduledTask -TaskName "Desktop File Organizer" -Confirm:$false
    }
    
    Register-ScheduledTask -TaskName "Desktop File Organizer" -Action $Action -Trigger $Trigger -Principal $Principal -Settings $Settings -Description "Automatically organizes Desktop files by type"
    
    Write-Host ""
    Write-Host "SUCCESS: Task Scheduler task created successfully!" -ForegroundColor Green
    Write-Host ""
    Write-Host "Task Details:" -ForegroundColor Cyan
    Write-Host "  Name: Desktop File Organizer"
    Write-Host "  Trigger: At system startup"
    Write-Host "  User: $env:USERDOMAIN\$env:USERNAME"
    Write-Host "  Working Directory: $WorkingDirectory"
    
    if ($UseExecutable) {
        Write-Host "  Type: Executable"
        Write-Host "  Path: $ExecutablePath"
    } else {
        Write-Host "  Type: Python Script"
        Write-Host "  Script: $PythonScript"
    }
    
    Write-Host ""
    Write-Host "The file organizer will now start automatically when you log in." -ForegroundColor Green
    Write-Host ""
    Write-Host "To manage the task:" -ForegroundColor Yellow
    Write-Host "  - View/Edit: Open Task Scheduler (Win+R, type: taskschd.msc)"
    Write-Host "  - Delete: schtasks /delete /tn 'Desktop File Organizer' /f"
    Write-Host "  - Test: schtasks /run /tn 'Desktop File Organizer'"
    
} catch {
    Write-Host ""
    Write-Host "ERROR: Failed to create the scheduled task." -ForegroundColor Red
    Write-Host "Error: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host ""
    Write-Host "You may need to run this script as Administrator." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Manual setup instructions:" -ForegroundColor Cyan
    Write-Host "1. Open Task Scheduler (Win+R, type: taskschd.msc)"
    Write-Host "2. Create Basic Task"
    Write-Host "3. Name: Desktop File Organizer"
    Write-Host "4. Trigger: When the computer starts"
    Write-Host "5. Action: Start a program"
    
    if ($UseExecutable) {
        Write-Host "6. Program: $ExecutablePath"
    } else {
        Write-Host "6. Program: python"
        Write-Host "7. Arguments: `"$PythonScript`""
        Write-Host "8. Start in: $ScriptDir"
    }
}

Write-Host ""
Read-Host "Press Enter to continue" 