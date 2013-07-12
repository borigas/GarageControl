from django.contrib import admin
from garage_app.models import Door, Status, Led, RgbLed, Sensor, Relay


class DoorAdmin(admin.ModelAdmin):
	list_display = ['name']
	actions = ['update_statuses']

	def update_statuses(self, request, queryset):
		for door in queryset:
			door.update_status()

admin.site.register(Door, DoorAdmin)

admin.site.register(Status)
admin.site.register(Led)
admin.site.register(RgbLed)
admin.site.register(Sensor)
admin.site.register(Relay)
