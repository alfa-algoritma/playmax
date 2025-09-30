from django import forms
from main.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "category", "thumbnail", "stock"]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline focus:border-pink-500',
                'placeholder': 'Masukkan nama produk'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline focus:border-pink-500',
                'placeholder': 'Masukkan harga'
            }),
            'description': forms.Textarea(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline focus:border-pink-500',
                'rows': 4,
                'placeholder': 'Masukkan deskripsi produk'
            }),
            'category': forms.TextInput(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline focus:border-pink-500',
                'placeholder': 'Contoh: Shoes, Apparel'
            }),
            'thumbnail': forms.URLInput(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline focus:border-pink-500',
                'placeholder': 'Masukkan URL gambar'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline focus:border-pink-500',
                'placeholder': 'Masukkan jumlah stok'
            }),
        }