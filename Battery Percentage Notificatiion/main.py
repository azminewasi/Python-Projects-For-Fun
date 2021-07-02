import psutil
from plyer import notification
import time 

battery=psutil.sensors_battery()

while(1):
    percent=battery.percent
    notification.notify(title="Battery Percentage", message=str(percent)+"% Charge Remaining\nPowered by XC",timeout=100)
    time.sleep(60*60)
    continue