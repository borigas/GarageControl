from django.db import models
import RPi.GPIO as GPIO

class Relay(models.Model):
	relayPin = models.IntegerField()

	def open(self):
		GPIO.output(self.relayPin, True)

	def close(self):
		GPIO.output(self.relayPin, False)

	def init_gpio(self):
		if self.relayPin != 0:
			GPIO.setup(self.relayPin, GPIO.OUT, initial=GPIO.HIGH)

	def __unicode__(self):
		return 'Pin: ' + str(self.relayPin)

	class Meta:
		app_label = 'garage_app'
