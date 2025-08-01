from core.downlwatch import scanner
from core.logger import log_alerts
from core.notifier import ualerts


def main():
    log_alerts("LOG ALERT - Kavval In Progress")

    ualerts("👀 Kavval In Operation and Now Monitering Downloads Folder")

    scanner()

if __name__ == "__main__":
    main()
