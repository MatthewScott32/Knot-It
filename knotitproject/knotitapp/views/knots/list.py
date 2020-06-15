  
import sqlite3
from django.shortcuts import render, redirect, reverse
from knotitapp.models import Knot
from ..connection import Connection
from django.contrib.auth.decorators import login_required

# @login_required
def knots_list(request):
    if request.method == 'GET':
                current_user = request.user.id
                all_knots = Knot.objects.filter(user_id=current_user).values("id", "name", "rope_type", "company", "notes", "video" )
                template = 'knots/list.html'
                context = {
                    'all_knots': all_knots
                }

                return render(request, template, context)
            
    elif request.method == 'POST':
        form_data = request.POST
        new_knot = Knot(
            name = form_data['name'],
            rope = form_data['rope_type'],
            company = form_data['company'],
            notes = form_data['notes'],
            video = form_data['video'],
            user_id = request.user.id,
        ) 
        new_knot.save()
        return redirect(reverse('knotitapp:knots'))