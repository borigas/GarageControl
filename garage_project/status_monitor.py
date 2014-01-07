# This script is automatically started at boot by /etc/rc.local

import os
import sys
import logging

logging.basicConfig(filename='/home/pi/logs/status_monitor_python.log',level=logging.ERROR)

path = os.path.dirname(os.path.abspath(__file__))
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'garage_project.settings'

from garage_app.models.door import Door
while True:
	try:
		for door in Door.objects.all():
			door.monitor_status()
	except Exception as e:
		print e
		logging.Exception("Error monitoring status: %s", e)

print("Done")
