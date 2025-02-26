from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile

User = get_user_model()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a Profile automatically when a User is created"""
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Save the Profile automatically when the User is saved"""
    try:
        if hasattr(instance, 'profile'):  # Ensure profile exists before saving
            instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)  # Create the profile if it doesn't exist


