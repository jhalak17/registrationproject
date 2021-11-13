from django.urls import path
from django.conf.urls import url
from .import views

urlpatterns=[
    path('', views.home, name='home'),
    path('data', views.data, name='data'),
    path('registration', views.registration, name='registration'),
    path('upload', views.upload, name='upload'),
    path('home', views.home, name='home'),
    ]