from django.contrib.auth.models import User
from django.db import models

from django.utils import timezone

from menu3.restaurants.models import Restaurant


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()
    special_requests = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Reservation by {self.user.username} at {self.restaurant.name} on {self.date}"

