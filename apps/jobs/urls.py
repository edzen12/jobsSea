from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.vacancy_list, name='vacancy_list'),
    path('vacancy/<int:vacancy_id>/', views.vacancy_detail, name='vacancy_detail'),
    path('register/job_seeker/', views.job_seeker_register, name='job_seeker_register'),
    path('register/employer/', views.employer_register, name='employer_register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='vacancy_list'), name='logout'),
    path('profile/', views.profile, name='profile'), # Assuming a profile view will be created
    # Add other app-specific URLs here, e.g., for resume management, applications, favorites
    path('resumes/', views.resume_management, name='resume_management'),
    path('applications/', views.my_applications, name='my_applications'),
    path('favorites/', views.favorite_vacancies, name='favorite_vacancies'),
]

