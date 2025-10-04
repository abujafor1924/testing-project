# testapp/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from .enums import UserRoles  # import the enum

class User(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=UserRoles.choices,  # use the imported enum
        default=UserRoles.USER
    )

    def __str__(self):
        return f"{self.username} ({self.role})"
