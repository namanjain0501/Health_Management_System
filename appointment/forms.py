from django import forms
from .models import appointment

class appointment_form(forms.ModelForm):

    class Meta:
        model = appointment
        fields = ['date_time']