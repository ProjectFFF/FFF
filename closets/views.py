from django.shortcuts import render, redirect, get_object_or_404


def new(request):
    return render(request, 'new.html')

def record(request):
    return render(request, 'record.html')

def mycloset(request):
    return render(request, 'mycloset.html')
