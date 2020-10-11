from django.shortcuts import render, redirect, get_object_or_404
from .models import Guide

def measureguides(request):
    guides = Guide.objects.all()
    return render(request, 'measureguides.html', {'guides' : guides})
