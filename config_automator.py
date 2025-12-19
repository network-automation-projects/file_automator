import os
import shutil
from pathlib import Path
from datetime import datetime
import logging

# Set up logging
logging.basicConfig(filename='logs/automation.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def backup_file(file_path: Path) -> Path:
    """Back up a file with timestamp."""
    backup_dir = Path('backups')
    backup_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = backup_dir / f"{file_path.stem}_{timestamp}{file_path.suffix}"
    try:
        shutil.copy(file_path, backup_path)
        logging.info(f"Backed up {file_path} to {backup_path}")
        return backup_path
    except Exception as e:
        logging.error(f"Failed to back up {file_path}: {e}")
        raise

def scan_and_backup(directory: str) -> list:
    """Scan directory for YAML/JSON files and back them up."""
    dir_path = Path(directory)
    if not dir_path.exists():
        raise ValueError(f"Directory {directory} does not exist")
    
    files_backed_up = []
    for file_path in dir_path.glob('*.[yaml|json]*'):  # Matches .yaml, .yml, .json
        try:
            backup_path = backup_file(file_path)
            files_backed_up.append(backup_path)
        except Exception as e:
            logging.error(f"Error processing {file_path}: {e}")
    return files_backed_up

# Test run (comment out later)
if __name__ == "__main__":
    scan_and_backup('configs')