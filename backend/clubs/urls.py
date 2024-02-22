from django.urls import include, path

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'clubs', views.ClubViewSet)

urlpatterns = [
	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	# path('create/', views.ClubCreateView.as_view(), name='club_create'),
	# path('search/', views.ClubSearchView.as_view(), name='club_search'),
	# path('edit/<str:url>/', views.ClubEditView.as_view(), name='club_edit'),
	# path('delete/<str:url>/', views.ClubDeleteView.as_view(), name='club_delete'),
	# path('<str:url>/', views.ClubDetailView.as_view(), name='club_detail'),
]

urlpatterns += router.urls