import os
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# Watchdog libraries imported for cross-platform monitering

from .filescanner import filescan
# imported from kavval filescanner.py
# imported from kavval quarantine.py
#Possibly not needed due to this script specifically for watchdog

class FileScanner(FileSystemEventHandler):
# custom class called filescanner using the input from watchdogs FileSystemEventHandler
    def on_created (self, event):
# this function is when a new file is made in the downloads
        if event.is_directory:
# if a new directory is made
            return

        filepath = event.src_path
# the filepath is the full filepath of the new file
        print(f"Dectected New file: {filepath}")

        filescan(filepath)
# run the filescan function on the function

def scanner():
    downloads_path = os.path.expanduser("~/Downloads")
# Kavval will watch downloads_path is the full expanded path to downloads
    print(f"Kavval starting watch on: {downloads_path}")

    event_handler = FileScanner()
# the event_handler is the file scanner function in kavval

    observer = Observer()
# file system monitering

    observer.schedule(event_handler, path=downloads_path, recursive=True)
# set kavval to watch the downloads folder 24/7

    observer.start()
# start the observer or kavval

    try:
# the observer will run through a loop so 24/7 always happens
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
# Unless ctrl + c in terminal is pressed and stops kavval
        observer.stop()
    observer.join()

if __name__ == "__main__":
    scanner()