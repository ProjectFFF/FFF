from django.shortcuts import render, redirect, get_object_or_404


def measureguides(request):
    return render(request, 'measureguides.html')
