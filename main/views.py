from django.shortcuts import render
from main.models import Product
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    products = Product.objects.all()

    context = {
        'app_name': 'PlayMax Sport Station',
        'name': 'Muhammad Alfa Mubarok',
        'npm': '2406431391',
        'class': 'PBP D',
        'products': products # Mengirimkan data produk ke template
    }
    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        # Jika form valid, simpan data ke database
        form.save()
        # Redirect kembali ke halaman utama
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")