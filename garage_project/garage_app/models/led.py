from django.db import models

import RPi.GPIO as GPIO

class Led(models.Model):
	pin = models.IntegerField()

	def init(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.pin, GPIO.OUT, initial=GPIO.HIGH)

	def on(self):
		GPIO.output(self.pin, False)

	def off(self):
		GPIO.output(self.pin, False)

	def __unicode__(self):
		return str(pin)
	
	class Meta:
		app_label = 'garage_app'
