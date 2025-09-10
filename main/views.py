from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'PlayMax Sport Station',
        'name': 'Muhammad Alfa Mubarok',
        'class': 'PBP D',
        'product_name': 'Adidas Adizero Evo SL',
        'product_price': 2600000,
        'product_description': 'Boost ur running performance',
        'product_category': 'Running Shoes',
        'product_stock': 25,
    }
    return render(request, "main.html", context)