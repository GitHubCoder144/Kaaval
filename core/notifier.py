import os

import platform
import subprocess

from .logger import log_alerts
# To print the log alert


def ualerts(message):
    current_os = platform.system()

    if current_os == "Darwin":
        try:
            escaped_message = message.replace('"', '\\"')
            subprocess.run([
                 "osascript", "-e",
                f'display notification "{escaped_message}" with title "📣 Kavval Alert"'
            ])
        except Exception as e:
            print("[macOS Alert Error]", e)

    elif current_os == "Windows":
        try:
            import win10toast
            toaster = win10toast.ToastNotifier()
            toaster.show_toast("📣 Kavval Alert", message, duration=5)
        except Exception as e:
            print("[Windows Alert Error]", e)

    elif current_os == "Linux":
        try:
            subprocess.run([
                "notify-send", "📣 Kavval Alert", message
            ])
        except Exception as e:
            print("[Linux Alert Error]", e)

    else:
        print("[Unknown OS]" + message)

    log_alerts(message)

#makes an alert to system causing a pop up alert
