import psutil
import tkinter
from threading import Thread
import time

def alert_window(battery_value):
    t = tkinter.Tk()
    t.geometry("200x200")
    if battery_value == 0:
        alert_label = tkinter.Label(t, text="Low battery").place(x=70, y=90)
    else:
        alert_label = tkinter.Label(t, text="Charged").place(x=70, y=90)
    t.mainloop()

def battery_monitor(low, high):
    while True:
        battery = psutil.sensors_battery()
        if battery.percent < low and not battery.power_plugged:
            print("\a")
            Thread(target=alert_window, args=(0,)).start()
            while not battery.power_plugged:
                print("\a")
                time.sleep(2)
                battery = psutil.sensors_battery()
        elif battery.percent > high and battery.power_plugged:
            print("\a")
            Thread(target=alert_window, args=(1,)).start()
            while battery.power_plugged:
                print("\a")
                time.sleep(2)
                battery = psutil.sensors_battery()
        else:
            time.sleep(30)

if __name__ == "__main__":
    low = int(input("Enter lowest battery percentage : "))
    high = int(input("Enter highest battery percentage : "))
    battery_monitor(low, high)
