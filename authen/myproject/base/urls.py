from django.urls import path
from .views import *


urlpatterns = [
    path('',home,name='home'),
    path('add/',add,name='add'),
    path('hdelete/<int:pk>',hdelete,name='hdelete'),
    path('trash/',trash,name='trash'),
    path('restore/<int:pk>',restore,name='restore'),
    path('hdelete_all/',hdelete_all,name='hdelete_all'),
    path('trestore_all/',trestore_all,name='trestore_all'),
    path('tdelete/<int:pk>',tdelete,name='tdelete'),
    path('tdelete_all/',tdelete_all,name='tdelete_all')
]
