from plyer import notification
import time

while True:
    notification.notify(
        title='Drink Water Reminder',
        message='Time to drink water! \n its been 1 hour since your last drink.',
        timeout=5)
    time.sleep(60*60)