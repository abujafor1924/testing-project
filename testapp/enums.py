from django.db import models

class UserRoles(models.TextChoices):
    USER = "USER", "User"
    PROVIDER = "PROVIDER", "Provider"
    ADMIN = "ADMIN", "Admin"
    SUPERADMIN = "SUPERADMIN", "Superadmin"