from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('register/', views.register),
    path('login/', views.api_login),
    path('set-profile/', views.set_profile),
    path('data/', views.xyz)
]
