from django.urls import path
from menu3.restaurants import views


urlpatterns = [
    path('', views.restaurant_list, name='restaurant_list'),
    path('<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),
]
