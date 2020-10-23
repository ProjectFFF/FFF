from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Member

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user=User.objects.create_user(username=request.POST['id'], password=request.POST['password1'])
            auth.login(request, user)
            member = Member()
            member.id_m= request.POST['id']
            member.password= request.POST['password1']
            member.name= request.POST['name']
            member.nickname= request.POST['nickname']
            member.age= request.POST['age']
            member.gender= request.POST['gender']
            member.email= request.POST['email']
            member.phone_naumber= request.POST['phone_number']
            member.save()
            
            return redirect('home')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['id']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
         return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'login.html')

