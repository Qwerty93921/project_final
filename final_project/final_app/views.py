from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return render(request, 'index.html', context={})


def login(request):
    return render(request, 'login.html', context={})


def home(request):
    return render(request, 'index.html', context={})


# def about(request):
#     return render(request, 'about.html', context={})
#
#
# def home(request):
#     return render(request, 'home.html', context={})
