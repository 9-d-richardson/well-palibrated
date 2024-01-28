from django.db import models
from django.contrib.auth import get_user_model

from accounts.models import CustomUser

from django_project import shared_constants as s_c

class Club(models.Model):
	managers = models.ManyToManyField(
		CustomUser, 
		related_name='managers'
	)