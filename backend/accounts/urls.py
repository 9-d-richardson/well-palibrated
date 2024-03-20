# # from django.contrib.auth.views import LogoutView

from . import views
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.DefaultRouter()
router.register(r'users', views.CustomUserViewSet)

# urlpatterns = [
# 	path('', include(router.urls)),
# 	path('', include('rest_framework.urls', namespace='rest_framework_accounts')),
# 	# path('signup/', views.SignUpView.as_view(), name='signup'),
# 	# path('login/', views.CustomLoginView.as_view(), name='login'),
# 	# path("logout/", LogoutView.as_view(), name="logout"),
# 	# path('edit-profile/', views.EditProfile.as_view(), name='edit_profile'),
# 	# path('delete/', views.DeleteProfile.as_view(), name='delete_profile'),
# 	# path('account/<str:url>/', views.ViewProfile.as_view(), name='view_profile'),

# 	# path("password_change/", views.CustomPasswordChangeView.as_view(),
# 	# 	name="password_change"),
#     # path("password_change/done/", views.CustomPasswordChangeDoneView.as_view(),
# 	# 	name="password_change_done"),
#     # path("password_reset/", views.CustomPasswordResetView.as_view(),
# 	# 	name="password_reset"),
#     # path("password_reset/done/", views.CustomPasswordResetDoneView.as_view(),
# 	# 	name="password_reset_done"),
# 	# path("reset/<uidb64>/<token>/", views.CustomPasswordResetConfirmView.as_view(),
# 	# 	name="password_reset_confirm"),
#     # path("reset/done/", views.CustomPasswordResetCompleteView.as_view(),
# 	# 	name="password_reset_complete"),
# ]

# urlpatterns += router.urls

# from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, UserDetailsView
# from django.urls import path
# from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('', include(router.urls)),
    path("register/", RegisterView.as_view(), name="rest_register"),
    # path("login/", LoginView.as_view(), name="rest_login"),
    path("login/", views.CustomTokenObtainPairView.as_view(), name="rest_login"),
    path("logout/", views.LogoutView.as_view(), name="rest_logout"),
    path("user/", UserDetailsView.as_view(), name="rest_user_details"),
    path("token/verify/", views.CustomTokenVerifyView.as_view(), name="token_verify"),
    # path("token/refresh/", get_refresh_view().as_view(), name="token_refresh"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
