from django import forms
from .models import Doctor,Patient
from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class DoctorSignup(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = ['name','adhaar_num','phone','blood_group','age','gender','locality','home_address','work_address','specialization']

class PatientSignup(forms.ModelForm): 

    class Meta:
        model = Patient
        fields = ['name','phone','blood_group','age','gender','address']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1','password2']

class user_update(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class profile_pic_doc(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = ['image']

class profile_pic_pat(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ['image']

    