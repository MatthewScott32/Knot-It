import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from knotitapp.models import Time, Knot
from ..connection import Connection

def get_time(time_id):
   
    return Time.objects.get(pk=time_id)

def get_knots():
    current_user = request.user.id
    all_knots = Knot.objects.filter(user_id=current_user).values("id", "name")
    # if request.method == 'GET':
    all_stores = Knot.objects.all()
    return all_knots

@login_required
def time_form(request):
    if request.method == 'GET':
        # times = get_times()
        template = 'times/form.html'
        # context = {
        #     'all_times': times
        # }

        return render(request, template)


@login_required
def time_edit_form(request, time_id):

    if request.method == 'GET':
        time = get_time(time_id)
        times = get_knots()

        template = 'times/form.html'
        context = {
            'time': time,
            # 'all_times': times
        }

        return render(request, template, context)