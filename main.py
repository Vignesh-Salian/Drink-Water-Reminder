import time
from plyer import notification 

while True:
    notification.notify(title="Water Remainder", message="You need to drink some water!",)
    time.sleep(60*60)