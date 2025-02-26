# views.py
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm
import logging
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileForm, UserFormSet
from django.contrib.auth import get_user_model
from .models import Profile, CustomUser

User = get_user_model()
logger = logging.getLogger(__name__)

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.get_or_create(user=user)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, 'Account created successfully!')
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/signup.html', {'form': form})


def profile_edit(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        user_formset = UserFormSet(request.POST, queryset=CustomUser.objects.filter(id=request.user.id))  # ✅ Fix here
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if all([
            user_formset.is_valid(), profile_form.is_valid(),

        ]):
            user_formset.save()  # No commit=False since we use queryset, not instance
            profile_form.save()
            # Save experience, certification, education
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')
        else:
            print("Form Errors:", user_formset.errors, profile_form.errors)

    else:
        user_formset = UserFormSet(queryset=CustomUser.objects.filter(id=request.user.id))  # ✅ Fix here
        profile_form = ProfileForm(instance=profile)

    return render(request, 'accounts/profile_edit.html', {
        'user_formset': user_formset,
        'profile_form': profile_form,
    })


class CustomLoginView(SuccessMessageMixin, LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    success_message = "Welcome back! You've been successfully logged in."

    def get_success_url(self):
        return reverse_lazy('home')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')


@login_required
def profile(request):
    user = request.user


    return render(request, 'accounts/profile.html', {
        'user': user,

    })




def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')




def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                # Get form data
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']

                # Construct email message
                email_message = f"""
                New contact form submission from {name}

                From: {email}
                Subject: {subject}

                Message:
                {message}
                """

                # Send email
                send_mail(
                    subject=f"Contact Form: {subject}",
                    message=email_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=False,
                )

                # Log successful submission
                logger.info(f"Contact form submitted successfully by {email}")

                messages.success(request, 'Thank you for your message. We will get back to you soon!')
                return redirect('contact')

            except Exception as e:
                # Log the specific error
                logger.error(f"Contact form error: {str(e)}")

                # Check for specific error types and provide more helpful messages
                if 'SMTPAuthenticationError' in str(e):
                    error_message = 'There was an issue with our email service. Our team has been notified.'
                elif 'SMTPConnectError' in str(e):
                    error_message = 'Unable to connect to email service. Please try again in a few minutes.'
                else:
                    error_message = 'Sorry, there was an error sending your message. Please try again later.'

                messages.error(request, error_message)

                # Re-render the form with the user's data
                return render(request, 'core/contact.html', {'form': form})
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {'form': form})

def privacy(request):
    return render(request, 'core/privacy.html')

def terms(request):
    return render(request, 'core/terms.html')