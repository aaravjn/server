from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register),
    path('login/', views.api_login),
    path('set-profile/', views.set_profile),
    path('profile/', views.profile_data),
    path('get-current-lottery/', views.get_current_lottery),
    path('won-lotteries/', views.lottries_won),
    path('registered-lotteries/', views.registered_lotteries),
    path('register-in-lottery/', views.register_in_lottery)
]
