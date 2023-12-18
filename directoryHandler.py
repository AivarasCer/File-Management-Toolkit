# Directory Handler
# It is a program that automatically moves and renames files from a specified source dir to a destination dir.

import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class DirHandler(FileSystemEventHandler):

    def __init__(self, folder_to_track, destination_dir):
        self.dir_to_track = Path(folder_to_track)
        self.destination_dir = Path(destination_dir)
        self.i = 1

    def on_modified(self, event):
        for filename in self.dir_to_track.iterdir():
            if filename.is_file():
                new_filename = f'{filename.name}_{self.i}'
                new_destination = self.destination_dir / new_filename

                filename.rename(new_destination)
                print(f"Moved and renamed {filename} to {new_destination}")
                self.i += 1


def start_handling(folder_to_track, destination_dir):
    event_handler = DirHandler(folder_to_track, destination_dir)
    observer = Observer()
    observer.schedule(event_handler, folder_to_track, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    dir_to_track = input('Enter the path to the directory to track: ')
    destination = input('Enter the path to the destination directory: ')
    start_handling(dir_to_track, destination)
