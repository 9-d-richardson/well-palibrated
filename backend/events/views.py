from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from django.urls import reverse_lazy

from rest_framework import permissions, viewsets


from .models import Event
from .serializers import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('event_name')
    serializer_class = EventSerializer
    # permission_classes = [permissions.IsAuthenticated]

# class OnlineEventViewSet(viewsets.ModelViewSet):
#     queryset = OnlineEvent.objects.all().order_by('event_name')
#     serializer_class = OnlineEventSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class EventCreateView(TemplateView):
# 	'''
# 	Page for deciding between creating an IRL or online event
# 	'''
# 	template_name = 'events/event_create.html'

# #Should we have separate pages for editing online/IRL events?
# class EventEditView(TemplateView):
# 	template_name = 'events/event_edit.html'

# class EventCreateIRLView(FormView):
# 	form_class = IRLEventForm
# 	success_url = reverse_lazy('home')
# 	template_name = 'events/event_create_irl.html'

# class EventCreateOnlineView(FormView):
# 	form_class = OnlineEventForm
# 	success_url = reverse_lazy('home')
# 	template_name = 'events/event_create_online.html'

# # class EventDetailView(UserPassesTestMixin, TemplateView):

# class EventSearchView(TemplateView):
# 	template_name = 'events/event_search.html'

# class EventCalendarView(TemplateView):
	# template_name = 'events/calendar.html'
