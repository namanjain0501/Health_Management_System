from django.db import models
from django.contrib.auth.models import User

class record(models.Model):
    doc = models.ForeignKey(User,null=True, on_delete=models.CASCADE,related_name="re1")
    pat = models.ForeignKey(User,null=True, on_delete=models.CASCADE,related_name="re2")

    time = models.DateTimeField(auto_now_add=True)
    symptoms = models.CharField(max_length=500)
    pres = models.CharField(max_length=1000)