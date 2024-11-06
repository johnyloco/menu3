from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from menu3.reservations.models import Reservation
from menu3.reservations.forms import ReservationForm
from menu3.restaurants.models import Restaurant


@login_required
def make_reservation(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.restaurant = restaurant
            reservation.save()
            return redirect('reservation_success')
    else:
        form = ReservationForm()
    return render(request, 'reservations/make_reservation.html', {'form': form, 'restaurant': restaurant})


def reservation_success(request):
    return render(request, 'reservations/success.html')

