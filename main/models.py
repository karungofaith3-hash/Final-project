from django.db import models

class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('Internship', 'Internship'),
        ('Part-time', 'Part-time'),
        ('Full-time', 'Full-time'),
        ('Contract', 'Contract'),
    ]

    title = models.CharField(max_length=200)
    company = models.CharField(max_length=150)
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    description = models.TextField()
    deadline = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company}"

class Mentor(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    bio = models.TextField()
    expertise = models.CharField(max_length=200, help_text="e.g. AI, Career Coaching, Finance")
    image = models.ImageField(upload_to='mentors/', blank=True, null=True)
    contact_email = models.EmailField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.mentor.name} by {self.user.username}"

