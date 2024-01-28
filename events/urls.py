from django.urls import path

from .views import NewEventView, NewOnlineEventView, NewIRLEventView

urlpatterns = [
	path('new-online/', NewOnlineEventView.as_view(), name='event_new_online'),
	path('new-irl/', NewIRLEventView.as_view(), name='event_new_irl'),
	path('new/', NewEventView.as_view(), name='event_new'),

	# path('edit/<str:url>/', EventEditView.as_view(), name='event_edit'),
	# path('delete/<str:url>/', EventDeleteView.as_view(), name='event_delete'),
	# path('<str:url>/', EventView.as_view(), name='event_view'),
]