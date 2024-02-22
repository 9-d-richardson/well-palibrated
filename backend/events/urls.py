from . import views 

from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'irl-event', views.IRLEventViewSet)
router.register(r'online-event', views.OnlineEventViewSet)

urlpatterns = [
	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	# path('new-online/', views.EventCreateOnlineView.as_view(), name='event_new_online'),
	# path('new-irl/', views.EventCreateIRLView.as_view(), name='event_new_irl'),
	# path('new/', views.EventCreateView.as_view(), name='event_new'),
	# path('calendar/', views.EventCalendarView.as_view(), name='calendar'),
	# path('search/', views.EventSearchView.as_view(), name='event_search'),

	# path('edit/<str:url>/', views.EventEditView.as_view(), name='event_edit'),
	# path('delete/<str:url>/', views.EventDeleteView.as_view(), name='event_delete'),
	# path('<str:url>/', views.EventDetailView.as_view(), name='event_detail'),
]

urlpatterns += router.urls