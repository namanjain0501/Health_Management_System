from django.shortcuts import render

def homepage(request):
	return render(request,'base_layout.html')

def about(request):
	return render(request,'about.html')
