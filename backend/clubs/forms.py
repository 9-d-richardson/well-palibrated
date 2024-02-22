from django import forms

from django_project import shared_constants as s_c

from .models import Club#, ClubConstants


class ClubForm(forms.ModelForm):
	class Meta:
		model = Club
		fields = ['club_name', 'permission_type', 'club_description', 'admins', 
			'members']

	club_name = forms.CharField(
		required=True,
		label="Club name*:",
		max_length=s_c.CharFieldMaxLength,
	)

	club_description = forms.CharField(
		max_length=s_c.TextFieldMaxLength,
		widget=forms.Textarea(attrs={'rows': s_c.TextAreaRows,}), 
		required=False, 
		label="Description:",
		error_messages={
			'max_length': s_c.max_length_error,
		}
	)

	permission_type = forms.ChoiceField(
		choices = Club.PERMISSION_TYPES,
		label='Permission type*:'
	)