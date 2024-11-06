from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    allergies = models.CharField(max_length=255, blank=True)  # comma-separated list of allergies

    def __str__(self):
        return f"{self.user.username}'s profile"
