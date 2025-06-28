# Quick Start Guide

Get your Desktop File Organizer up and running in 5 minutes!

## 🚀 Quick Setup (Windows)

### Step 1: Install Dependencies
Double-click `install_dependencies.bat` or run:
```cmd
pip install watchdog
```

### Step 2: Test Installation
Run the test script to make sure everything works:
```cmd
python test_installation.py
```

### Step 3: Start the File Organizer
```cmd
python file_organizer.py
```

That's it! The organizer will now automatically move files from your Desktop into organized folders.

## 📁 What Happens

When you drop files on your Desktop, they'll be automatically moved to:
- **Images** folder: .jpg, .png, .gif, etc.
- **Documents** folder: .pdf, .doc, .txt, etc.
- **Videos** folder: .mp4, .avi, .mov, etc.
- **Audio** folder: .mp3, .wav, .flac, etc.
- And many more categories...

## 🔄 Auto-Start Options

### Option A: Simple Setup
Double-click `setup_task_scheduler.bat`

### Option B: Advanced Setup (PowerShell)
```powershell
.\setup_task_scheduler.ps1
```

### Option C: Create Executable (No Console Window)
```cmd
build_exe.bat
```

## 🛠️ Troubleshooting

**Files not moving?**
- Check `file_organizer.log` for errors
- Make sure the file is fully saved before moving

**Permission errors?**
- Run as Administrator
- Check Desktop folder permissions

**Task Scheduler not working?**
- Verify Python path in Task Scheduler
- Test the command manually first

## 📞 Need Help?

1. Run `test_installation.py` to diagnose issues
2. Check the full README.md for detailed instructions
3. Look at the log file for error details

## 🎯 Pro Tips

- **Customize categories**: Edit `file_organizer.py` to add your own file types
- **Silent mode**: Use the executable version for no console window
- **Multiple monitors**: Works with any Desktop location
- **Safe operation**: Only moves files, never deletes them

---

**Ready to organize your Desktop?** Just run `python file_organizer.py` and start dropping files! 🎉 