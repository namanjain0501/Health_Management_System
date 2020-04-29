from django.contrib import admin
from django.urls import path,include
from .import views

app_name = 'accounts'

urlpatterns = [
    path('signup-doctor', views.signup_doctor,name="signup_doctor"),
    path('signup-patient',views.signup_patient,name="signup_patient"),
    # path('login-doctor',views.login_doctor,name="login-doctor"),
    # path('login-patient',views.login_patient,name="login-patient"),
    # path('detail-doctor',views.doctor_details,name="doctor_details"),
    # path('detail-patient',views.patient_details,name="patient_details"),
]