from .views import *
from django.urls import path, include

app_name = "knotitapp"

urlpatterns = [
    path('', home, name='home'),
    path('register/', register_user, name="register"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('knots/', knots_list, name='knots'),
    path('knots/form', knot_form, name='knot_form'),
    path('times/', times_list, name='times'),
]