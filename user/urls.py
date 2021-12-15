from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('order/', views.pizza_order, name = 'pizza_order'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('confirm/', views.confirm, name = 'confirm'),
]