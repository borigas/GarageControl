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

		status.save()

		return dist

	def _toggle_door(self, expectedIsDoorUp):
		from status import Status
		self.update_status()
		status = Status.objects.filter(door = self).latest()
		if not status.isError and expectedIsDoorUp == status.isDoorUp:
			self.relay.close()
			sleep(0.010)
			self.relay.open()
			# Log change
	
	def open(self):
		self._toggle_door(False)
	
	def close(self):
		self._toggle_door(True)
		

	def __unicode__(self):
		return self.name

	class Meta:
		app_label = 'garage_app'
