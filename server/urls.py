from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register),
    path('login/', views.api_login),
    path('set-profile/', views.set_profile),
    path('profile/', views.profile_data),
    path('get-current-lottery/', views.get_current_lottery),
    path('won-lotteries/', views.lottries_won),
    path('registered-lotteries/', views.registered_lotteries),
    path('register-in-lottery/', views.register_in_lottery),
    path('d466072c4f71832b3ee11ac6afa6dec0/', views.create_lottery)
]
