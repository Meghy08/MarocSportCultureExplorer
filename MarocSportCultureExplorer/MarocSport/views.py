from django.shortcuts import render, redirect
# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):

    return render(request, 'register.html')

def login(request):
    
    return render(request, 'login.html')


def activities(request):
    return render(request,'activities.html')

def hotels(request):
    return render(request,'hotels.html')

def restaurants(request):
    return render(request,'restaurants.html')

def réserver(request):
    return render(request,'réserver.html')



