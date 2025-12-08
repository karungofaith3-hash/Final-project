import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youthhub.settings')
django.setup()

from main.models import Mentor

def populate():
    if Mentor.objects.count() > 0:
        print("Mentors already exist in the database.")
        return

    mentors = [
        {
            "name": "Dr. Sarah Kimani",
            "role": "Chief Data Scientist",
            "company": "DataCorp Africa",
            "bio": "Expert in AI and Machine Learning with over 10 years of experience leading data teams. Passionate about empowering women in tech.",
            "expertise": "Data Science, AI, Leadership",
            "contact_email": "sarah.k@datacorp.example.com",
            # We will use pravatar.cc for dynamic images
        },
        {
            "name": "James Omondi",
            "role": "Senior Frontend Engineer",
            "company": "TechSolutions Ltd",
            "bio": "Specializes in React and modern CSS. I help junior developers bridge the gap between design and code.",
            "expertise": "Frontend Dev, React, UX",
            "contact_email": "james.o@techsolutions.example.com",
        },
        {
            "name": "Linda Wanjiku",
            "role": "Product Manager",
            "company": "Innovate Lab",
            "bio": "Experienced PM with a background in FinTech. I can help you understand product lifecycles and agile methodologies.",
            "expertise": "Product Management, Agile, FinTech",
            "contact_email": "linda.w@innovate.example.com",
        },
        {
            "name": "David Kamau",
            "role": "Cloud Architect",
            "company": "CloudNine Systems",
            "bio": "Certified AWS Solutions Architect. I mentor students on cloud computing, DevOps, and serverless architectures.",
            "expertise": "Cloud Computing, AWS, DevOps",
            "contact_email": "david.k@cloudnine.example.com",
        }
    ]

    for data in mentors:
        Mentor.objects.create(**data)
        print(f"Created mentor: {data['name']}")

    print("Mentors populated successfully!")

if __name__ == '__main__':
    populate()
