from django.urls import path
from menu3.reservations import views

urlpatterns = [
    path('make/<int:restaurant_id>/', views.make_reservation, name='make_reservation'),
    path('success/', views.reservation_success, name='reservation_success'),
]
