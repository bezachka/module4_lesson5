from django.urls import path
from .views import index, top_sellers, register, login, profile

urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('advertisement/', profile, name='advertisement'),
    path('advertisement-post/', profile, name='advertisement-post'),
]
