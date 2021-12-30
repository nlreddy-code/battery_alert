import psutil
import time
import tkinter

low=int(input("Enter lowest battery percentage : "))
high=int(input("Enter highest battery percentage : "))

battery = psutil.sensors_battery()

def alert_window(battery_value):
	t=tkinter.Tk()
	t.geometry("200x200")

	if battery_value==0:
		alert_label=tkinter.Label(t,text="Low battery").place(x=70,y=90)
	else:
		alert_label=tkinter.Label(t,text="Charged").place(x=70,y=90)
	t.mainloop()

import _thread as thread

while(1):
	if battery.percent<low and battery.power_plugged==False:
		print("\a")
		thread.start_new_thread(alert_window,(0,))
		while(battery.power_plugged==False):
			print("\a")
			time.sleep(2)
			battery = psutil.sensors_battery()

	elif battery.percent>high and battery.power_plugged==True:
		print("\a")
		thread.start_new_thread(alert_window,(1,))
		while(battery.power_plugged==True):
			print("\a")
			time.sleep(2)
			battery = psutil.sensors_battery()

	else:
		time.sleep(30)
	battery = psutil.sensors_battery()

