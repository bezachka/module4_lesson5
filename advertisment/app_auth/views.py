from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def login_view(request: WSGIRequest):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(reverse('profile'))
        else:
            return render(request, 'auth/login.html')

def profile_view(request):
    return render(request, 'auth/profile.html')

