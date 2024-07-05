from django.shortcuts import render, redirect
from .models import Product

# Create your views here.


def index(request):
    return render(request, 'index.html', context={})


def login(request):
    return render(request, 'login.html', context={})


def home(request):
    return render(request, 'index.html', context={})


def product_list_viewer(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', context={'products': products})


def about(request):
    return render(request, 'about.html', context={})


def basket(request):
    return render(request, 'basket.html', context={})


def order_create(request):
    return render(request, 'order.html', context={})
