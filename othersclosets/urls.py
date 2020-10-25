from django.urls import path
from . import views

urlpatterns = [
    path('othersclosets/', views.othersclosets, name="othersclosets"),
    path('othersclosets_t/', views.subchoice, name="othersclosets_t"),
    path('othersclosets_s/', views.search, name="othersclosets_s"),
]