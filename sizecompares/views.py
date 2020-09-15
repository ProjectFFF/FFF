from django.shortcuts import render, redirect, get_object_or_404


def sizecompares(request):
    return render(request, 'sizecompares.html')