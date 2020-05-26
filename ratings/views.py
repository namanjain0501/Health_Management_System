from django.shortcuts import render,redirect
from accounts.models import Doctor
from records.models import record
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url = '/login/')
def edit_ratings(request,id):
    if 'rating' in request.GET:
        rat_s = request.GET['rating']
        if(rat_s == ""):
            messages.error(request,f'Please select any rating')
            return redirect('records:view_record')
        rat = int(rat_s)
        print(rat)
        rec = record.objects.get(id=id)
        rec.rating = rat
        doc = rec.doc.doctor
        doc.points = doc.points+rat
        doc.num_reviews = doc.num_reviews+1
        doc.save()
        rec.save()
        messages.success(request,f'{rat} Rating given for Dr. {doc.name}')
        return redirect('records:view_record')
    else:
        print("NO")
        return redirect('records:view_record')
