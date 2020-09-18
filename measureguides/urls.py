from django.urls import path
from . import views

urlpatterns = [
    path('measureguides/', views.measureguides, name="measureguides"),
]