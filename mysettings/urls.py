from django.urls import path
from . import views

urlpatterns = [
    path('mysettings/', views.mysettings, name="mysettings"),
]