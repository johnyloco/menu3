from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    image = models.ImageField(upload_to="restaurant_photos", blank=True, null=True)

    def __str__(self):
        return self.name
