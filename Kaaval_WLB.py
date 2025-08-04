from core.downlwatch import scanner
# for scanner running
from core.logger import log_alerts
# for the alert log to save alerts
from core.notifier import ualerts
# Notify user Kaaval in progress

def main():
    log_alerts("LOG ALERT - Kavval In Progress")

    ualerts("👀 Kavval In Operation and Now Monitering Downloads Folder")

    scanner()

if __name__ == "__main__":
    main()
