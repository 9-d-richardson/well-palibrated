from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.db import IntegrityError, transaction

from django.views.generic import CreateView, DetailView, ListView, FormView
from django.views.generic.base import TemplateView
from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import permissions, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .forms import (CustomUserCreationForm, CustomUserChangeForm,
	CustomUserDeleteForm)
from .models import CustomUser
from django.conf import settings

from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    # TokenRefreshView,
	TokenObtainPairView,
    TokenVerifyView
)

from .serializers import CustomUserSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clubs to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('username')
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

class SignUpView(CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'accounts/signup.html'

	def form_invalid(self, form):
		return super().form_invalid(form)

	def form_valid(self, form):
		messages.success(self.request, 'Account created!')
		return super().form_valid(form)


class EditProfile(LoginRequiredMixin, FormView):
	template_name = 'accounts/edit_profile.html'
	form_class = CustomUserChangeForm
	success_url = 'home'

	def get_initial(self):
		initial = super().get_initial()
		user = self.request.user
		initial['username'] = user.username
		initial['email'] = user.email
		initial['user_description'] = user.user_description
		initial['avatar'] = user.avatar
		return initial

	def form_invalid(self, form):
		'''This adds changed_input to the context, so the template knows to
		warn of unsaved changes'''
		return self.render_to_response(self.get_context_data(
			form=form,
			changed_input=True
		))

	def post(self, request, *args, **kwargs):
		user = self.request.user
		form = CustomUserChangeForm(request.POST, request.FILES, instance=user)
		print(form)
		if form.is_bound and form.is_valid():
			with transaction.atomic():
				form.save()
				messages.success(request, 'Changes saved!')
				return HttpResponseRedirect(reverse_lazy('view_user',
					kwargs={"username":user.username}))
		messages.error(request, 'There were problems updating your profile.')
		return self.form_invalid(form)


class DeleteProfile(LoginRequiredMixin, TemplateView):
	template_name = 'accounts/delete_profile.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['form'] = CustomUserDeleteForm()
		return context

	def post(self, request, **kwargs):
		user = self.request.user
		form = CustomUserDeleteForm(request.POST, user=user)
		if form.is_bound and form.is_valid():
			with transaction.atomic():
				user.is_active = False
				user.save()
				messages.success(request, 'Account deleted.')
				return HttpResponseRedirect(reverse_lazy('home'))
		messages.error(request, 'There were problems deleting your account.')
		return render(self.request, self.template_name, {'form': form})

class ViewProfile(TemplateView):
	template_name = 'accounts/view_profile.html'

class CustomTokenVerifyView(TokenVerifyView):

	def post(self, request, *args, **kwargs):
		access_token = request.COOKIES.get('access')
		if access_token:
			request.data['token'] = access_token

		return super().post(request, *args, **kwargs)


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            access_token = response.data.get('access')
            refresh_token = response.data.get('refresh')

            response.set_cookie(
                'access',
                access_token,
                max_age=settings.AUTH_COOKIE_MAX_AGE,
                path=settings.AUTH_COOKIE_PATH,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE
            )
            response.set_cookie(
                'refresh',
                refresh_token,
                max_age=settings.AUTH_COOKIE_MAX_AGE,
                path=settings.AUTH_COOKIE_PATH,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE
            )

        return response

class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        response = Response(status=status.HTTP_204_NO_CONTENT)
        response.delete_cookie('access')
        response.delete_cookie('refresh')
        response.delete_cookie('csrftoken')
        response.delete_cookie('sessionid')

        return response

#Custom views which just set a different template location
class CustomLoginView(views.LoginView):
	template_name = 'accounts/login.html'
class CustomPasswordChangeView(views.PasswordChangeView):
	template_name = 'accounts/password_change_form.html'
class CustomPasswordChangeDoneView(views.PasswordChangeDoneView):
	template_name = 'accounts/password_change_done.html'
class CustomPasswordResetView(views.PasswordResetView):
	template_name = 'accounts/password_reset_form.html'
class CustomPasswordResetDoneView(views.PasswordResetDoneView):
	template_name = 'accounts/password_reset_done.html'
class CustomPasswordResetConfirmView(views.PasswordResetConfirmView):
	template_name = 'accounts/password_reset_confirm.html'
class CustomPasswordResetCompleteView(views.PasswordResetCompleteView):
	template_name = 'accounts/password_reset_complete.html'
