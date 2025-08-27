from django.urls import path
from SchoolAPI import views

urlpatterns = [
    path("", views.home),
    path("servercall", views.servercall),
    path("clientcall", views.clientcall)
]