import os

# suspicious files
SUSPICIOUS_EXTENSIONS = ['.exe', '.dll']

# location of quarantined folder
QUARANTINE_DIR = os.path.expanduser('~/.kavvalquarantine')