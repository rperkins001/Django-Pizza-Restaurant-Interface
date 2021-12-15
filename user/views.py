from django.forms.widgets import PasswordInput
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PizzaOrder


def homepage (request):
    context = {}
    return render (request, 'user/homepage.html', context)

def pizza_order (request):
    context = {}
    return render (request, 'user/pizza_order.html', context)

def checkout(request):
    context = {}
    return render (request, 'user/checkout.html', context)

def confirm(request):
    context = {}
    return render (request, 'user/confirm.html', context)