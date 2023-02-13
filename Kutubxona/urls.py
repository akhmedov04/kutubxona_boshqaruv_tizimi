"""Kutubxona URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('salom/', salomlash),
    path('salomber/', salom),
    path('', main),
    path('talabalar/', talabalar),
    path('kitoblar/', kitoblar),
    path('talabalar/<int:son>/', talaba),
    path('talaba_ochir/<int:son>/', talaba_ochir),
    path('kitob_ochir/<int:son>/', kitob_ochir),
    path('mualliflar/', mualliflar),
    path('mualliflar/<int:son>', muallif),
    path('records/', records),
    path('admins/', admins),
]
