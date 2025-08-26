from django.urls import path
from core import views

urlpatterns = [
    path("", views.home),
    path("servercall", views.servercall),
    path("clientcall", views.clientcall)
]