"""
URL configuration for final_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import index, login, home, product_list_viewer, about, basket, order_create, pay, process_payment


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login, name='login'),
    path('index/', index, name='index'),
    path('home/', home, name='home'),
    path('products/', product_list_viewer, name='products'),
    path('about/', about, name='about'),
    path('basket/', basket, name='basket'),
    path('order/', order_create, name="order"),
    path('pay/', pay, name='pay'),
    path('process_payment/', process_payment, name='process_payment'),
    # path('', include('final_app.urls')),
    # path('home/', home, name='home'),
    # path('contacts/', contacts, name='contacts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
