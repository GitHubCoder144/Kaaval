import os
import platform
import shutil
# gives python permission to move files into quarantine

from plyer import notification
#shows cross-platform alerts
from config import SUSPICIOUS_EXTENSIONS, QUARANTINE_DIR
#Library of file considered dangerous
from logger import log_alert
#To print the log alert


#makes a standard quarantine files to
# store malicious files
def suspiciousfile(path):
    _, ext = os.path.splitext(path)
    ext = ext.lower()

    current_os = platform.system()

    if current_os == "Windows":
            suspicious_extensions = ['.exe', '.dll']
    elif current_os == "Darwin":
            suspicious_extensions = ['.dmg', '.pkg', '.sh']
    elif current_os == "Linux":
            suspicious_extensions = ['.sh', '.bin', '.run']
    else:
        suspicious_extensions = ['.sh', '.bin']

    return ext in suspicious_extensions

# extract and expands extension and verifys if suspicious

def quarantine(filepath):
    if not os.path.exists(QUARANTINE_DIR):
        os.makedirs(QUARANTINE_DIR)
    filename = os.path.basename(filepath)
    quarantined_path = os.path.join(QUARANTINE_DIR, filename)
    shutil.move(filepath, quarantined_path)
    return quarantined_path

# 1. check if quarantined file exists and makes one if it doesnt
# 2. takes filename from path
# 3. builds a new quarantine location for the filename
# 4. moves suspicious file there
# 5. gives new location of file

def ualerts(message):
    notification.notify(
        title="📣📣 Alert",
        message=message,
        timeout=5
    )

    log_alert(message)

#makes an alert to system causing a pop up alert

def filescan(filepath):
    if suspiciousfile(filepath):
        quarantined_path = quarantine(filepath)
        message = (
        f"📬Kavval has held '{os.path.basename(filepath)}' for secondary review.\n"
        "It has been moved to secure location.\n"
        "Please individually verify before proceeding"
        )
        ualerts(message)
    else:
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
    ualerts("File Found and quarantined for secondary review")