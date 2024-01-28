from django import forms

from django_project import shared_constants as s_c

from .models import Club


class ClubForm(forms.ModelForm):
	class Meta:
		model = Club
		fields = ['managers']