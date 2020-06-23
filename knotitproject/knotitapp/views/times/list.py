
import sqlite3
from django.shortcuts import render, redirect, reverse
from knotitapp.models import Knot, Time
# from ..connection import Connection
from django.contrib.auth.decorators import login_required

@login_required
def times_list(request):
    if request.method == 'GET':

        current_user = request.user.id
        all_knots = Knot.objects.filter(user_id=current_user).values("id", "name", "rope_type", "company", "notes", "how_to_video", "image" )

        all_times = Time.objects.filter(user_id=current_user).values("id", "time", "knot", "knot__name")
        knotId = request.GET.get('knot', None)

        if knotId is not None:
            all_knots = all_knots.filter(knot_id=knotId)

        template = 'times/list.html'
        context = {
                    'all_knots':all_knots,
                    'all_times': all_times,
        }

        return render(request, template, context)
            
    elif request.method == 'POST':
        form_data = request.POST
        new_time = Time(
            time = form_data['time'],
            knot_id = int(form_data['knot']),
            user_id = request.user.id,
        ) 
        new_time.save()
        return redirect(reverse('knotitapp:times'))