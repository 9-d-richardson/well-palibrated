from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from django.urls import reverse_lazy

from .models import IRLEvent, OnlineEvent
from .forms import IRLEventForm, OnlineEventForm

class NewEventView(TemplateView):
	'''
	Page for deciding between creating an IRL or online event
	'''
	template_name = 'events/new.html'

class NewIRLEventView(FormView):
	form_class = IRLEventForm
	success_url = reverse_lazy('home')
	template_name = 'events/new_irl_event.html'

class NewOnlineEventView(FormView):
	form_class = OnlineEventForm
	success_url = reverse_lazy('home')
	template_name = 'events/new_online_event.html'
