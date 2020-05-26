from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import record

class add_record_doc(forms.ModelForm): 

    class Meta:
        model = record
        fields = ['pat','symptoms','pres','record_file']
        labels = {
            "pat" : "Patient",
            "symptoms":"Symptoms",
            "pres" : "Prescription",
            "record_file":"File",
        }

class update_record(forms.ModelForm):

    class Meta:
        model = record
        fields = ['symptoms','pres','record_file']
        labels = {
            "symptoms": "Symptoms",
            "pres": "Prescription",
            "record_file":"File",
        }
    
