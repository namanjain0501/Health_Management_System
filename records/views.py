from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import add_record_doc,update_record
from django.contrib import messages
from accounts.models import Patient
from .models import record

@login_required(login_url="/login/")
def view_patient_records(request):
    if request.user.profile.type == 'D':
        r1 = request.user.doctor.patient_records.all()
        r1 = r1[::-1]
        return render(request,'records/view_records_doc.html',{'r1':r1})
    else:
        r1 = request.user.patient.records.all()
        r1 = r1[::-1]
        return render(request,'records/view_records_pat.html',{'r1':r1})

@login_required(login_url="/login/")
def record_detail(request,id):
    if request.method == 'POST':
        r1 = record.objects.get(id=id)
        form = update_record(request.POST,request.FILES,instance=r1)
        if form.is_valid():
            form.save()
            messages.success(request, f'Record Updated for patient : {r1.pat.patient.name} !')
            return redirect('records:view_record')
        else:
            return render(request,'records/record_update_doc.html',{'form':form})
    else:
        if request.user.profile.type == 'D':
            r1 = record.objects.get(id=id)
            form = update_record(instance=r1)
            return render(request,'records/record_update_doc.html',{'form':form,'r1':r1})
        else:
            r1 = record.objects.get(id = id)
            return render(request,'records/record_detail_pat.html',{'r1':r1})

@login_required(login_url="/login/")
def add_record(request):
    if request.user.profile.type == 'D':
        if request.method == 'POST':
            form = add_record_doc(request.POST,request.FILES)
            if form.is_valid():
                rec = form.save(commit=False)
                rec.doc = request.user
                rec.save()
                pat_user = form.cleaned_data.get('pat')
                pat_name = pat_user.patient.name
                request.user.doctor.patient_records.add(rec)
                pat_user.patient.records.add(rec)
                messages.success(request, f'Record Saved for Patient : {pat_name} !')
                return redirect('/')
            else:
                return render(request,'records/add_record.html',{'form':form})
        else:
            form = add_record_doc()
            return render(request,'records/add_record.html',{'form':form})
    else:
        messages.error(request, f'You Need to be a Doctor to add a record')
        return redirect('/')




