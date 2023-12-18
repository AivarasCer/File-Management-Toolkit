# Directory Handler
#

import json
import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class DirHandler(FileSystemEventHandler):

    def __init__(self, folder_to_track, destination_dir):
        self.dir_to_track = Path(folder_to_track)
        self.destination_dir = Path(destination_dir)

    def on_modified(self, event):
        for filename in self.dir_to_track.iterdir():
            if filename.is_file():
                new_destination = self.destination_dir / filename.name
                filename.rename(new_destination)

