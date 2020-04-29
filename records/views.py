from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import add_record_doc
from django.contrib import messages
from accounts.models import Patient
from .models import record

@login_required(login_url="/login/")
def view_patient_records(request):
    if request.user.profile.type == 'D':
        r1 = request.user.doctor.own_records.all()
        return render(request,'records/view_records.html',{'records':r1})
    else:
        r1 = request.user.patient.records.all()
        return render(request,'records/view_records.html',{'r1':r1})

@login_required(login_url="/login/")
def add_record(request):
    if request.user.profile.type == 'D':
        if request.method == 'POST':
            form = add_record_doc(request.POST)
            if form.is_valid():
                rec = form.save(commit=False)
                rec.doc = request.user
                rec.save()
                pat_user = form.cleaned_data.get('pat')
                pat_name = pat_user.patient.name
                messages.success(request, f'Record Saved for Patient : {pat_name} !')
                return redirect('/')
            else:
                return render(request,'records/add_record.html',{'form':form})
        else:
            form = add_record_doc()
            return render(request,'records/add_record.html',{'form':form})
    else:
        messages.error(request, f'You Need to be a Doctor to add a record')




