import sqlite3
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from knotitapp.models import Time, Knot
from ..connection import Connection

def get_time(time_id):
    
    return Time.objects.get(pk=time_id)

def get_knots(user):
    all_knots = Knot.objects.filter(user=user)
    return all_knots

@login_required
def time_form(request):
    if request.method == 'GET':
        knots = get_knots(request.user)
        template = 'times/form.html'
        context = {
            'all_knots': knots
            
        }

        return render(request, template, context)


@login_required
def time_edit_form(request, time_id):

    if request.method == 'GET':
        time = get_time(time_id)
        if request.user.id == time.user_id:
            knots = get_knots(request.user)

            template = 'times/form.html'
            context = {
                'time': time,
                'all_knots': knots
            }

            return render(request, template, context)
        
        else:
            return redirect(reverse('knotitapp:home'))