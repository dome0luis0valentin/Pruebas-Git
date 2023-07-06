from django.shortcuts import render

# Create your views here.
def ver_menu(request):
    return render(request, "menu.html")