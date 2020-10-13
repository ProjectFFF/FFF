from django.contrib import admin
from .models import Newcloth

# class PhotoInline(admin.TabularInline):
    # model = Photocloset

# class NewclothAdmin(admin.ModelAdmin):
    # inlines = [PhotoInline, ]


admin.site.register(Newcloth)
