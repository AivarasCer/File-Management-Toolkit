# Automated Backup Script
# Program that automatically backs up specified directories to a local drive after each addition/edit

import shutil
import time
from pathlib import Path
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class BackupHandler(FileSystemEventHandler):

    def __init__(self, source_dir, backup_dir):
        self.source_dir = Path(source_dir)
        self.backup_dir = Path(backup_dir)

    def on_modified(self, event):
        if not event.is_directory:
            self.backup_file(event.src_path)

    def on_created(self, event):
        if not event.is_directory:
            self.backup_file(event.src_path)

    def backup_file(self, path):
        relative_path = Path(path).relative_to(self.source_dir)
        destination = self.backup_dir / relative_path
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, destination)
        print(f'Backp created for: {path}')


def start_backup(monitor_dir, backup_dir):
    event_handler = BackupHandler(monitor_dir, backup_dir)
    observer = Observer()
    observer.schedule(event_handler, monitor_dir, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    monitor = input('Enter the path to the directory to monitor: ')
    backup = input('Enter the path to the backup directory: ')
    start_backup(monitor, backup)
