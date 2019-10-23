from django.db import models
from django.contrib.auth.models import User

class Daddy_O(models.Model):
    """Model for the Daddy-O (aka the user)"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("daddy_o")
        verbose_name_plural = ("daddy_os")