import psutil
import time
battery = psutil.sensors_battery()
while(1):
	if battery.percent<30 and battery.power_plugged==False:
		print("\a")
		while(battery.power_plugged==False):
			print("\a")
			time.sleep(2)
			battery = psutil.sensors_battery()
	elif battery.percent>80 and battery.power_plugged==True:
		print("\a")
		while(battery.power_plugged==True):
			print("\a")
			time.sleep(2)
			battery = psutil.sensors_battery()
	else:
		time.sleep(30)
	battery = psutil.sensors_battery()

