from django.urls import path
from Youtube import views

urlpatterns = [
    path("", views.home),
    path("servercall", views.servercall)
]