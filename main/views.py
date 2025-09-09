from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406431391',
        'name': 'Muhammad Alfa Mubarok',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)