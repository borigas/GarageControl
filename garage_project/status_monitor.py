# This script is automatically started at boot by /etc/rc.local

import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'garage_project.settings'

from garage_app.models.door import Door
while True:
	for door in Door.objects.all():
		door.monitor_status()

print("Done")
