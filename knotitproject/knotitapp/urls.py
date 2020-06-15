from .views import *
from django.urls import path, include

app_name = "knotitapp"

urlpatterns = [
    path('', home, name='home'),
    path('register/', register_user, name="register"),
    path('knots/', knots_list, name='knots'),
    path('times/', times_list, name='times'),
]