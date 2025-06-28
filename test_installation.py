#!/usr/bin/env python3
"""
Test script to verify the Desktop File Organizer installation.
"""

import sys
import os
from pathlib import Path

def test_python_version():
    """Test if Python version is compatible."""
    print("Testing Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 7:
        print(f"✓ Python {version.major}.{version.minor}.{version.micro} - Compatible")
        return True
    else:
        print(f"✗ Python {version.major}.{version.minor}.{version.micro} - Requires Python 3.7+")
        return False

def test_watchdog():
    """Test if watchdog is installed."""
    print("Testing watchdog installation...")
    try:
        import watchdog
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler
        print(f"✓ watchdog - Installed successfully")
        return True
    except ImportError as e:
        print(f"✗ watchdog - Not installed: {e}")
        return False

def test_desktop_access():
    """Test if we can access the Desktop folder."""
    print("Testing Desktop folder access...")
    try:
        desktop_path = Path.home() / "Desktop"
        if desktop_path.exists():
            print(f"✓ Desktop folder found: {desktop_path}")
            
            # Test write permissions
            test_file = desktop_path / "test_write_permission.tmp"
            try:
                test_file.write_text("test")
                test_file.unlink()  # Clean up
                print("✓ Write permission to Desktop - OK")
                return True
            except Exception as e:
                print(f"✗ Write permission to Desktop - Failed: {e}")
                return False
        else:
            print(f"✗ Desktop folder not found: {desktop_path}")
            return False
    except Exception as e:
        print(f"✗ Desktop access test failed: {e}")
        return False

def test_file_organizer_import():
    """Test if we can import the file organizer."""
    print("Testing file organizer import...")
    try:
        # Add current directory to path
        current_dir = Path(__file__).parent
        sys.path.insert(0, str(current_dir))
        
        # Try to import the main module
        import file_organizer
        print("✓ file_organizer.py - Import successful")
        return True
    except ImportError as e:
        print(f"✗ file_organizer.py - Import failed: {e}")
        return False
    except Exception as e:
        print(f"✗ file_organizer.py - Error: {e}")
        return False

def test_category_folders():
    """Test if category folders can be created."""
    print("Testing category folder creation...")
    try:
        from file_organizer import FileOrganizer
        
        # Create a temporary organizer instance
        organizer = FileOrganizer()
        
        # Test creating category folders
        for category in organizer.file_categories.keys():
            category_path = organizer.desktop_path / category
            if not category_path.exists():
                category_path.mkdir(exist_ok=True)
                print(f"✓ Created folder: {category}")
            else:
                print(f"✓ Folder exists: {category}")
        
        print("✓ Category folder creation - OK")
        return True
    except Exception as e:
        print(f"✗ Category folder creation failed: {e}")
        return False

def main():
    """Run all tests."""
    print("Desktop File Organizer - Installation Test")
    print("=" * 50)
    print()
    
    tests = [
        test_python_version,
        test_watchdog,
        test_desktop_access,
        test_file_organizer_import,
        test_category_folders
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"✗ Test failed with exception: {e}")
        print()
    
    print("=" * 50)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The file organizer is ready to use.")
        print()
        print("Next steps:")
        print("1. Run: python file_organizer.py")
        print("2. Or set up automatic startup: setup_task_scheduler.bat")
        print("3. Or create executable: build_exe.bat")
    else:
        print("❌ Some tests failed. Please fix the issues above.")
        print()
        print("Common solutions:")
        print("1. Install dependencies: install_dependencies.bat")
        print("2. Run as Administrator if permission issues occur")
        print("3. Check Python installation and PATH")

if __name__ == "__main__":
    main() 