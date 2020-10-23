from django.shortcuts import render, redirect, get_object_or_404
from closets.models import Newcloth, Newcloth_closet

def othersclosets(request):
    records_c = Newcloth_closet.objects
    return render(request, 'othersclosets.html', {'records':records_c})
