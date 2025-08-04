import os
import platform
import shutil
# gives python permission to move files into quarantine
import subprocess

from .config import QUARANTINE_DIR
#Library of file considered dangerous
from .logger import log_alerts
#To print the log alert

from .notifier import ualerts


#makes a standard quarantine files to
# store malicious files
def suspiciousfile(path):
    _, ext = os.path.splitext(path)
    # splits the directory up to two readable parts: The toot name and extension
    ext = ext.lower()
    # makes the extension lowercase

    current_os = platform.system()
    # Checks the current OS its on

    if current_os == "Windows":
            suspicious_extensions = ['.exe', '.dll']
    elif current_os == "Darwin":
            suspicious_extensions = ['.dmg', '.pkg', '.sh']
    elif current_os == "Linux":
            suspicious_extensions = ['.sh', '.bin', '.run']
    else:
        suspicious_extensions = ['.sh', '.bin']

    return ext in suspicious_extensions
# flags these potential extensions for double check and
# puts any of these files into quarantine

# extract and expands extension and verifys if suspicious

def quarantine(filepath):
    try:
        if not os.path.exists(QUARANTINE_DIR):
            os.makedirs(QUARANTINE_DIR)
# 1. check if quarantined file exists and makes one if it doesnt
        filename = os.path.basename(filepath)
# 2. takes filename from path
        quarantined_path = os.path.join(QUARANTINE_DIR, filename)
# 3. builds a new quarantine location for the filename
        try:
            shutil.move(filepath, quarantined_path)
# 4. moves suspicious file there
        except (PermissionError, FileNotFoundError) as e:
            print(f"Failed To Quarantined File {e}")
            return None

        return quarantined_path
# 5. gives new location of file
    except Exception as outer_e:
        print(f"Unexpected Error During Quarantine Setup: {outer_e}")
        return None

def filescan(filepath):
    if suspiciousfile(filepath):
# If There Is a filepath added to suspicious file ---> Make user alert
        quarantined_path = quarantine(filepath)
        message = (
        f"📬Kavval has held '{os.path.basename(filepath)}' for secondary review.\n"
        "It has been moved to secure location.\n"
        "Please individually verify before proceeding"
        )
        ualerts(message)
    else:
# Else approve filepath to stay in downloads
        ualerts(
            f"'{os.path.basename(filepath)}' has been verified.\n"
            "This file may be used as intended."
        )

# The Decision - maker: decided to either quarantine it or not
# if yes:
# immediately quarantine and warn user
# if no
# "file is safe" message

if __name__ == "__main__":
    log_alerts("File Found and quarantined for secondary review")