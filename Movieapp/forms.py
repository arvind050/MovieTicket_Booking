from django import forms
from Movieapp.models import Movie,Customer,Shows,Bookings

class Movieform(forms.ModelForm):
    class Meta:
        model= Movie
        fields = "__all__"

class CustomerForm(forms.ModelForm):
    class Meta:
        model= Customer
        fields = "__all__"

class showsForm(forms.ModelForm):
    class Meta:
        model = Shows
        fields = '__all__'

class Bookingform(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = ['bookedshow','bookedSeats','totalPrice']