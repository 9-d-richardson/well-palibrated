from django.db import models
from django.contrib.auth import get_user_model

from accounts.models import CustomUser

from django_project import shared_constants as s_c

class Event(models.Model):
	NOT_REPEATED = 'NR'
	DAILY = 'D'
	WEEKLY = 'W'
	MONTHLY = 'M'
	REPETITION_TYPES = {
		NOT_REPEATED: 'Not repeated',
		DAILY: 'Daily',
		WEEKLY: 'Weekly',
		MONTHLY: 'Monthly',
	}

	INVITE_ONLY = 'IO'
	CLUB_ONLY = 'CO'
	PUBLIC = 'P'
	PERMISSION_TYPES = {
		INVITE_ONLY: "Invitation only",
		CLUB_ONLY: 'Club members only',
		PUBLIC: 'Public'
	}

	creator = models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE,
		related_name='creator'
	)
	event_name = models.CharField(
		max_length=s_c.CharFieldMaxLength,
	)
	event_description = models.TextField(
		max_length=s_c.CharFieldMaxLength,
		null=True,
		blank=True,
	)
	permission_type = models.CharField(
		choices=PERMISSION_TYPES,
		max_length=s_c.CharFieldMaxLength,
	)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField(
		null=True,
		blank=True,
	)
	link = models.URLField(
		null=True,
		blank=True,
	)
	repetition_type = models.CharField(
		choices=REPETITION_TYPES,
		max_length=s_c.CharFieldMaxLength,
	)
	repetition_length = models.IntegerField(
		null=True,
		blank=True,
	)


class IRLEvent(Event):
	location = models.TextField(
		null=True,
		blank=True,
	)
	#Should be to like Google Maps. Only if it's an IRL event
	location_link = models.URLField(
		null=True,
		blank=True,
	)

class OnlineEvent(Event):
	''' This should be a link to like a webcast or something, as opposed to a 
	link which describes the event in greater detail '''
	event_link  = models.URLField(
		null=True,
		blank=True,
	)