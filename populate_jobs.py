import os
import django
from datetime import date, timedelta

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youthhub.settings')
django.setup()

from main.models import Job

def populate():
    # Check if jobs already exist to avoid duplicates
    if Job.objects.count() > 0:
        print("Jobs already exist in the database.")
        return

    jobs = [
        {
            "title": "Junior Frontend Developer",
            "company": "TechSolutions Ltd",
            "location": "Nairobi",
            "job_type": "Full-time",
            "description": "We are looking for a junior developer with strong React and CSS skills to join our dynamic team. You will work on building responsive web interfaces.",
            "deadline": date.today() + timedelta(days=30)
        },
        {
            "title": "Data Science Intern",
            "company": "DataCorp Africa",
            "location": "Remote",
            "job_type": "Internship",
            "description": "Great opportunity for students! Learn how to process heavy datasets using Python, Pandas, and SQL. Mentorship provided.",
            "deadline": date.today() + timedelta(days=14)
        },
        {
            "title": "Social Media Manager",
            "company": "Creative Buzz",
            "location": "Mombasa",
            "job_type": "Part-time",
            "description": "Manage our social media presence. Skills in content creation, SEO, and digital marketing strategies are required.",
            "deadline": date.today() + timedelta(days=21)
        },
        {
            "title": "UX/UI Designer",
            "company": "Innovate Lab",
            "location": "Nairobi",
            "job_type": "Contract",
            "description": "Design user-friendly interfaces for mobile and web apps. Experience with Figma and user research is a must.",
            "deadline": date.today() + timedelta(days=45)
        },
        {
            "title": "Backend Developer",
            "company": "FinTrust Systems",
            "location": "Remote",
            "job_type": "Full-time",
            "description": "Seeking a backend engineer with Django and PostgreSQL experience to build secure financial applications.",
            "deadline": date.today() + timedelta(days=60)
        }
    ]

    for job_data in jobs:
        Job.objects.create(**job_data)
        print(f"Created job: {job_data['title']}")

    print("Database populated successfully!")

if __name__ == '__main__':
    populate()
