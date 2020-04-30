from django.contrib import admin
from django.urls import path,include
from .import views

app_name = 'accounts'

urlpatterns = [
    path('signup-doctor', views.signup_doctor,name="signup_doctor"),
    path('signup-patient',views.signup_patient,name="signup_patient"),
]