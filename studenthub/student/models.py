from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return f"ATY>{self.name} - {self.email}"


#  sabak_42

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    phone_number = models.CharField(max_length=10, null=True, blank=True)
    tulgan_kun = models.DateField(null=True, blank=True)

from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    info = models.TextField(blank=True)
    website = models.URLField(blank=True)
    tulgan_kun = models.DateField(null=True, blank=True)  

    def __str__(self):
        return f"Profile: {self.user.username} (Tulgan Kun: {self.tulgan_kun})"