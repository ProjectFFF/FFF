"""FFFproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import main.urls
import main.views
import accounts.urls
import accounts.views
import closets.urls
import closets.views
import mysettings.urls
import mysettings.views
import sizecompares.urls
import sizecompares.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.welcome, name="welcome"),
    path('main/', include('main.urls')),
    path('accounts/', include('accounts.urls')),
    path('closets/', include('closets.urls')),
    path('mysettings/', include('mysettings.urls')),
    path('sizecompares/', include('sizecompares.urls')),
]
    
