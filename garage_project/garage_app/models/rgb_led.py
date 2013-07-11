from django.db import models
from led import Led

class RgbLed(models.Model):
	redLed = models.ForeignKey(Led, related_name='redLed')
	greenLed = models.ForeignKey(Led, related_name='greenLed')
	blueLed = models.ForeignKey(Led, related_name='blueLed')

	def init(self):
		redLed.init()
		greenLed.init()
		blueLed.init()

	def all_on(self):
		redLed.on()
		greenLed.on()
		blueLed.on()

	def all_off(self):
		redLed.off()
		greenLed.off()
		blueLed.off()

	def __unicode__(self):
		return 'R:' + str(redLed.pin) + ' G:' + str(greenLed.pin) + ' B:' + str(blueLed.pin)

	class Meta:
		app_label = 'garage_app'
