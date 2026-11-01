from django.urls import path
from .views import *

urlpatterns = [
    path('',login_,name='login_'),
    path('register/',register,name='register'),
    path('logout/',logout_,name='logout_'),
    path('profile/',profile,name='profile'),
    path('reset_password/',reset_password,name='reset_password'),
    path('forgot_password/',forgot_password,name='forgot_password'),
    path('upadte/',update,name='update')
]


