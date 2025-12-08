from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import Job, Mentor, Booking
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def jobs(request):
    jobs = Job.objects.all().order_by('-created_at')
    return render(request, 'jobs.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'job_detail.html', {'job': job})

def mentorship(request):
    mentors = Mentor.objects.all()
    return render(request, 'mentorship.html', {'mentors': mentors})

@login_required(login_url='login')
def book_session(request, mentor_id):
    mentor = get_object_or_404(Mentor, pk=mentor_id)
    if request.method == 'POST':
        date = request.POST.get('date')
        message = request.POST.get('message')
        Booking.objects.create(user=request.user, mentor=mentor, date=date, message=message)
        messages.success(request, f'Session booked with {mentor.name} on {date}!')
        return redirect('mentorship')
    return render(request, 'book_session.html', {'mentor': mentor})

@login_required(login_url='login')
def dashboard(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-date')
    return render(request, 'dashboard.html', {'bookings': bookings})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now login.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

