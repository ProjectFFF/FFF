from django.shortcuts import render, redirect, get_object_or_404


def mysettings(request):
    return render(request, 'mysettings.html')

