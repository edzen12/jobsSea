from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Vacancy, Category, Company
from django.utils import timezone

def vacancy_list(request):
    vacancies = Vacancy.objects.all().order_by("-published_date")
    categories = Category.objects.all()
    companies = Company.objects.all()

    category_filter = request.GET.get("category")
    company_filter = request.GET.get("company")
    location_filter = request.GET.get("location")
    salary_min_filter = request.GET.get("salary_min")

    if category_filter:
        vacancies = vacancies.filter(category__id=category_filter)
    if company_filter:
        vacancies = vacancies.filter(company__id=company_filter)
    if location_filter:
        vacancies = vacancies.filter(location__icontains=location_filter)
    if salary_min_filter:
        try:
            vacancies = vacancies.filter(salary_from__gte=int(salary_min_filter))
        except ValueError:
            pass

    context = {
        "vacancies": vacancies,
        "categories": categories,
        "companies": companies,
        "locations": Vacancy.objects.values_list("location", flat=True).distinct().order_by("location"),
    }
    return render(request, "index.html", context)

def vacancy_detail(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)
    return render(request, "jobs/vacancy_detail.html", {"vacancy": vacancy})

def job_seeker_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration/job_seeker_register.html", {"form": form})

def employer_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration/employer_register.html", {"form": form})

@login_required
def profile(request):
    return render(request, "jobs/profile.html")

@login_required
def resume_management(request):
    resumes_data = [] # Empty list as per "bare code" request
    return render(request, "jobs/resume_management.html", {"resumes": resumes_data})

@login_required
def my_applications(request):
    applications_data = [] # Empty list
    return render(request, "jobs/my_applications.html", {"applications": applications_data})

@login_required
def favorite_vacancies(request):
    favorite_vacancies_data = [] # Empty list
    return render(request, "jobs/favorite_vacancies.html", {"favorite_vacancies": favorite_vacancies_data})

