import RPi.GPIO as GPIO
from django.db import models
from django.db.models.signals import post_init

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

def gpio_post_init(sender, instance, **kwargs):
#	print sender
	print "Instance: " + str(instance)
	init_gpio_method = getattr(instance, "init_gpio", None)
	if callable(init_gpio_method):
		print "Method found"
		instance.init_gpio()
#	if sender is Sensor:
#		print(instance)
#		instance.init_gpio()
post_init.connect(gpio_post_init)
