from django.shortcuts import render
from menu3.restaurants.models import Restaurant


def location_list(request):
    cities = Restaurant.objects.values_list('city', flat=True).distinct()
    return render(request, 'locations/location_list.html', {'cities': cities})
