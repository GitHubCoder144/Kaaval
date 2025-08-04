import platform
import subprocess

from .logger import log_alerts
# To print the log alert


def ualerts(message):
    current_os = platform.system()
# Checks the current Operating System
    if current_os == "Darwin":
# calls apon osascript (macOS Script Editor Notification)
# to display notification
        try:
            escaped_message = message.replace('"', '\\"')
            subprocess.run([
                 "osascript", "-e",
                f'display notification "{escaped_message}" with title "📣 Kavval Alert"'
            ])
        except Exception as e:
            print("[macOS Alert Error]", e)

    elif current_os == "Windows":
# Originally this alert would use win10toast
# However I realized that win10toast didnt get
# Updates since 2017 💀💀💀
# Will Update with plyer in future update
        try:
            import win10toast
            toaster = win10toast.ToastNotifier()
            toaster.show_toast("📣 Kavval Alert", message, duration=5)
        except Exception as e:
            print("[Windows Alert Error]", e)

    elif current_os == "Linux":
# Calls apon the "notify send" subprocess to push alert
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
