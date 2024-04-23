from django.shortcuts import render
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

from rest_framework import permissions, viewsets

from .models import Club
from .forms import ClubForm
from .serializers import ClubSerializer

# class ClubCreateView(FormView):
# 	form_class = ClubForm
# 	success_url = reverse_lazy('home')
# 	template_name = 'clubs/club_create.html'

# class ClubDetailView(TemplateView):
# 	template_name = 'clubs/club_detail.html'

# class ClubEditView(TemplateView):
# 	template_name = 'clubs/club_edit.html'

# class ClubDeleteView(TemplateView):
# 	template_name = 'clubs/club_delete.html'

# class ClubSearchView(TemplateView):
# 	template_name = 'clubs/club_search.html'
# ''' Need to filter by joined/not joined/both, creator'''

class ClubViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clubs to be viewed or edited.
    """
    queryset = Club.objects.all().order_by('club_name')
    serializer_class = ClubSerializer
    # Being logged in currently doesn't = isAuthenticated, so this is commented out temporarily to test other things
    # Also need to customize permissions - viewing allowed when logged out but not creating/editing
    permission_classes = [permissions.IsAuthenticated]

    # def create(self, validated_data):
    #   admins = [self.request.user]
    #   return models.YourModel.objects.create(email=email, **validated_data)
