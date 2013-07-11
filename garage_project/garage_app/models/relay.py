from django.db import models
import RPi.GPIO as GPIO

class Relay(models.Model):
	relayPin = models.IntegerField()

	def toggle_state(self):
		self.state = not self.state
		GPIO.output(self.relayPin, self.state)

	def init(self):
		GPIO.setmode(GPIO.BOARD)
		self.state = True
		GPIO.setup(self.relayPin, GPIO.OUT, initial=GPIO.HIGH)

	def __unicode__(self):
		return str(relayPin)

	class Meta:
		app_label = 'garage_app'
