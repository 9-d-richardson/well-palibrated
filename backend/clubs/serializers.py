from rest_framework import serializers
from .models import Club

class ClubSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Club
        fields = ['club_name', 'permission_type', 'club_description', 'admins', 
			'members']