from django.db import models
from django.db.models.signals import post_init
import time
import RPi.GPIO as GPIO

class Sensor(models.Model):
	CallbackChannels = list()

	triggerPin = models.IntegerField()
	echoPin = models.IntegerField()

	distance = 0
	risingTime = 0

	initialized = False

	def find_distance(self):
		self.risingTime = 0
		self.distance = 0
		GPIO.output(self.triggerPin, True)
		time.sleep(0.01)
		GPIO.output(self.triggerPin, False)
		i = 0
		while(self.distance == 0 and i < 100):
			time.sleep(0.01)
			i += 1
		return self.distance

	def edge_callback(self, channel):
		if channel == self.echoPin:
			if GPIO.input(self.echoPin):
				# Is rising edge
				self.risingTime = time.time()
			elif self.risingTime != 0:
				# Is falling edge
				timeDiff = time.time() - self.risingTime
				self.risingTime = 0

				# time * 340 m/s * 3.28 ft/m / 2
				self.distance = timeDiff * 340 * 3.28 / 2
			
	
	def init_gpio(self):
		if self.triggerPin != None and self.triggerPin != 0 and self.echoPin != None and self.echoPin != 0 and not self.initialized:
			GPIO.setup(self.triggerPin, GPIO.OUT, initial=GPIO.LOW)
			GPIO.setup(self.echoPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
			if self.echoPin in Sensor.CallbackChannels:
				# Already setup echo pin. Remove it 1st
				GPIO.remove_event_detect(self.echoPin)
				Sensor.CallbackChannels.remove(self.echoPin)

			# Setup echo pin edge callback
			GPIO.add_event_detect(self.echoPin, GPIO.BOTH, callback=self.edge_callback)
			Sensor.CallbackChannels.append(self.echoPin)

			self.initialized = True

	def __unicode__(self):
		return 'Trig: ' + str(self.triggerPin) + ' Echo: ' + str(self.echoPin)
	
	class Meta:
		app_label = 'garage_app'
