from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_view(request: WSGIRequest):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse('profile'))
        else:
            return render(request, 'auth/login.html')

    print(request.POST)    
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password = password)

    if user is not None:
        login(request, user)
        return redirect(reverse('profile'))
    else:
        return render(request, 'auth/login.html', {'error' : 'Пользователь не найден'})


def profile_view(request):
    return render(request, 'auth/profile.html')


def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

