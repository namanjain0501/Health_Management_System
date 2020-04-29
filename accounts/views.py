from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import DoctorSignup,PatientSignup,UserRegisterForm,user_update,profile_pic_doc,profile_pic_pat
from django.contrib.auth import login,logout
from .models import Doctor,Patient,Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from PIL import Image
from django.core.files.base import ContentFile

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

@login_required(login_url="/login/")
def profile(request):
    if request.method == 'POST':
        if request.user.profile.type == 'D':
            user_form = user_update(request.POST, instance=request.user)
            pic_form = profile_pic_doc(request.POST,instance=request.user.doctor)

            if user_form.is_valid() and pic_form.is_valid():
                user_form.save()
                pic_form.save()
                messages.success(request, f'Your Account Has been Updated')
                return redirect('profile')
            
            context = {
                'user_form': user_form,
                'pic_form': pic_form
            }
            return render(request, 'accounts/profile_doc.html', context)
        
        else:
            user_form = user_update(request.POST, instance=request.user)
            pic_form = profile_pic_pat(request.POST,instance=request.user.patient)

            if user_form.is_valid() and pic_form.is_valid():
                user_form.save()
                pic_form.save()
                messages.success(request, f'Your Account Has been Updated')
                return redirect('profile')
            
            context = {
                'user_form': user_form,
                'pic_form': pic_form
            }
            return render(request, 'accounts/profile_pat.html', context)

    else:
        if request.user.profile.type == 'D':
            user_form = user_update(instance = request.user)
            pic_form = profile_pic_doc(instance = request.user.doctor)

            context = {
                'user_form': user_form,
                'pic_form': pic_form
            }
            return render(request, 'accounts/profile_doc.html', context)
        
        else:
            user_form = user_update(instance = request.user)
            pic_form = profile_pic_pat(instance = request.user.patient)

            context = {
                'user_form': user_form,
                'pic_form': pic_form
            }
            return render(request, 'accounts/profile_pat.html', context)










