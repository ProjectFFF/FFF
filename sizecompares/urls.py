from django.urls import path
from . import views
from .models import Compare
from closets.models import Newcloth

urlpatterns = [
    path('sizecompares/', views.sizecompares, name="sizecompares"),
]