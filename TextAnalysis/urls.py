from django.urls import path
from TextAnalysis import views

urlpatterns = [
    path("", views.home),
    path("counter", views.counter)
]