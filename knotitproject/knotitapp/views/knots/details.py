import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from knotitapp.models import Knot
from ..connection import Connection


def get_knot(knot_id):
       
    return Knot.objects.get(pk=knot_id)


@login_required
def knot_details(request, knot_id):
    current_user = request.user.id
    knot = get_knot(knot_id)
    if knot.user_id == current_user:
        if request.method == 'GET':
            template_name = 'knots/details.html'
            return render(request, template_name, {'knot': knot})

        elif request.method == 'POST':
            form_data = request.POST

            if (
                "actual_method" in form_data
                and form_data["actual_method"] == "PUT"
             ):
          
                knot_update = Knot.objects.get(pk=knot_id)
                knot_update.name = form_data['name']
                knot_update.rope_type = form_data['rope_type']
                knot_update.notes = form_data['notes']
                knot_update.how_to_video = form_data['how_to_video']
                knot_update.image = form_data['image']

                knot_update.save()

                return redirect(reverse('knotitapp:knots'))

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
           ):
                
            knot = Knot.objects.get(pk=knot_id)
            knot.delete()            
            return redirect(reverse('knotitapp:knots'))
    else:
        return redirect(reverse('knotitapp:knots'))