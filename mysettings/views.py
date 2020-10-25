from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from accounts.models import Member

def mysettings(request):
    
    setting = Member.objects.get(id_m=request.user.username)
    
    return render(request, 'mysettings.html', {'setting': setting})

