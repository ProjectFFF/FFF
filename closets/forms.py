from django import forms
from .models import Newcloth

class NewclothPost(forms.ModelForm):
    class Meta:
        model = Newcloth
        fields = ['cloth_name', 'shoulder', 'chest', 'arm', 'total_length', 'image']

class ImgclothPost(forms.ModelForm):
    class Meta:
        model = Newcloth
        fields = ['image']