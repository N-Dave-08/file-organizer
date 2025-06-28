#!/usr/bin/env python3
"""
Desktop File Organizer

A Python script that monitors the Desktop folder and automatically organizes
files by their extensions into categorized folders (Images, Documents, Videos, etc.).

Usage:
    python file_organizer.py

Dependencies:
    - watchdog
"""

import os
import time
import shutil
import logging
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('file_organizer.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class FileOrganizer:
    """Main class for organizing files on the Desktop."""
    
    def __init__(self, desktop_path=None):
        """Initialize the file organizer with the desktop path."""
        if desktop_path is None:
            self.desktop_path = Path.home() / "Desktop"
        else:
            self.desktop_path = Path(desktop_path)
        
        # File extension to category mapping
        self.file_categories = {
            # Images
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.svg', '.webp', '.ico', '.raw', '.heic'],
            
            # Documents
            'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.pages', '.md', '.tex', '.csv', '.xls', '.xlsx', '.ppt', '.pptx', '.odp', '.ods'],
            
            # Videos
            'Videos': ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.webm', '.mkv', '.m4v', '.3gp', '.ogv', '.ts', '.mts', '.m2ts'],
            
            # Audio
            'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a', '.opus', '.aiff', '.alac'],
            
            # Archives
            'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.iso', '.dmg', '.pkg'],
            
            # Executables
            'Executables': ['.exe', '.msi', '.app', '.dmg', '.deb', '.rpm', '.pkg', '.bat', '.cmd', '.sh', '.py', '.jar'],
            
            # Code
            'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.h', '.php', '.rb', '.go', '.rs', '.swift', '.kt', '.ts', '.jsx', '.tsx', '.vue', '.svelte'],
            
            # Fonts
            'Fonts': ['.ttf', '.otf', '.woff', '.woff2', '.eot', '.svg'],
            
            # 3D Models
            '3D_Models': ['.obj', '.fbx', '.dae', '.3ds', '.blend', '.max', '.ma', '.mb', '.stl', '.ply', '.wrl'],
            
            # CAD Files
            'CAD': ['.dwg', '.dxf', '.step', '.stp', '.iges', '.igs', '.sldprt', '.sldasm', '.prt', '.asm'],
            
            # Database
            'Database': ['.db', '.sqlite', '.sql', '.mdb', '.accdb', '.odb', '.fdb', '.db3'],
            
            # Other
            'Other': []
        }
        
        # Create category folders if they don't exist
        self.create_category_folders()
        
        logger.info(f"File Organizer initialized for Desktop: {self.desktop_path}")
    
    def create_category_folders(self):
        """Create category folders on the Desktop if they don't exist."""
        for category in self.file_categories.keys():
            category_path = self.desktop_path / category
            if not category_path.exists():
                category_path.mkdir(exist_ok=True)
                logger.info(f"Created folder: {category}")
    
    def get_file_category(self, file_extension):
        """Determine the category for a given file extension."""
        file_extension = file_extension.lower()
        
        for category, extensions in self.file_categories.items():
            if file_extension in extensions:
                return category
        
        return 'Other'
    
    def organize_file(self, file_path):
        """Move a file to its appropriate category folder."""
        try:
            file_path = Path(file_path)
            
            # Skip if it's a directory or if the file doesn't exist
            if not file_path.is_file() or not file_path.exists():
                return
            
            # Skip if the file is already in a category folder
            if file_path.parent.name in self.file_categories.keys():
                return
            
            # Get file extension and determine category
            file_extension = file_path.suffix
            category = self.get_file_category(file_extension)
            
            # Create destination path
            destination_folder = self.desktop_path / category
            destination_path = destination_folder / file_path.name
            
            # Handle duplicate filenames
            counter = 1
            original_name = file_path.stem
            original_extension = file_path.suffix
            
            while destination_path.exists():
                new_name = f"{original_name}_{counter}{original_extension}"
                destination_path = destination_folder / new_name
                counter += 1
            
            # Move the file
            shutil.move(str(file_path), str(destination_path))
            
            logger.info(f"Moved: {file_path.name} → {category}/")
            
        except Exception as e:
            logger.error(f"Error organizing file {file_path}: {str(e)}")

class DesktopEventHandler(FileSystemEventHandler):
    """Event handler for file system events on the Desktop."""
    
    def __init__(self, organizer):
        """Initialize the event handler with a file organizer instance."""
        self.organizer = organizer
        self.pending_files = {}  # Track files that are being created
    
    def on_created(self, event):
        """Handle file creation events."""
        if event.is_directory:
            return
        
        file_path = Path(event.src_path)
        
        # Check if file exists and is not empty
        if file_path.exists() and file_path.stat().st_size > 0:
            self.organizer.organize_file(file_path)
        else:
            logger.warning(f"File {file_path.name} appears to be empty or was deleted")

def main():
    """Main function to run the file organizer."""
    try:
        # Initialize the file organizer
        organizer = FileOrganizer()
        
        # Create event handler
        event_handler = DesktopEventHandler(organizer)
        
        # Create observer
        observer = Observer()
        observer.schedule(event_handler, str(organizer.desktop_path), recursive=False)
        
        logger.info("Starting file organizer...")
        logger.info(f"Monitoring Desktop folder: {organizer.desktop_path}")
        logger.info("Press Ctrl+C to stop")
        
        # Start monitoring
        observer.start()
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            logger.info("Stopping file organizer...")
            observer.stop()
        
        observer.join()
        
    except Exception as e:
        logger.error(f"Error in main: {str(e)}")

if __name__ == "__main__":
    main() 