from django.db import models
import time
import RPi.GPIO as GPIO

class Sensor(models.Model):
	CallbackChannels = list()

	triggerPin = models.IntegerField()
	echoPin = models.IntegerField()

	distance = 0
	risingTime = 0

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

				# 3.28 ft/m
				self.distance = (timeDiff * 10000 * 3.28 / 2) / 29.1
			
	
	def init_gpio(self):
		# Call from post_init signal
		# Check if this pk has been initialized. If not, initialize gpio
		if self.triggerPin != 0 and self.echoPin != 0:
			GPIO.setup(self.triggerPin, GPIO.OUT, initial=GPIO.LOW)
			GPIO.setup(self.echoPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
			if not self.echoPin in Sensor.CallbackChannels:
				GPIO.add_event_detect(self.echoPin, GPIO.BOTH, callback=self.edge_callback)
				Sensor.CallbackChannels.append(self.echoPin)

	def __unicode__(self):
		return 'Trig: ' + str(self.triggerPin) + ' Echo: ' + str(self.echoPin)
	
	class Meta:
		app_label = 'garage_app'
