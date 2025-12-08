from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/', views.jobs, name='jobs'),
    path('jobs/<int:job_id>/', views.job_detail, name='job_detail'),
    path('mentorship/', views.mentorship, name='mentorship'),
    path('mentorship/<int:mentor_id>/', views.book_session, name='book_session'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Auth
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
