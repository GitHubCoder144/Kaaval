import os
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from filescanner import filescan
from quarentine import files_quarantined

class FileScanner(FileSystemEventHandler):
    def on_created (self, event):
        if event.is_directory:
            return

        filepath = event.src_path
        print(f"Dectected New file: {filepath}")

        filescan(filepath)

