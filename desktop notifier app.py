pip install plyer
import time
from plyer import notification

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name='Desktop Notifier',
        timeout=10  # Notification will disappear after 10 seconds
    )

if __name__ == "__main__":
    while True:
        title = "Reminder"
        message = "This is your desktop notification!"
        
        send_notification(title, message)
        
        # Wait for 60 seconds before sending the next notification
        time.sleep(60)