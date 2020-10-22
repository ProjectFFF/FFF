from django.contrib import admin
from .models import Newcloth, Newcloth_closet

# class PhotoInline(admin.TabularInline):
    # model = Photocloset

# class NewclothAdmin(admin.ModelAdmin):
    # inlines = [PhotoInline, ]


admin.site.register(Newcloth)
admin.site.register(Newcloth_closet)
