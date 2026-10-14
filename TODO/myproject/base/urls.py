from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('add/', add, name='add'),
    path('complete/', complete, name='complete'),
    path('trash/', trash, name='trash'),
    path('hdelete/<int:pk>',hdelete,name='hdelete'),
    path('update/<int:pk>',update,name='update'),
    path('complete/<int:pk>',hcomplete,name='hcomplete'),
    path('hcomplete_all',hcomplete_all,name='hcomplete_all'),
    path('hdelete_all',hdelete_all,name='hdelete_all'),
    path('restore/<int:pk>',restore,name='restore'),
    path('cdelete/<int:pk>',cdelete,name='cdelete'),
    path('restore_all/',restore_all,name='restore_all'),
    path('cdelete_all/',cdelete_all,name='cdelete_all'),
    path('trestore/<int:pk>',trestore,name='trestore'),
    path('tdelete/<int:pk>',tdelete,name='tdelete'),
    path('trestore_all/',trestore_all,name='trestore_all'),
    path('tdelete_all/',tdelete_all,name='tdelete_all')
]