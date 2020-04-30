from django.db import models
from django.contrib.auth.models import User

status_choices =(
    ('pending','pending'),
    ('approved','approved'),
    ('rejected','rejected'),
    ('cancelled','cancelled'),
)

class appointment(models.Model):
    doc = models.ForeignKey(User,null=True, on_delete=models.CASCADE,related_name="ap1")
    pat = models.ForeignKey(User,null=True, on_delete=models.CASCADE,related_name="ap2")

    date_time = models.CharField(max_length = 100)
    status = models.CharField(max_length = 20 ,default='rejected',choices=status_choices)
    doc_cmts = models.CharField(max_length=150)

