from django.db import models
from django.contrib.auth import get_user_model

from accounts.models import CustomUser
from clubs.models import Club
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
	parent_club = models.ForeignKey(
		Club,
		on_delete=models.CASCADE,
		related_name='parent_club',
		null=True,
		blank=True,
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
	start_date = models.DateField()
	start_time = models.TimeField(
		null=True,
		blank=True,
	)
	end_date = models.DateField(
		null=True,
		blank=True,
	)
	end_time = models.TimeField(
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
	is_irl = models.BooleanField()

	#These are only for IRL Events
	location = models.TextField(
		null=True,
		blank=True,
	)
	#Should be to like Google Maps. Only if it's an IRL event
	location_link = models.URLField(
		null=True,
		blank=True,
	)

	''' This should be a link to like a webcast or something, as opposed to a
	link which describes the event in greater detail '''
	event_link  = models.URLField(
		null=True,
		blank=True,
	)

	def __str__(self):
		return self.event_name


# class IRLEvent(EventBase):
# 	location = models.TextField(
# 		null=True,
# 		blank=True,
# 	)
# 	#Should be to like Google Maps. Only if it's an IRL event
# 	location_link = models.URLField(
# 		null=True,
# 		blank=True,
# 	)

# class OnlineEvent(EventBase):
# 	''' This should be a link to like a webcast or something, as opposed to a
# 	link which describes the event in greater detail '''
# 	event_link  = models.URLField(
# 		null=True,
# 		blank=True,
# 	)

# class Event(models.Model):
# 	irl_event = models.OneToOneField(
# 		IRLEvent,
# 		on_delete=models.CASCADE,
# 	)
# 	online_event = models.OneToOneField(
# 		OnlineEvent,
# 		on_delete=models.CASCADE,
# 	)
