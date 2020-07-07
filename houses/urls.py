from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('houses', post, name='houses'),
   # path('success', success, name='success'),
]

