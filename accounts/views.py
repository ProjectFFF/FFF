from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

