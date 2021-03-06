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
    path('knots/<int:knot_id>/', knot_details, name='knot'),
    path('knots/<int:knot_id>/form/', knot_edit_form, name='knot_edit_form'),
    path('times/', times_list, name='times'),
    path('times/<int:time_id>/', time_details, name='time'),
    path('times/form', time_form, name='time_form'),
    path('times/<int:time_id>/form/', time_edit_form, name='time_edit_form'),
]