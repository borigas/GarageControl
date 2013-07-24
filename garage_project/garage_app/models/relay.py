from django.db import models
import RPi.GPIO as GPIO

class Relay(models.Model):
	relayPin = models.IntegerField()

	initialized = False

	def open(self):
		GPIO.output(self.relayPin, True)

	def close(self):
		GPIO.output(self.relayPin, False)

	def init_gpio(self):
		if self.relayPin != None and self.relayPin != 0 and not self.initialized:
			GPIO.setup(self.relayPin, GPIO.OUT, initial=GPIO.HIGH)
			self.initialized = True

	def __unicode__(self):
		return 'Pin: ' + str(self.relayPin)

	class Meta:
		app_label = 'garage_app'
