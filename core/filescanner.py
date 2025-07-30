import os
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
    return ext.lower() in SUSPICIOUS_EXTENSIONS

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
        title="📣📣 Kaaval Alert",
        message=message,
        timeout=5
    )

    log_alert(message)

#makes an alert to system causing a pop up alert

def filescan(filepath):
    if suspiciousfile(filepath):
        quarantined_path = quarantine(filepath)
        ualerts(f"SUSPICIOUS FILE DETECTED AND QUARANTINED: {quarantined_path}")
    else:
        ualerts(f"File {filepath} is clean and safe to use.")

# The Decision - maker: decided to either quarantine it or not
# if yes:
# immediately quarantine and warn user
# if no
# "file is safe" message

if __name__ == "__main__":
    ualerts("Suspicious File Found and quarantined")