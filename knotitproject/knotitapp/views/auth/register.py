from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register_user(request):

    if request.method == "GET":
        template_name = 'registration/register.html'
        return render(request, template_name, {})

    elif request.method == "POST":
        form_data = request.POST

        new_user = User.objects.create_user(
            email=request.POST['email'],
            username=request.POST['username'],
            password=request.POST['password']
        )

        authenticated_user = authenticate(
        email=form_data['email'],
        username=form_data['username'], 
        password=form_data['password']
        )

        if authenticated_user is not None:
            login(request=request, user=authenticated_user)
            return redirect(reverse('knotitapp:home'))

        else:
            return HttpResponse("Username and/or password incorrect.") 
        login(request, new_user)

        return redirect(reverse('knotitapp:home'))