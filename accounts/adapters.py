from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth import get_user_model
from allauth.core.exceptions import ImmediateHttpResponse
from django.http import HttpResponseRedirect

User = get_user_model()


class CustomAccountAdapter(DefaultAccountAdapter):
    """This adapter skips the additional signup form and automatically logs in users."""

    def is_open_for_signup(self, request):
        """Prevent new signups and only allow existing users."""
        return True  # Set to True if you want to allow new users via Google


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    """Automatically links social accounts to existing users without requiring extra input."""

    def pre_social_login(self, request, sociallogin):
        """If an account exists with the same email, link it automatically."""

        if sociallogin.is_existing:
            return

        email = sociallogin.account.extra_data.get("email")
        if not email:
            return

        try:
            user = User.objects.get(email=email)
            sociallogin.connect(request, user)
            raise ImmediateHttpResponse(HttpResponseRedirect("/"))
        except User.DoesNotExist:
            pass
