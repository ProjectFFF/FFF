from django.urls import path
from . import views

urlpatterns = [
    path('sizecompares/', views.sizecompares, name="sizecompares"),
]