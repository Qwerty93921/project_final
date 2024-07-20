from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.urls import reverse
from decimal import Decimal
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


def basket(request):
    basket = request.session.get('basket', {})
    basket_total = request.session.get('basket_total', '0.00')
    context = {
        'basket': basket,
        'basket_total': basket_total,
    }
    return render(request, 'basket.html', context={'basket': basket})


def add_to_basket(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    basket = request.session.get('basket', {})

    if str(product_id) not in basket:
        basket[str(product_id)] = {'title': product.title, 'price': str(product.price), 'quantity': 1}
    else:
        basket[str(product_id)]['quantity'] += 1

    request.session['basket'] = basket

    total_price = calculate_basket_total(basket)
    request.session['basket_total'] = str(total_price)
    return redirect(reverse('products'))


def calculate_basket_total(basket):
    total = Decimal('0.00')
    for item in basket.values():
        total += Decimal(item['price']) * item['quantity']
    return total


def about(request):
    return render(request, 'about.html', context={})


# def basket(request):
#     return render(request, 'basket.html', context={})


def order_create(request):
    return render(request, 'order.html', context={})


def pay(request):
    return render(request, 'payment.html', context={})


def process_payment_1(request):
    if request.method == "POST":
        address = request.POST.get('address')
        house_number = request.POST.get('house_number')
        flat_number = request.POST.get('flat_number')
        floor_number = request.POST.get('floor_number')
        return render(request, 'payment.html', context={})
    else:
        return HttpResponse('Invalid request')


def process_payment_2(request):
    if request.method == "POST":
        cardholder_name = request.POST.get('cardholder_name')
        card_number = request.POST.get('card_number')
        expiry_date = request.POST.get('expiry_date')
        cvv = request.POST.get('cvv')
        billing_address = request.POST.get('billing_address')
        return render(request, 'payment_success.html', context={'cardholder_name': cardholder_name})
    else:
        return HttpResponse('Invalid request')
