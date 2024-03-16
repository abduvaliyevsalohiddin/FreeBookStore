from django.db import models
from django.contrib.auth.models import AbstractUser


class UserAdmin(AbstractUser):
    phone = models.CharField(max_length=15, unique=True)
    birthday = models.DateField(blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username
