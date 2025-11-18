from django.urls import path
from main.views import show_main, register, login_user, logout_user, show_product, get_product_json, add_product_ajax, edit_product_ajax, delete_product_ajax, get_product_by_id_ajax, register_ajax, login_ajax, create_product_flutter, proxy_image

app_name = 'main'

urlpatterns = [
    # Halaman utama
    path('', show_main, name='show_main'),

    # Halaman autentikasi (hanya untuk menampilkan form)
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('product/<int:id>/', show_product, name='show_product'),

    # Endpoints AJAX untuk CRUD
    path('get-product/', get_product_json, name='get_product_json'),
    path('get-product-by-id/<int:id>/', get_product_by_id_ajax, name='get_product_by_id_ajax'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('edit-product-ajax/<int:id>/', edit_product_ajax, name='edit_product_ajax'),
    path('delete-product-ajax/<int:id>/', delete_product_ajax, name='delete_product_ajax'),

    # Endpoints AJAX untuk autentikasi
    path('register-ajax/', register_ajax, name='register_ajax'),
    path('login-ajax/', login_ajax, name='login_ajax'),

    path('', show_main, name='show_main'),
    path('json/', get_product_json, name='get_product_json'),

    # Endpoint untuk Flutter
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    path('proxy-image/', proxy_image, name='proxy_image'),
]
