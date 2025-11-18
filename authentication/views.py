import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({
                'status': True,
                'message': 'Login successful!',
                'username': username,
            }, status=200)
        else:
            return JsonResponse({
                'status': False,
                'message': 'Invalid credentials',
            }, status=401)
    return JsonResponse({'status': False, 'message': 'Invalid method'}, status=405)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        # Validasi sederhana
        if User.objects.filter(username=username).exists():
            return JsonResponse({'status': False, 'message': 'Username already exists'}, status=400)

        user = User.objects.create_user(username=username, password=password)
        user.save()

        return JsonResponse({'status': True, 'message': 'Register successful!'}, status=200)
    return JsonResponse({'status': False, 'message': 'Invalid method'}, status=405)

@csrf_exempt
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return JsonResponse({'status': True, 'message': 'Logout successful!'}, status=200)
    return JsonResponse({'status': False, 'message': 'User not logged in'}, status=401)