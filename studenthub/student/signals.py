from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import UserProfile

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def crete_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        instance.userprofile.save()