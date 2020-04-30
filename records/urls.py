from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'records'

urlpatterns = [
    path('view_patient_records/',views.view_patient_records,name="view_record"),
    path('add_record/',views.add_record,name="add_record"),
    path('<id>/',views.record_detail,name="record-detail"),
]