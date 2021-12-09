from django.shortcuts import render
from django.views.generic import ListView  # импортируем уже знакомый generic

from .models import Product


# Create your views here.

class Products(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 1  # поставим постраничный вывод в один элемент