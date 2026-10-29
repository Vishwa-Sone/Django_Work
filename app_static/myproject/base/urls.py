from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home,name="home"),
    path('mobile/',mobile,name="mobile"),
    path('fashion/',fashion,name="fashion")
]
