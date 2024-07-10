from django.shortcuts import render, redirect
from .models import Product
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
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


def pay(request):
    return render(request, 'payment.html', context={})


def process_payment(request):
    if request.method == "POST":
        cardholder_name = request.POST.get('cardholder_name')
        card_number = request.POST.get('card_number')
        expiry_date = request.POST.get('expiry_date')
        cvv = request.POST.get('cvv')
        billing_address = request.POST.get('billing_address')
        return render(request, 'payment_success.html', context={'cardholder_name': cardholder_name})
    else:
        return HttpResponse('Invalid request')


def payment_success(request):
    return render(request, 'payment_success', context={})
