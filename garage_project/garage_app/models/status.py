from django.db import models
from door import Door

class Status(models.Model):
	class Meta:
		verbose_name_plural = 'Statuses'
		app_label = 'garage_app'

	door = models.ForeignKey(Door)
	distance = models.DecimalField(max_digits=10, decimal_places=4)
	isDoorUp = models.BooleanField(default=True)
	isCarPresent = models.BooleanField(default=False)
	statusDate = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return str(self.distance)