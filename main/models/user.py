from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Roles(models.TextChoices):
        DEVELOPER = "developer"
        MANAGER = "manager"
        ADMIN = "admin"

    date_of_birth = models.DateField()
    phone = models.CharField(max_length=13)
    role = models.CharField(
        max_length=255, default=Roles.DEVELOPER, choices=Roles.choices
    )
