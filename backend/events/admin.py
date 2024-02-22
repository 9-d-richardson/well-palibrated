from django.contrib import admin

from .models import (IRLEvent, OnlineEvent)

class EventAdmin(admin.ModelAdmin):
	list_display = ('event_name', 'permission_type')
	fields = ['creator', 'event_name', 'event_description', 'permission_type', 
		'start_time', 'end_time', 'link', 'repetition_type', 
		'repetition_length']

class IRLEventAdmin(EventAdmin):
	fields = EventAdmin.fields + ['location', 'location_link']

class OnlineEventAdmin(EventAdmin):
	pass

admin.site.register(IRLEvent, IRLEventAdmin)
admin.site.register(OnlineEvent, OnlineEventAdmin)

