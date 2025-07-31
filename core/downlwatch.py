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

def main():
    downloads_path = os.path.expanduser("~/Downloads")
    print(f"Kavval starting watch on: {downloads_path}")

    event_handler = FileScanner()

    observer = Observer()

    observer.schedule(event_handler, path=downloads_path, recursive=True)

    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()