from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('main/', main_page, name='main'),
    path('admin/', admin.site.urls, name='admin'),
    path('friends/',all_friends,name='friends'),
    path('establishments/',place_arrangement,name='establishments'),
    path('hosts/',all_hosts,name='hosts'),
    path('guest/',all_guests,name='guests'),
    path('establishments_rating/',Establishments_rating,name= 'Establishments_rating'),
    path('users_rating/', Users_rating, name= 'Users_rating'),
]