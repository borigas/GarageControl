from django.db import models
from led import Led

class RgbLed(models.Model):
	redLed = models.ForeignKey(Led, related_name='redLed')
	greenLed = models.ForeignKey(Led, related_name='greenLed')
	blueLed = models.ForeignKey(Led, related_name='blueLed')

	def init(self):
		self.redLed.init()
		self.greenLed.init()
		self.blueLed.init()

	def all_on(self):
		self.redLed.on()
		self.greenLed.on()
		self.blueLed.on()

	def all_off(self):
		self.redLed.off()
		self.greenLed.off()
		self.blueLed.off()

	def __unicode__(self):
		return 'R:' + str(self.redLed.pin) + ' G:' + str(self.greenLed.pin) + ' B:' + str(self.blueLed.pin)

	class Meta:
		app_label = 'garage_app'
