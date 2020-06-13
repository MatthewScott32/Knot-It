from .views import *
from django.urls import path, include

app_name = "knotitapp"

urlpatterns = [
    path('', home, name='home'),
    path('knots/', knots_list, name='knots'),
]