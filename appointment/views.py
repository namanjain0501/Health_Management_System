from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import Doctor
from .forms import appointment_form
from .models import appointment

@login_required(login_url = "/login/")
def book_appointment(request,id):
    if request.user.profile.type == 'D':
        messages.error(request,f'Only Patients can book appointments')
        return redirect('/')
    else:
        d1 = Doctor.objects.get(id=id)
        doc = d1.user
        if request.method == 'POST':
            form = appointment_form(request.POST)
            if form.is_valid():
                appointm = form.save(commit=False)
                appointm.doc = doc
                appointm.pat = request.user
                a1 = appointm.save()
                doc.doctor.appointments.add(appointm)
                request.user.patient.appointments.add(appointm)
                messages.success(request,f'Appointment booked for Dr. {doc.doctor.name} at {appointm.date_time} ')
                return redirect('/')
            else:
                return render(request,'appointment/book_appointment.html',{'form':form,'d1':d1})
        else: 
            form = appointment_form()
            return render(request,'appointment/book_appointment.html',{'form':form,'d1':d1})

@login_required(login_url = '/login/')
def view_appointment(request):
    if request.user.profile.type == 'P':
        a1 = request.user.patient.appointments.all()
        a1 = a1[::-1]
        return render(request,'appointment/view_appointments_pat.html',{'a1':a1})
    else:
        a1 = request.user.doctor.appointments.all()
        a1 = a1[::-1]
        return render(request,'appointment/view_appointments_doc.html',{'a1':a1})
    
@login_required(login_url = '/login/')
def cancel_view(request,id):
    ap = appointment.objects.get(id=id)
    if ap.pat == request.user :
        ap.status = 'cancelled'
        ap.save()
        messages.success(request,f'Appointment cancelled')
        return redirect('appointment:view-appointment')
    else:
        messages.error(request,f'Invalid Request')
        return redirect('/')

@login_required(login_url = '/login/')
def approve_view(request,id):
    ap = appointment.objects.get(id=id)
    if ap.doc == request.user:
        ap.status = "approved"
        ap.save()
        messages.success(request,f'Appointment Approved')
        return redirect('appointment:view-appointment')
    else:
        messages.error(request,f'Invalid Request')
        return redirect('/')

@login_required(login_url = '/login/')
def reject_view(request,id):
    ap = appointment.objects.get(id=id)
    if ap.doc == request.user:
        ap.status = "rejected"
        ap.save()
        messages.success(request,f'Appointment Rejected')
        return redirect('appointment:view-appointment')
    else:
        messages.error(request,f'Invalid Request')
        return redirect('/')

@login_required(login_url = '/login/')
def edit_cmts(request,id):
    if 'comments' in request.GET:
        cmts = request.GET['comments']
        ap = appointment.objects.get(id=id)
        ap.doc_cmts = cmts
        ap.save()
        messages.success(request,f'Comment edited')
        return redirect('appointment:view-appointment')
    else:
        return redirect('appointment:view-appointment')





