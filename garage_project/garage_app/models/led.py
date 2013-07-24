from django.db import models

import RPi.GPIO as GPIO

class Led(models.Model):
	pin = models.IntegerField()

	initialized = False

	def init_gpio(self):
		if self.pin != None and self.pin != 0 and not self.initialized:
			GPIO.setup(self.pin, GPIO.OUT, initial=GPIO.HIGH)
			self.initialized = True

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
