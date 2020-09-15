from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new, name="new"),
    path('record/', views.record, name="record"),
    path('mycloset/', views.mycloset, name="mycloset"),
]