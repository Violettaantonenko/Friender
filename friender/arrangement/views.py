from django.shortcuts import render
from django.http import HttpResponse
import datetime

friends=["Max","Grigory","Michael","Pedro","Boris",'Nataly','Anna','Darya','Oleg','Aryna']
establishments=['Butter Bro', 'Depo', 'Golden Cafe', 'Gan Bei', 'KFC']
hosts=['Nataly','Anna','Darya','Oleg','Aryna']
guests=["Max","Grigory","Michael","Pedro","Boris"]


def main_page(request):
    return render(request, 'main.html')

def place_arrangement(request):
    context = {
        'establishments': establishments
    }
    return render(request, 'establishments.html',context=context)

def all_friends(request):
    context = {
        "friends":friends
    }
    return render (request, 'friends.html',context=context)
def all_hosts(request):
    context = {
        "hosts":hosts
    }
    return render(request,'hosts.html',context=context)

def all_guests(request):
    context = {
        "guests":guests
    }
    return render(request,'guests.html',context=context)

def Users_rating(reguest):
    return render(reguest, 'users rating.html')

def Establishments_rating(request):
    return render(request, 'establishments rating.html')
