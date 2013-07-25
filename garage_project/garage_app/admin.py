from django.contrib import admin
from garage_app.models.door import Door
from garage_app.models.status import Status
from garage_app.models.led import Led
from garage_app.models.rgb_led import RgbLed
from garage_app.models.sensor import Sensor
from garage_app.models.relay import Relay


class DoorAdmin(admin.ModelAdmin):
	list_display = ['name']
	actions = ['update_statuses', 'open', 'close']

	def update_statuses(self, request, queryset):
		for door in queryset:
			door.update_status()

	def open(self, request, queryset):
		for door in queryset:
			door.open()

	def close(self, request, queryset):
		for door in queryset:
			door.close()

admin.site.register(Door, DoorAdmin)

admin.site.register(Status)
admin.site.register(Led)
admin.site.register(RgbLed)
admin.site.register(Sensor)
admin.site.register(Relay)
