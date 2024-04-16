from rest_framework import serializers
from .models import Event

# event_fields = fields = ['event_name', 'creator', 'parent_club', 'event_description', 'permission_type',
#         'start_date', 'start_time', 'end_date', 'end_time', 'link', 'repetition_type',
#         'repetition_length']

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['event_name', 'creator', 'parent_club', 'event_description', 'permission_type',
        'start_date', 'start_time', 'end_date', 'end_time', 'link', 'repetition_type',
        'repetition_length', 'location', 'location_link']

# class IRLEventSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = IRLEvent
#         fields = event_fields + ['location', 'location_link']


# class OnlineEventSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = OnlineEvent
#         fields = event_fields
