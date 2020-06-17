import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from knotitapp.models import Time, Knot
from ..connection import Connection


def get_time(time_id):
   
    return Time.objects.get(pk=time_id)


@login_required
def time_details(request, time_id):
    if request.method == 'GET':
        time = get_time(time_id)
        template_name = 'times/details.html'
        return render(request, template_name, {'time': time})

    elif request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
          
            time_to_update = Time.objects.get(pk=time_id)
            time_to_update.time = form_data['time']
            time_to_update.knot_id = form_data['knot']

            time_to_update.save()

            return redirect(reverse('knotitpapp:times'))

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
                
            time = Time.objects.get(pk=time_id)
            time.delete()

            return redirect(reverse('knotitapp:times'))