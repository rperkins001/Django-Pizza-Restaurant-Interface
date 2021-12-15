from django.db import models
import uuid
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey
from django.db.models.fields.reverse_related import ManyToOneRel
from django.shortcuts import render


# Create your views here.
class Customer(models.Model):
    #user = foreignkey onto user model
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name_first = models.CharField(max_length=65)
    name_last = models.CharField(max_length=65)
    street_address = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=5)
    phone_number = IntegerField(null=False, blank=False, unique=True)
    customer_email  = models.EmailField(max_length=70, blank=True, unique=True)

    def __str__(self):
        return self.name_last, self.name_first 
        
# in the customer model needs a .user foreign key which links to the django default user model.

class Order(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    datetime = models.DateTimeField(auto_now_add=True, blank=True)
    orderPizzas = ForeignKey
    
class OrderPizza(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    indpizza = ForeignKey
    toppings = ForeignKey

class PizzaOfTheDay(models.Model):
    
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    dayofweek = models.CharField(max_length=9)
    pizzatype = models.CharField(max_length=15)
    price = models.DecimalField(max_digits=4, decimal_places=2)

class Toppings(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    Name = models.CharField(max_length=65)
    Price = models.DecimalField(max_digits=4, decimal_places=2)

