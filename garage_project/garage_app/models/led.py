from django.db import models

import RPi.GPIO as GPIO

class Led(models.Model):
	pin = models.IntegerField()

	def init_gpio(self):
		if self.pin != 0:
			GPIO.setup(self.pin, GPIO.OUT, initial=GPIO.HIGH)

	def on(self):
		# TODO Check if it's Common Anode (current) or Common Cathode
		GPIO.output(self.pin, False)

	def off(self):
		# TODO Check if it's Common Anode (current) or Common Cathode
		GPIO.output(self.pin, True)

	def __unicode__(self):
		return str(self.pin)
	
	class Meta:
		app_label = 'garage_app'
