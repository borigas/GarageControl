#!/usr/bin/python

import RPi.GPIO as GPIO
import time

class Proximity:
	outputPin = 12
	inputPin = 16
	bluePin = 11
	greenPin = 13
	redPin = 15
	relay1Pin = 3
	relay2Pin = 5

	def rising_callback(self, channel):
		if GPIO.input(channel):
			self.risingTime = time.time()
			#print('Rising edge')
		elif  self.risingTime != 0:
			timeDiff = time.time() - self.risingTime
			self.risingTime = 0
			#print('Falling edge')
			# 1/10000 seconds * 3.28 ft/m
			dist = (timeDiff * 10000 * 3.28 / 2) / 29.1
			print(dist)

			GPIO.output(self.redPin, True)
			GPIO.output(self.greenPin, True)
			GPIO.output(self.bluePin, True)

			if(dist > 20):
				GPIO.output(self.bluePin, False)
			if(dist > 4):
				GPIO.output(self.greenPin, False)
			else:
				GPIO.output(self.redPin, False)

	def setup(self):
		GPIO.setmode(GPIO.BOARD)

		GPIO.setup(self.bluePin, GPIO.OUT, initial=GPIO.HIGH)
		GPIO.setup(self.greenPin, GPIO.OUT, initial=GPIO.HIGH)
		GPIO.setup(self.redPin, GPIO.OUT)

		GPIO.setup(self.relay1Pin, GPIO.OUT, initial=GPIO.HIGH)
		GPIO.setup(self.relay2Pin, GPIO.OUT, initial=GPIO.HIGH)
	
		GPIO.setup(self.outputPin, GPIO.OUT, initial=GPIO.HIGH)
		GPIO.setup(self.inputPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

		self.risingTime = 0


		GPIO.add_event_detect(self.inputPin, GPIO.BOTH, callback=self.rising_callback)

	def run(self):
		GPIO.output(self.outputPin, False)

		while(True):
#		for x in range(0, 100):
			print('--Starting--')
			triggered = True
			GPIO.output(self.outputPin, True)
			time.sleep(0.01)
			GPIO.output(self.outputPin, False)
			time.sleep(1)
			print('-------------------')

		GPIO.cleanup()


prox = Proximity()
prox.setup()
prox.run()
