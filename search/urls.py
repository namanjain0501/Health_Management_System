from django.contrib import admin
from django.urls import path,include
from .import views

app_name = 'search'

urlpatterns = [
    path('', views.search,name="search"),    
    path('doctor/<id>/' , views.doctor_detail ,name = 'doctor-detail'),

]