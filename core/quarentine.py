import os
import shutil

from .config import QUARANTINE_DIR, DOWNLOADS_DIR
# Imported so we can move files to the
# Quarantine Directory and then the Downloads Directory

def quarantine_file(filepath):
    try:
        filename = os.path.basename(filepath)
# The Filename
        dest_path = os.path.join(QUARANTINE_DIR, filename)
# The file goes towards the destination if flag which is quarantine
        shutil.move(filepath, dest_path)
# Moving the file using shutil from downloads to the quarantine folder
        print(f"File {filename} Forced to Quarantine")
# Prints out that this file goes to quarantine
        return dest_path
# goes to destination


    except Exception as e:
# If non of these instructions work print this message
        print(f"The Quarantine failed - Please Try Again: {e}")
        return None


def files_quarantined():
# if the quarantine directory has files make a file path for
# Quarantined path
    try:
        files = [
            f for f in os.listdir(QUARANTINE_DIR)
            if os.path.isfile(os.path.join(QUARANTINE_DIR, f))
        ]
# if not print no files
        if not files:
            print("Quarantine directory Has No Files")
            return []
# shows the Quarantined files in the directory

        print("Quarantine Files:", QUARANTINE_DIR)
        for i, file in enumerate(files, start=1):
            print(f"{i}, {file}")
        return files

# print error message if nothing works
    except FileNotFoundError:
        print("Quarantine Directory Nonexistant!!")
        return []

def restoration(filename):
# src_path - the original or starting path is Quarantine path
#  dest_path - the final location is downloads folder
    src_path = os.path.join(QUARANTINE_DIR, filename)
    dest_path = os.path.join(DOWNLOADS_DIR, filename)

    try:
# If unable to work print error message
        if not os.path.exists(src_path):
            print(f"Quarantine File '{filename}' Not Found!!")
            return False

# If works split the filename and extension and restore to downloads
        if os.path.exists(dest_path):
            base, ext = os.path.splitext(filename)
            dest_path = os.path.join(DOWNLOADS_DIR, f"{base} _restored{ext}")

# Use shutil to move the file from the original Quarantine path to downloads
# print success message when done
        shutil.move(src_path, dest_path)
        print(f"Quarantine File '{filename}' Moved to Downloads Folder.")
        return True

# error message
    except Exception as e:
        print(f"Restoring File Error {e}")
        return False

def delete(filename):
# full_path - this is the full quarantined path including the filename
    full_path = os.path.join(QUARANTINE_DIR, str(filename))
    try:
#  if the file path in the quarantine does not exist
        if not os.path.exists(full_path):
            print(f"Quarantine File '{filename}' Not Found!!")
            return False

# if the filepath is found or exists then remove the file (Duh)
# then print out the success message
        if os.path.exists(full_path):
            os.remove(full_path)
            print(f"Quarantine File '{filename}' Deleted.")
            return True

# error message if this does not work
    except Exception as e:
            print(f"Delete File Error: {e}")
            return False

    return False
