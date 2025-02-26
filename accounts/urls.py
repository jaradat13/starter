from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
        path('', views.home, name='home'),
        path('about/', views.about, name='about'),
        path('contact/', views.contact, name='contact'),
        path('privacy/', views.privacy, name='privacy'),
        path('terms/', views.terms, name='terms'),
        # Authentication
        path('profile/', views.profile, name='profile'),
        path('profile/edit/', views.profile_edit, name='edit_profile'),

        path('signup/', views.signup, name='signup'),
        path('login/', views.CustomLoginView.as_view(), name='login'),
        path('logout/', views.CustomLogoutView.as_view(), name='logout'),
        path('password-reset/',auth_views.PasswordResetView.as_view(
                template_name='accounts/password_reset.html'
            ),
            name='password_reset'),
        path('password-reset/done/',
            auth_views.PasswordResetDoneView.as_view(
                template_name='accounts/password_reset_done.html'
            ),
            name='password_reset_done'),
        path('password-reset-confirm/<uidb64>/<token>/',
            auth_views.PasswordResetConfirmView.as_view(
                template_name='accounts/password_reset_confirm.html'
            ),
            name='password_reset_confirm'),
        path('password-reset-complete/',
            auth_views.PasswordResetCompleteView.as_view(
                template_name='accounts/password_reset_complete.html'
            ),
            name='password_reset_complete'),


    ]