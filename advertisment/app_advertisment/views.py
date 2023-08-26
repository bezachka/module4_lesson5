from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Advertisment
from .forms import AdvertismentForm
from django.core.handlers.wsgi import WSGIRequest
from django.urls import reverse
import requests


# Create your views here.

def index(request):
    #adv = Advertisment(title = f'Объявление создано через views', text = 'Кто-то перешел в index.html', price = 100, user = 'admin')
    #adv.save()

    advertisements = Advertisment.objects.all()
    

    title = request.GET.get('query')
    if title:
        advertisements = Advertisment.objects.filter(title__icontains = title)
    else:
        advertisements = Advertisment.objects.all()

    context = {'advertisments': advertisements,
               'title' : title,
               }
    return render(request, 'advertisment/index.html', context)

def top_sellers(request):
    return render(request, 'advertisment/top-sellers.html')


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
        return render(request, 'advertisment/advertisement-post.html', context)

def advertisement(request, pk):
    advertisment = Advertisment.objects.get(id = pk)
    context = {'advertisment' : advertisement}

    return render(request, 'advertisment/advertisement.html', context)

   
