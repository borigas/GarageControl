from django.db import models

# Create your models here.

class Door(models.Model):
	name = models.CharField(max_length=200)
	relayPin = models.IntegerField()
	sensorTriggerPin = models.IntegerField()
	sensorEchoPin = models.IntegerField()
	greenPin = models.IntegerField()
	redPin = models.IntegerField()
	bluePin = models.IntegerField()

	def update_status(self):
		status = Status(door = self, distance = 1.5, isDoorUp = False, isCarPresent = True)
		status.save()
		return status
	
	def __unicode__(self):
		return self.name

class Status(models.Model):
	class Meta:
		verbose_name_plural = 'Statuses'

	door = models.ForeignKey(Door)
	distance = models.DecimalField(max_digits=10, decimal_places=4)
	isDoorUp = models.BooleanField(default=True)
	isCarPresent = models.BooleanField(default=False)
	statusDate = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return str(self.distance)
