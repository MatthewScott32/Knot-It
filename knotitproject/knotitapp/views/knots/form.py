import sqlite3
from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from knotitapp.models import Knot
from ..connection import Connection
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.forms import ModelChoiceField




class KnotForm(forms.ModelForm):
    class Meta:
        model = Knot
        exclude = ["user"]
        
    def __init__(self, id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id=id


def get_knot(knot_id):

    return Knot.objects.get(pk=knot_id)

@login_required
def knot_form(request):
    context = {}
    current_user = request.user.id
    if request.method == 'POST':
        form = KnotForm(current_user, request.POST, request.FILES)
        if form.is_valid():
            knot = form.save(commit=False)
            knot.user_id = request.user.id
            knot.save()
            return redirect('knotitapp:knots')

    else:
        form = KnotForm(current_user)
        context['form'] = form
        context['knot_id'] = None

        return render(request, 'knots/form.html', context)


@login_required
def knot_edit_form(request, knot_id):
    context = {}
    current_user = request.user.id
    knot = get_knot(knot_id)
    if request.method == 'GET':
        form = KnotForm(current_user, instance=knot)
        context['form'] = form
        context['knot_id'] = knot_id

        template = 'knots/form.html'

        return render(request, template, context)

    if request.method == 'POST':
        # Pass in the user edited data via the resquest.POST param, and any media files via request.FILES (i.e. docs, imgs, etc.) while ensuring the correct instance is being updated
        form = KnotForm(current_user, request.POST, request.FILES, instance=knot)

        # Ensure form validation is complete and the correct data is being passed back to the server
        if form.is_valid():
            # Save the changes to the database
            form.save()
            return redirect('knotitapp:knots')