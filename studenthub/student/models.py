from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return f"ATY>{self.name} - {self.email}"


#  sabak_42

from django.contrib.auth.models import AbstractUser


class OzubuzdunUser(AbstractUser):

    phone_nuber = models.CharField(max_length=10, null=True, blank=True)
    tulgan_kun = models.DateField(null=True, blank=True)
