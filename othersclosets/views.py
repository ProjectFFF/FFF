from django.shortcuts import render, redirect, get_object_or_404


def othersclosets(request):
    return render(request, 'othersclosets.html')
