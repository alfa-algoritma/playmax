from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'PlayMax',
        'name': 'Muhammad Alfa Mubarok',   
        'class': 'Kelas PBP D'     
    }

    # Me-render template main.html dengan data dari context
    return render(request, "main.html", context)