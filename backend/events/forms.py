from django import forms

from django_project import shared_constants as s_c
from .models import Event


class EventForm(forms.ModelForm):
	fields = ['creator', 'event_name', 'parent_club', 'event_description', 'permission_type',
		'start_date', 'start_time', 'end_date', 'end_time', 'link', 'repetition_type',
		'repetition_length', 'is_irl', 'location', 'location_link']
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
	permission_type = forms.ChoiceField(
		choices = Event.PERMISSION_TYPES,
		label='Permission type*:'
	)
	start_date = forms.DateField()
	start_time = forms.TimeField(
		required=False,
	)
	end_date = forms.DateField()
	end_time = forms.TimeField(
		required=False,
	)
	link = forms.URLField(
		required=False,
	)
	repetition_type = forms.ChoiceField(
		choices = Event.REPETITION_TYPES,
		label='Repetition type*:'
	)
	#repetition_length should be required only if repetition_type isn't none
	repetition_length = forms.IntegerField(
		required=False,
	)

	is_irl = forms.BooleanField()

	#These are for IRL events
	location = forms.CharField(
		required=False,
	)
	location_link = forms.URLField(
		required=False,
	)


# class IRLEventForm(EventForm):
# 	class Meta:
# 		model = IRLEvent
# 		fields = EventForm.fields + ['location', 'location_link']

# 	location = forms.CharField(
# 		required=False,
# 	)
# 	location_link = forms.URLField(
# 		required=False,
# 	)

# class OnlineEventForm(EventForm):
# 	class Meta:
# 		model = OnlineEvent
# 		fields = EventForm.fields
