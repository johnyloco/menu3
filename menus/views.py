from django.shortcuts import render, get_object_or_404
from menu3.restaurants.models import Restaurant
from menu3.menus.models import FoodItem, DrinkItem, WineItem


def menu_by_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    food_items = restaurant.food_items.all()
    drink_items = restaurant.drink_items.all()
    wine_items = restaurant.wine_items.all()
    return render(request, 'menus/menu_by_restaurant.html', {
        'restaurant': restaurant,
        'food_items': food_items,
        'drink_items': drink_items,
        'wine_items': wine_items,
    })

