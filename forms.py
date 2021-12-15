from django.db.models.base import Model
from django.forms import ModelForm, widgets
from .models import *
from django import forms

from .models import PizzaOfTheDay, Toppings


class PizzaOrder():
    class Meta:
        model = PizzaOfTheDay, Toppings
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    

class Checkout ():
    class Meta:
        model = Customer
        fields = ('name_first', 'name_last', 'street_address', 'zip_code', 'phone_number', 'customer_email', )

