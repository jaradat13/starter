import logging
from django.contrib.auth.forms import UserCreationForm
from django.forms import modelformset_factory
from django import forms
from django.contrib.auth import get_user_model

from .models import Profile


logger = logging.getLogger(__name__)

CustomUser = get_user_model()  # Get the custom user model dynamically


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = CustomUser  # Use the custom user model
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(disabled=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'image']
        labels = {
            'image': '',
            'delete': '',
        }
        widgets = {
            'image': forms.FileInput(attrs={
                'id': 'id_profile_image',
                'class': 'd-none',  # Hide file insdsdsdsdsdput, can be triggered with JavaScript
            }),
        }

    def save(self, commit=True, user=None):  # Add user parameter
        """
        Override the save method to associate the Profile with the user.
        """
        instance = super().save(commit=False)
        if user:  # If a user is passed in, set it.  This is important for profile creation.
            instance.user = user
        if commit:
            instance.save()
        return instance



UserFormSet = modelformset_factory(CustomUser, form=UserUpdateForm, extra=0)


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Email'
    }))
    subject = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Subject'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Your Message',
        'rows': 5
    }))