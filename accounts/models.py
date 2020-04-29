from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User
from records.models import record 
from PIL import Image

blood_grp_choices =(
        ('A-','A-'),
        ('A+','A+'),
        ('B-','B-'),
        ('B+','B+'),
        ('AB-','AB-'),
        ('AB+','AB+'),
        ('O-','O-'),
        ('O+','O+'),
    )

gender_choices =(
        ('M','M'),
        ('F','F'),
    )


class Doctor(models.Model):
    name = models.CharField(max_length = 100)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    adhaar_num = models.CharField(max_length=20,blank=True)
    blood_group = models.CharField(max_length = 4 ,blank=True,choices=blood_grp_choices)
    age = models.IntegerField(blank=True)
    gender = models.CharField(max_length = 1,blank=True,choices = gender_choices)
    locality = models.CharField(max_length=50)
    home_address = models.CharField(max_length=150,blank=True)
    work_address = models.CharField(max_length=150,blank=True)
    specialization = models.CharField(max_length=100)
    specialization_proof = models.FileField(blank=True)
    image = models.ImageField(default='def_M.jpg', upload_to = 'profile_pics')
    patient_records = models.ManyToManyField(record,related_name="p1")
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
    	return self.name
      

class Patient(models.Model):
    name = models.CharField(max_length = 100)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    blood_group = models.CharField(max_length = 4 ,blank=True,choices=blood_grp_choices)
    age = models.IntegerField(blank=True)
    gender = models.CharField(max_length=1, blank=True,choices=gender_choices)
    address = models.CharField(max_length=150,blank=True)
    image = models.ImageField(default = 'def_M.jpg', upload_to = 'profile_pics')
    records = models.ManyToManyField(record)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
    	return self.name


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=1) 

    def __str__(self):
        return self.user.username

       




