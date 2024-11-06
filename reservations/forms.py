from django import forms
from menu3.reservations.models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'time', 'guests', 'special_requests']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'guests': forms.NumberInput(attrs={'min': 1}),
            'special_requests': forms.Textarea(attrs={'placeholder': 'Any special requests'}),
        }
