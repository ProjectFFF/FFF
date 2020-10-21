from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new, name="new"),
    path('record/', views.record, name="record"),
    path('mycloset/', views.mycloset, name="mycloset"),
    path('newcloth/', views.newcloth, name="newcloth"),
    path('create/', views.create, name="create"),
    path('detail/<int:pk>', views.detail, name="detail"),
    path('update/<int:pk>', views.update, name="update"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('compare/<int:pk>', views.compare, name="compare"),
]