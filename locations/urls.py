from django.urls import path
from menu3.locations import views

urlpatterns = [
    path('', views.location_list, name='location_list'),
]
