from django.shortcuts import render
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

from .models import Club
from .forms import ClubForm

class NewClubView(FormView):
	form_class = ClubForm
	success_url = reverse_lazy('home')
	template_name = 'clubs/new_club.html'

class ClubView(TemplateView):
	template_name = 'clubs/club.html'