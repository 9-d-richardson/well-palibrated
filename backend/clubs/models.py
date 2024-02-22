from django.db import models
from django.contrib.auth import get_user_model

from accounts.models import CustomUser

from django_project import shared_constants as s_c

# class ClubConstants:
# 	INVITE_ONLY = 'IO'
# 	REQUEST_TO_JOIN = 'RTJ'
# 	PUBLIC = 'P'
# 	PERMISSION_TYPES = {
# 		INVITE_ONLY: 'Invite only',
# 		REQUEST_TO_JOIN: 'Request to join',
# 		PUBLIC: 'Public',
# 	}

class Club(models.Model):
	INVITE_ONLY = 'IO'
	REQUEST_TO_JOIN = 'RTJ'
	PUBLIC = 'P'
	PERMISSION_TYPES = {
		INVITE_ONLY: 'Invite only',
		REQUEST_TO_JOIN: 'Request to join',
		PUBLIC: 'Public',
	}

	admins = models.ManyToManyField(
		CustomUser, 
		related_name='admins',
	)
	members = models.ManyToManyField(
		CustomUser, 
		related_name='members',
	)
	club_name = models.CharField(
		max_length=s_c.CharFieldMaxLength,
	)
	club_description = models.TextField(
		max_length=s_c.TextFieldMaxLength,
		null=True,
		blank=True,
	)
	permission_type = models.CharField(
		choices=PERMISSION_TYPES,
		max_length=s_c.CharFieldMaxLength,
	)

	def __str__(self):
		return self.club_name