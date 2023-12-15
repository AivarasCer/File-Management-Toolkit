# Automated Backup Script
# Program that automatically backs up specified directories to a local drive after each addition/edit

from pathlib import Path
from watchdog.events import FileSystemEventHandler


class BackupHandler(FileSystemEventHandler):

    def __init__(self, source_dir, backup_dir):
        self.source_dir = Path(source_dir)
        self.backup_dir = Path(backup_dir)

    def on_modified(self, event):
        pass

    def on_created(self, event):
        pass

    def backup_file(self, path):
        pass


def start_backup(monitor_dir, backup_dir):
    pass

if __name__ == "__main__":
    monitor = input('Enter the path to the directory to monitor: ')
    backup = input('Enter the path to the backup directory: ')
    start_backup(monitor, backup)
