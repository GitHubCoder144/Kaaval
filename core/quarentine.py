import os
import shutil

from .config import QUARANTINE_DIR, DOWNLOADS_DIR


def quarantine_file(filepath):
    try:
        filename = os.path.basename(filepath)
        dest_path = os.path.join(QUARANTINE_DIR, filename)
        shutil.move(filepath, dest_path)
        print(f"File {filename} Forced to Quarantine")
        return dest_path


    except Exception as e:
        print(f"The Quarantine failed - Please Try Again: {e}")
        return None


def files_quarantined():
    try:
        files = [
            f for f in os.listdir(QUARANTINE_DIR)
            if os.path.isfile(os.path.join(QUARANTINE_DIR, f))
        ]

        if not files:
            print("Quarantine directory Has No Files")
            return []

        print("Quarantine Files:", QUARANTINE_DIR)
        for i, file in enumerate(files, start=1):
            print(f"{i}, {file}")
        return files

    except FileNotFoundError:
        print("Quarantine Directory Nonexistant!!")
        return []

def restoration(filename):
    src_path = os.path.join(QUARANTINE_DIR, filename)
    dest_path = os.path.join(DOWNLOADS_DIR, filename)

    try:
        if not os.path.exists(src_path):
            print(f"Quarantine File '{filename}' Not Found!!")
            return False

        if os.path.exists(dest_path):
            base, ext = os.path.splitext(filename)
            dest_path = os.path.join(DOWNLOADS_DIR, f"{base} _restored{ext}")

        shutil.move(src_path, dest_path)
        print(f"Quarantine File '{filename}' Moved to Downloads Folder.")
        return True

    except Exception as e:
        print(f"Restoring File Error {e}")
        return False

def delete(filename):
    full_path = os.path.join(QUARANTINE_DIR, str(filename))
    try:
        if not os.path.exists(full_path):
            print(f"Quarantine File '{filename}' Not Found!!")
            return False

        if os.path.exists(full_path):
            os.remove(full_path)
            print(f"Quarantine File '{filename}' Deleted.")
            return True

    except Exception as e:
            print(f"Delete File Error: {e}")
            return False

    return False
