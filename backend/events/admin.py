from django.contrib import admin

from .models import Event
from .forms import EventForm

class EventAdmin(admin.ModelAdmin):
	list_display = ('event_name', 'permission_type')
	fields = EventForm.fields

# class IRLEventAdmin(EventAdmin):
# 	fields = EventAdmin.fields + ['location', 'location_link']

# class OnlineEventAdmin(EventAdmin):
# 	pass

admin.site.register(Event, EventAdmin)
