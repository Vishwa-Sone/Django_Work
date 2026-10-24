from django.urls import path
from .views import *


urlpatterns = [
    path('home/',home,name='home'),
    path('about/',about,name='about'),
    path('fashion/',fashion,name='fashion')
]
