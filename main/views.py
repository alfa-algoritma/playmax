from django.shortcuts import render
from .models import Product

def show_main(request):
    products = Product.objects.all()

    context = {
        'app_name': 'PlayMax',
        'name': 'Muhammad Alfa Mubarok',
        'class': 'PBP D',
        'products': products # Kirim data produk ke template
    }

    return render(request, "main.html", context)