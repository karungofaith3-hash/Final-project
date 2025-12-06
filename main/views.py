from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def jobs(request):
    return render(request, 'jobs.html')  # create this template

def mentorship(request):
    return render(request, 'mentorship.html')  # create this template



# Create your views here.
