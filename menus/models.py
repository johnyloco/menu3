from django.db import models

from menu3.restaurants.models import Restaurant


class FoodItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="food_items")
    #This means that each FoodItem is related to a single Restaurant, but a single Restaurant can have multiple FoodItems.
    #on_delete=models.CASCADE:
    #This specifies what should happen to FoodItem records if the related Restaurant record is deleted.
    #models.CASCADE means that if a Restaurant is deleted, all associated FoodItem records should also be deleted. This is called a cascading delete.
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    gluten_free = models.BooleanField(default=False)
    dairy_free = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)


class DrinkItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="drink_items")
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)


class WineItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="wine_items")
    name = models.CharField(max_length=100)
    description = models.TextField()
    wine_type = models.CharField(max_length=50)  # e.g., "Red", "White", "Rosé", etc.
    region = models.CharField(max_length=100, blank=True, null=True)  # optional
    grape_variety = models.CharField(max_length=100, blank=True, null=True)  # optional
    vintage = models.IntegerField(blank=True, null=True)  # year the wine was produced, if relevant
    price = models.DecimalField(max_digits=5, decimal_places=2)
