from django import forms

from django_project import shared_constants as s_c

from .models import OnlineEvent, IRLEvent

class EventForm(forms.ModelForm):
	event_name = forms.CharField(
		max_length=s_c.CharFieldMaxLength,
		label="Event name*:"
	)
	event_description = forms.CharField(
		max_length=s_c.TextFieldMaxLength,
		widget=forms.Textarea(attrs={'rows': s_c.TextAreaRows,}), 
		required=False, 
		label="Event description:",
	)
	permission_type = forms.CharField()
	start_time = forms.DateTimeField()
	end_time = forms.DateTimeField()
	link = forms.URLField()
	repetition_type = forms.CharField()
	repetition_length = forms.IntegerField()

class IRLEventForm(EventForm):
	class Meta:
		model = IRLEvent
		fields = ['event_name', 'event_description', 'permission_type', 
			'start_time', 'end_time', 'link', 'location', 'location_link', 
			'repetition_type', 'repetition_length']

	location = forms.CharField()
	location_link = forms.URLField()

class OnlineEventForm(EventForm):
	class Meta:
		model = OnlineEvent
		fields = ['event_name', 'event_description', 
			'permission_type', 'start_time', 'end_time', 'link', 
			'repetition_type', 'repetition_length']