from django import views
from django.urls import path, include
from .views import *
urlpatterns = [
    path('',home, name="home"),
    path('login', login, name="login"),
    path('register/', register, name="register"),
    path('activities', activities, name='activities'),
    path('hotels', hotels, name='hotels'),
    path('restaurants', restaurants, name='restaurants'),
    path('réserver', réserver, name='réserver')

]
