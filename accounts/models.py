from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User
from records.models import record 
from appointment.models import appointment
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
    phone = PhoneField(blank=True, help_text='Contact phone number') #update
    adhaar_num = models.CharField(max_length=20,blank=True)
    blood_group = models.CharField(max_length = 4 ,blank=True,choices=blood_grp_choices)
    age = models.IntegerField(null=True) 
    gender = models.CharField(max_length = 1,blank=True,choices = gender_choices)
    locality = models.CharField(max_length=50) #update
    home_address = models.CharField(max_length=150,blank=True) #update
    work_address = models.CharField(max_length=150,blank=True) #update
    specialization = models.CharField(max_length=100)
    specialization_proof = models.FileField(blank=True,upload_to='specialization_proofs')
    image = models.ImageField(default='def_M.jpg', upload_to = 'profile_pics')
    patient_records = models.ManyToManyField(record,related_name="p1",blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    appointments = models.ManyToManyField(appointment,related_name="app_doc",blank=True)
    points = models.IntegerField(default=0)
    num_reviews = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)


    def __str__(self):
    	return self.name

    def save(self, *args, **kwargs):
        if self.num_reviews == 0:
            self.rating = 0
        else:
            self.rating = self.points/self.num_reviews
        super(Doctor, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
      

class Patient(models.Model):
    name = models.CharField(max_length = 100)
    phone = PhoneField(blank=True, help_text='Contact phone number') #update
    blood_group = models.CharField(max_length = 4 ,blank=True,choices=blood_grp_choices)
    age = models.IntegerField(null=True) 
    gender = models.CharField(max_length=1, blank=True,choices=gender_choices)
    address = models.CharField(max_length=150,blank=True) #update
    image = models.ImageField(default = 'def_M.jpg', upload_to = 'profile_pics')
    records = models.ManyToManyField(record)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    appointments = models.ManyToManyField(appointment,related_name="app_pat")

    def __str__(self):
    	return self.name

    def save(self, *args, **kwargs):
        super(Patient, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=1) 

    def __str__(self):
        return self.user.username

       




