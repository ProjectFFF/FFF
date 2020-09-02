from django.shortcuts import render, redirect, get_object_or_404

def welcome(request):
    return render(request, 'home.html')

def read(request):
    return render(request, 'home.html')