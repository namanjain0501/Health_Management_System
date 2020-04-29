from django.shortcuts import render
from accounts.models import Doctor

def search(request):
    if 'search' in request.GET:
        doctors = []
        search_name = request.GET['search']
        for doctor in Doctor.objects.all():
            if doctor.name == search_name or doctor.specialization == search_name or doctor.locality == search_name:
                doctors.append(doctor)
        return render(request,'search/search.html',{'doctors':doctors}) 

    doctors = Doctor.objects.all()
    return render(request,'search/search.html',{'doctors':doctors}) 

def doctor_detail(request,id):
    doctor = Doctor.objects.get(id = id)
    return render(request,'search/doctor_detail.html',{'doctor':doctor})
