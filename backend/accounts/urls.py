# from django.contrib.auth.views import LogoutView

from . import views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.CustomUserViewSet)

urlpatterns = [
	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	# path('signup/', views.SignUpView.as_view(), name='signup'),
	# path('login/', views.CustomLoginView.as_view(), name='login'),
	# path("logout/", LogoutView.as_view(), name="logout"),
	# path('edit-profile/', views.EditProfile.as_view(), name='edit_profile'),
	# path('delete/', views.DeleteProfile.as_view(), name='delete_profile'),
	# path('account/<str:url>/', views.ViewProfile.as_view(), name='view_profile'),

	# path("password_change/", views.CustomPasswordChangeView.as_view(), 
	# 	name="password_change"),
    # path("password_change/done/", views.CustomPasswordChangeDoneView.as_view(),
	# 	name="password_change_done"),
    # path("password_reset/", views.CustomPasswordResetView.as_view(), 
	# 	name="password_reset"),
    # path("password_reset/done/", views.CustomPasswordResetDoneView.as_view(),
	# 	name="password_reset_done"),
	# path("reset/<uidb64>/<token>/", views.CustomPasswordResetConfirmView.as_view(),
	# 	name="password_reset_confirm"),
    # path("reset/done/", views.CustomPasswordResetCompleteView.as_view(),
	# 	name="password_reset_complete"),
]

urlpatterns += router.urls
