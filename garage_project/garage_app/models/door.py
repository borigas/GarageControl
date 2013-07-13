from django.db import models
from relay import Relay
from sensor import Sensor
from rgb_led import RgbLed

class Door(models.Model):
	name = models.CharField(max_length=200)
	relay = models.ForeignKey(Relay)
	sensor = models.ForeignKey(Sensor)
	rgbLed = models.ForeignKey(RgbLed)

	def update_status(self):
		dist = self.sensor.find_distance()

		self.rgbLed.all_off()

		if dist > 20:
			# Bad reading
			self.rgbLed.blueLed.on()
		else:
			status = Status(door = self, distance = dist)
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

	def __unicode__(self):
		return self.name

	class Meta:
		app_label = 'garage_app'


from status import Status
