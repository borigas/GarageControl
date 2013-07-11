from django.db import models
import time
import RPi.GPIO as GPIO

class Sensor(models.Model):
	triggerPin = models.IntegerField()
	echoPin = models.IntegerField()

	def find_distance(self):
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
		if channel == echoPin:
			if GPIO.input(echoPin):
				# Is rising edge
				self.risingTime = time.time()
			elif self.risingTime != 0:
				# Is falling edge
				timeDiff = time.time() - self.risingTime
				self.risingTime = 0

				# 3.28 ft/m
				self.distance = (timeDiff * 10000 * 3.28 / 2) / 29.1
			
	
	def init(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.triggerPin, GPIO.OUT, initial=GPIO.LOW)
		GPIO.setup(self.echoPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		GPIO.add_event_detect(self.echoPin, GPIO.BOTH, callback=self.edge_callback)	

	def __unicode__(self):
		return str(self.triggerPin) + '-' + str(echoPin)
	
	class Meta:
		app_label = 'garage_app'
