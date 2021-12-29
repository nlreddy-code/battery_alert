import psutil
import time
import tkinter
st=int(input("Enter start time"))
et=int(input("Enter end time"))
battery = psutil.sensors_battery()
def alert_window():
	t=tkinter.Tk()
	t.mainloop()
import _thread as thread
while(1):
	if battery.percent<st and battery.power_plugged==False:
		print("\a")
		thread.start_new_thread(alert_window,())
		while(battery.power_plugged==False):
			print("\a")
			time.sleep(2)
			battery = psutil.sensors_battery()
	elif battery.percent>et and battery.power_plugged==True:
		print("\a")
		thread.start_new_thread(alert_window,())
		while(battery.power_plugged==True):
			print("\a")
			time.sleep(2)
			battery = psutil.sensors_battery()
	else:
		time.sleep(30)
	battery = psutil.sensors_battery()

