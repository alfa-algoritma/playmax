import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import requests
from django.shortcuts import render, redirect, get_object_or_404
from main.models import Product
from django.http import HttpResponse, JsonResponse
from main.forms import ProductForm
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json

@login_required(login_url='/login/')
def show_main(request):
    form = ProductForm()
    context = {
        'app_name': 'PlayMax Sport Station',
        'name': request.user.username,
        'form': form,
        'user_id': request.user.id,
    }
    return render(request, "main.html", context)

def register(request):
    form = UserCreationForm()
    return render(request, "register.html", {"form": form})

def login_user(request):
    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def logout_user(request):
    logout(request)
    return redirect('main:login')

@login_required(login_url='/login/')
def get_product_json(request):
    filter_type = request.GET.get('filter')
    if filter_type == 'my':
        products = Product.objects.filter(user=request.user)
    else:
        products = Product.objects.all()
    return HttpResponse(serializers.serialize('json', products))

@login_required(login_url='/login/')
def get_product_by_id_ajax(request, id):
    product = get_object_or_404(Product, pk=id)
    return HttpResponse(serializers.serialize('json', [product]))

@csrf_exempt
@login_required(login_url='/login/')
def add_product_ajax(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return JsonResponse({"status": "success"}, status=201)
        else:
            return JsonResponse({"status": "error", "errors": form.errors}, status=400)
    return JsonResponse({"status": "error"}, status=405)

@csrf_exempt
@login_required(login_url='/login/')
def edit_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return JsonResponse({"status": "success"}, status=200)
        else:
            return JsonResponse({"status": "error", "errors": form.errors}, status=400)
    return JsonResponse({"status": "error"}, status=405)

@csrf_exempt
@login_required(login_url='/login/')
def delete_product_ajax(request, id):
    if request.method == 'DELETE':
        product = get_object_or_404(Product, pk=id, user=request.user)
        product.delete()
        return JsonResponse({"status": "success"}, status=200)
    return JsonResponse({"status": "error"}, status=405)

@csrf_exempt
def register_ajax(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"status": "success", "message": "Registrasi berhasil! Silakan login."}, status=201)
        else:
            return JsonResponse({"status": "error", "errors": form.errors}, status=400)
    return JsonResponse({"status": "error"}, status=405)

@csrf_exempt
def login_ajax(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"status": "success", "message": "Login berhasil!"}, status=200)
        else:
            return JsonResponse({"status": "error", "message": "Username atau password salah."}, status=401)
    return JsonResponse({"status": "error"}, status=405)

@login_required(login_url='/login/')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {'product': product}
    return render(request, "product_detail.html", context)

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        # Buat produk baru
        new_product = Product.objects.create(
            user=request.user,
            name=data["name"],
            price=int(data["price"]),
            description=data["description"],
            category=data["category"],
            thumbnail=data["thumbnail"],
            is_featured=data["isFeatured"]
        )
        
        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

# View untuk Proxy Gambar (Agar emulator bisa load gambar)
def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)

    try:
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        content_type = response.headers.get('Content-Type', 'image/jpeg')
        return HttpResponse(response.content, content_type=content_type)
    except Exception as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)