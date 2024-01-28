from django.urls import path

from .views import NewClubView, ClubView

urlpatterns = [
	path('new/', NewClubView.as_view(), name='club_new'),
	# path('edit/<str:url>/', ClubEditView.as_view(), name='club_edit'),
	# path('delete/<str:url>/', ClubDeleteView.as_view(), name='club_delete'),
	# path('<str:url>/', ClubView.as_view(), name='club_view'),
]