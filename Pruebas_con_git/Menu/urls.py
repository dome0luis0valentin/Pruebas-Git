from django.urls import path
from Menu import views

urlpatterns =[
    path("/", views.ver_menu, name = "Ver Menu")
]