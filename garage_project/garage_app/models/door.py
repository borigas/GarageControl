from django.db import models
from relay import Relay
from sensor import Sensor
from rgb_led import RgbLed
from time import sleep

class Door(models.Model):
	name = models.CharField(max_length=200)
	relay = models.ForeignKey(Relay)
	sensor = models.ForeignKey(Sensor)
	rgbLed = models.ForeignKey(RgbLed)

	def update_status(self):
		status = self.find_status()
		status.save()
		return status

	def monitor_status(self):
		from status import Status

		saveNew = False
		status = self.find_status()
		recentStatuses = Status.objects.filter(door=self).order_by('-statusDate')[:2]
		# If the last 2 match, we don't need to save a new one. We can just update the time on the newest one
		saveNew = recentStatuses.count() < 2 or not status.areEquivalentStates(recentStatuses[0]) or not status.areEquivalentStates(recentStatuses[1])
		if saveNew:
			print "Saving new status"
			status.save()
			return status
		else:
			print "Updating old status"
			recentStatuses[0].statusDate = status.statusDate
			recentStatuses[0].distance = status.distance
			recentStatuses[0].save()
			return recentStatuses[0]

	def find_status(self):
		from status import Status
		dist = self.sensor.find_distance()

		self.rgbLed.all_off()

		status = Status(door = self, distance = dist)

		if dist > 20 or dist == 0:
			# Bad reading
			self.rgbLed.blueLed.on()
			status.isError = True
		else:
			if dist > 3:
				status.isDoorUp = False
				self.rgbLed.greenLed.on()
			else:
				status.isDoorUp = True
				self.rgbLed.redLed.on()

			if dist > 6:
				status.isCarPresent = False
			else:
				status.isCarPresent = True

		return status

	def _toggle_door(self, expectedIsDoorUp):
		from status import Status
		status = self.update_status()
		if not status.isError and expectedIsDoorUp == status.isDoorUp:
			self.relay.close()
			sleep(0.010)
			self.relay.open()
			# Log change
			print("Door toggled to Open=" + str(not expectedIsDoorUp))
			return True
		else:
			# Log that we didn't change
			print("Door not toggled to Open=" + str(not expectedIsDoorUp))
			return False
	
	def open(self):
		return self._toggle_door(False)
	
	def close(self):
		return self._toggle_door(True)
		

	def __unicode__(self):
		return self.name

	class Meta:
		app_label = 'garage_app'
