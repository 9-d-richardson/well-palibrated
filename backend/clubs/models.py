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
	INVITE_ONLY = 'invite_only'
	REQUEST_TO_JOIN = 'request_to_join'
	PUBLIC = 'public'
	PERMISSION_TYPES = {
		INVITE_ONLY: 'Invite only',
		REQUEST_TO_JOIN: 'Request to join',
		PUBLIC: 'Public',
	}

	admins = models.ManyToManyField(
		CustomUser,
		related_name='admins',
		blank=True,
	)
	members = models.ManyToManyField(
		CustomUser,
		related_name='members',
    blank=True,
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

  #This method sets the default admin to whoever the user currently is, for new clubs
	def save(self, *args, **kwargs):
		if self.id is None:
			print('x')
		super(Club, self).save(*args, **kwargs)
