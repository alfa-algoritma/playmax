from django.shortcuts import render, redirect
from main.models import Product
from django.http import HttpResponseRedirect, HttpResponse
from main.forms import ProductForm
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime

@login_required(login_url='/login/')
def show_main(request):
    products = Product.objects.filter(user=request.user)
    context = {
        'app_name': 'PlayMax Sport Station',
        'name': request.user.username,
        'npm': '2406431391',
        'class': 'PBP D',
        'products': products,
        'last_login': request.COOKIES.get('last_login', 'Belum pernah login')
    }
    return render(request, "main.html", context)

@login_required(login_url='/login/')
def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    context = {'form': form}
    return render(request, "create_product.html", context)

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Akun berhasil dibuat!")
            return redirect('main:login')
    context = {'form':form}
    return render(request, "register.html", context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST) # DIUBAH DI SINI
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                response = HttpResponseRedirect(reverse('main:show_main'))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
            else:
                messages.error(request, "Username atau password salah.")
        else:
            messages.error(request, "Username atau password salah.")
    
    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    messages.info(request, "Anda berhasil logout.")
    return response

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