from rest_framework import serializers
from .models import Club

class ClubSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Club
        fields = ['club_name', 'permission_type', 'club_description', 'admins',
			'members']

    # Will contain the logic to add the current user as the admin of the club being created
    # def create(self, validated_data):
    #     club = Club.objects.create(**validated_data)
    #     club.admins.add(request.user)
    #     return club
