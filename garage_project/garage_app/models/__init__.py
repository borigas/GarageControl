import RPi.GPIO as GPIO
from django.db import models
from django.db.models.signals import post_init

from door import Door
from led import Led
from rgb_led import RgbLed
from sensor import Sensor
from relay import Relay
from status import Status

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

def gpio_post_init(sender, instance, **kwargs):
	init_gpio_method = getattr(instance, "init_gpio", None)
	if callable(init_gpio_method):
		instance.init_gpio()

post_init.connect(gpio_post_init)
