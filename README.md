# Desktop File Organizer

A Python application that automatically monitors your Desktop folder and organizes files by their extensions into categorized folders (Images, Documents, Videos, etc.) in real-time.

## Features

- **Real-time monitoring** of Desktop folder using `watchdog`
- **Automatic file categorization** based on file extensions
- **Comprehensive file type support** including images, documents, videos, audio, archives, and more
- **Duplicate file handling** with automatic renaming
- **Detailed logging** with both console and file output
- **Safe file operations** with delay to ensure files are fully saved
- **Easy customization** of file categories and extensions

## Supported File Categories

- **Images**: .jpg, .jpeg, .png, .gif, .bmp, .tiff, .svg, .webp, .ico, .raw, .heic
- **Documents**: .pdf, .doc, .docx, .txt, .rtf, .odt, .pages, .md, .tex, .csv, .xls, .xlsx, .ppt, .pptx
- **Videos**: .mp4, .avi, .mov, .wmv, .flv, .webm, .mkv, .m4v, .3gp, .ogv, .ts, .mts
- **Audio**: .mp3, .wav, .flac, .aac, .ogg, .wma, .m4a, .opus, .aiff, .alac
- **Archives**: .zip, .rar, .7z, .tar, .gz, .bz2, .xz, .iso, .dmg, .pkg
- **Executables**: .exe, .msi, .app, .dmg, .deb, .rpm, .pkg, .bat, .cmd, .sh, .py, .jar
- **Code**: .py, .js, .html, .css, .java, .cpp, .c, .h, .php, .rb, .go, .rs, .swift, .kt, .ts, .jsx, .tsx, .vue, .svelte
- **Fonts**: .ttf, .otf, .woff, .woff2, .eot, .svg
- **3D Models**: .obj, .fbx, .dae, .3ds, .blend, .max, .ma, .mb, .stl, .ply, .wrl
- **CAD Files**: .dwg, .dxf, .step, .stp, .iges, .igs, .sldprt, .sldasm, .prt, .asm
- **Database**: .db, .sqlite, .sql, .mdb, .accdb, .odb, .fdb, .db3
- **Other**: Any file type not covered by the above categories

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Install Dependencies

Open Command Prompt or PowerShell and run:

```bash
pip install -r requirements.txt
```

Or install watchdog directly:

```bash
pip install watchdog
```

### Step 2: Run the Application

```bash
python file_organizer.py
```

The application will:
1. Create category folders on your Desktop (if they don't exist)
2. Start monitoring for new files
3. Automatically move files to appropriate folders when they appear on the Desktop

## Usage

### Basic Usage

1. **Start the application**:
   ```bash
   python file_organizer.py
   ```

2. **Drop files on your Desktop** - they will be automatically organized

3. **Stop the application** by pressing `Ctrl+C`

### Customization

You can modify the file categories and extensions by editing the `file_categories` dictionary in `file_organizer.py`:

```python
self.file_categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', ...],
    'Documents': ['.pdf', '.doc', '.docx', ...],
    # Add your own categories here
}
```

## Setting Up Automatic Startup (Windows Task Scheduler)

### Method 1: Using Task Scheduler GUI

1. **Open Task Scheduler**:
   - Press `Win + R`, type `taskschd.msc`, and press Enter

2. **Create Basic Task**:
   - Click "Create Basic Task" in the right panel
   - Name: "Desktop File Organizer"
   - Description: "Automatically organizes Desktop files by type"

3. **Set Trigger**:
   - Choose "When the computer starts"
   - Click Next

4. **Set Action**:
   - Choose "Start a program"
   - Program/script: `python`
   - Add arguments: `"C:\path\to\your\file_organizer.py"`
   - Start in: `C:\path\to\your\project\folder`

5. **Finish**:
   - Review settings and click Finish

### Method 2: Using Command Line

Create a batch file (`start_organizer.bat`):

```batch
@echo off
cd /d "C:\path\to\your\project\folder"
python file_organizer.py
```

Then create the task via command line:

```cmd
schtasks /create /tn "Desktop File Organizer" /tr "C:\path\to\start_organizer.bat" /sc onstart /ru "YourUsername" /rl highest
```

### Method 3: Using PowerShell Script

Create a PowerShell script (`setup_task.ps1`):

```powershell
$action = New-ScheduledTaskAction -Execute "python" -Argument "C:\path\to\your\file_organizer.py" -WorkingDirectory "C:\path\to\your\project\folder"
$trigger = New-ScheduledTaskTrigger -AtStartup
$principal = New-ScheduledTaskPrincipal -UserId "$env:USERDOMAIN\$env:USERNAME" -LogonType Interactive -RunLevel Highest
Register-ScheduledTask -TaskName "Desktop File Organizer" -Action $action -Trigger $trigger -Principal $principal -Description "Automatically organizes Desktop files by type"
```

## Creating an Executable (.exe) with PyInstaller

### Step 1: Install PyInstaller

```bash
pip install pyinstaller
```

### Step 2: Create the Executable

#### Option A: Console Application
```bash
pyinstaller --onefile file_organizer.py
```

#### Option B: Windowless Application (Recommended)
```bash
pyinstaller --onefile --windowed --name "Desktop File Organizer" file_organizer.py
```

#### Option C: With Icon (if you have one)
```bash
pyinstaller --onefile --windowed --icon=icon.ico --name "Desktop File Organizer" file_organizer.py
```

### Step 3: Find Your Executable

The executable will be created in the `dist` folder. You can:
- Run it directly by double-clicking
- Use it in Task Scheduler instead of the Python script
- Copy it to a permanent location

### Step 4: Update Task Scheduler (if using .exe)

If you created an executable, update your Task Scheduler action to use the .exe file instead:

- Program/script: `C:\path\to\Desktop File Organizer.exe`
- Remove the "Add arguments" field
- Start in: `C:\path\to\your\desktop\folder`

## Troubleshooting

### Common Issues

1. **Permission Errors**:
   - Run as Administrator or ensure you have write permissions to the Desktop folder

2. **Files Not Moving**:
   - Check the log file (`file_organizer.log`) for error messages
   - Ensure the file is fully saved before the script tries to move it

3. **Task Scheduler Not Working**:
   - Verify the path to Python or the executable is correct
   - Check that the user account has the necessary permissions
   - Test the command manually first

4. **Duplicate Files**:
   - The script automatically handles duplicates by adding a number suffix

### Log Files

The application creates a log file (`file_organizer.log`) in the same directory as the script. Check this file for detailed information about file operations and any errors.

## Security Considerations

- The script only monitors and moves files on your Desktop
- It doesn't delete files, only moves them
- All operations are logged for transparency
- The script runs with your user permissions

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this project.

## License

This project is open source and available under the MIT License.
