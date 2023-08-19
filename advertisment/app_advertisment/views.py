from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Advertisment
from .forms import AdvertismentForm
from django.core.handlers.wsgi import WSGIRequest
from django.urls import reverse


# Create your views here.

def index(request):
    #adv = Advertisment(title = f'Объявление создано через views', text = 'Кто-то перешел в index.html', price = 100, user = 'admin')
    #adv.save()

    advertisements = Advertisment.objects.all()
    context = {'advertisments': advertisements}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def advertisement_post(request : WSGIRequest):
    print(request.POST)
    if request.method == 'POST':
        form = AdvertismentForm(request.POST, request.FILES)
        if form.is_valid():
            adv = Advertisment(**form.cleaned_data)
            adv.user = request.user
            adv.save()
            return redirect(
                reverse('main-page')
            )
        else:
            print(form.errors)
    else:
        form = AdvertismentForm()
        context = {'form': form}
        return render(request, 'advertisement-post.html', context)

def advertisement(request):
    return render(request, 'advertisement.html')

   
