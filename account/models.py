from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    img = models.ImageField(upload_to='user/', null=True, blank=True)
    bio = models.CharField(max_length=200, null=True, blank=True)
    birth_day = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=13, unique=True, null=True, blank=True)

    def __str__(self):
        return self.username
