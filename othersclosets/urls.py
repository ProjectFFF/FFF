from django.urls import path
from . import views

urlpatterns = [
    path('othersclosets/', views.othersclosets, name="othersclosets"),
]