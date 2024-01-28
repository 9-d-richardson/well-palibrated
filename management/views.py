from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

class HomeView(TemplateView):
	'''
	Home page/FAQ page
	'''
	template_name = 'management/home.html'