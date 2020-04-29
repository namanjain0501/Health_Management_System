from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import DoctorSignup,PatientSignup,UserRegisterForm
from django.contrib.auth import login,logout
from .models import Doctor,Patient,Profile

def signup_doctor(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        details_form = DoctorSignup(request.POST,request.FILES)


        if user_form.is_valid() and details_form.is_valid():
            cur_user = user_form.save()

            prof1 = Profile()
            prof1.user = cur_user
            prof1.type = "D"
            prof1.save()
            doc = details_form.save(commit=False)
            doc.user = cur_user
            doc.save()
            
            login(request,cur_user)
            return redirect('/')
        else:
            context = {
                'user_form': user_form,
                'details_form': details_form
            }
            return render(request,'accounts/signup_doctor_view.html',context)

    user_form = UserRegisterForm()
    details_form = DoctorSignup()
    context = {
        'user_form': user_form,
        'details_form': details_form
    }
    return render(request,'accounts/signup_doctor_view.html',context)

def signup_patient(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        details_form = PatientSignup(request.POST)

        if user_form.is_valid() and details_form.is_valid():
            cur_user = user_form.save()
            prof1 = Profile()
            prof1.user = cur_user
            prof1.type = "P"
            prof1.save()
            pat = details_form.save(commit=False)
            pat.user = cur_user
            pat.save()
            
            login(request,cur_user)
            return redirect('/')
        else:
            context = {
                'user_form': user_form,
                'details_form': details_form
            }
            return render(request,'accounts/signup_patient_view.html',context)

    user_form = UserRegisterForm()
    details_form = PatientSignup()
    context = {
        'user_form': user_form,
        'details_form': details_form
    }
    return render(request,'accounts/signup_patient_view.html',context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

# def login_doctor(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             for doctor in Doctor.objects.all():
#                 if doctor.user == user:

#     form = AuthenticationForm()
#     return render(request,'accounts/login_doctor_view.html',{'form':form})








