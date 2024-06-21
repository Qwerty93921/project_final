from django.db import models
from django.forms.utils import ValidationError
from django import forms
from django.core import validators

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img/', null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    price = models.DecimalField(null=False, blank=False, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
