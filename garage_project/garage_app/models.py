from django.db import models

# Create your models here.

class Door(models.Model):
	name = models.CharField(max_length=200)

class Status(models.Model):
	door = models.ForeignKey(Door)
	distance = models.DecimalField(max_digits=10, decimal_places=4)
	isDoorUp = models.BooleanField(default=True)
	isCarPresent = models.BooleanField(default=False)
	statusDate = models.DateField(auto_now_add=True)

