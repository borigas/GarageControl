import RPi.GPIO as GPIO
from time import sleep

outputPin = 12
inputPin = 16

GPIO.setmode(GPIO.BOARD)

GPIO.setup(outputPin, GPIO.OUT, initial=GPIO.HIGH)
sleep(2)
state = True

for x in range(0, 10):
	GPIO.output(outputPin, state)
	state = not state
	sleep(0.5)

GPIO.cleanup()
