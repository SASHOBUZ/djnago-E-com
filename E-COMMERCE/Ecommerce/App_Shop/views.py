from django.shortcuts import render

# Import Views list
from django.views.generic import ListView, DetailView

# Models
from App_Shop.models import Product

# Mixin for login required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class Home(ListView):
    model = Product
    template_name = 'App_Shop/home.html'


class ProductDetails(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'App_Shop/product_details.html'
