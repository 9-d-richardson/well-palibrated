from django.contrib import admin

from .models import (Club)

class ClubAdmin(admin.ModelAdmin):
	fields = ['club_name', 'permission_type', 'club_description', 'admins', 
			'members']
	list_display = ('club_name', 'permission_type')

admin.site.register(Club, ClubAdmin)
