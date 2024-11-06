from django.urls import path
from menu3.menus import views

urlpatterns = [
    path('restaurant/<int:restaurant_id>/', views.menu_by_restaurant, name='menu_by_restaurant'),
]
