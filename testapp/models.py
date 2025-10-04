# testapp/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # role choices
    class Roles(models.TextChoices):
        USER = "USER", "User"
        PROVIDER = "PROVIDER", "Provider"
        ADMIN = "ADMIN", "Admin"
        SUPERADMIN = "SUPERADMIN", "Superadmin"

    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.USER
    )
def __str__(self):
    def __str__(self):
        return f"{self.username} ({self.role})"