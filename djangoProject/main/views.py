from django.shortcuts import render
from .models import Salary_years, Number_vacancies, Salary_city, Vacancy_rate_city, Skills


def index(request):
    return render(request, 'main/index.html')

def general_statistics(request):
    dynamics = Salary_years.objects.all()
    dynamics_count = Number_vacancies.objects.all()
    salary_city_level = Salary_city.objects.all()
    rate_vacancy = Vacancy_rate_city.objects.all()
    skills = Skills.objects.all()
    return render(request, 'main/statistics.html', {'dynamics': dynamics, 'dynamics_count': dynamics_count, 'salary_city_level': salary_city_level, 'rate_vacancy': rate_vacancy, 'skills': skills})

def geography(request):
    return render(request, 'main/geography.html')

def relevance(request):
    return render(request, 'main/relevance.html')

def skills(request):
    return render(request, 'main/skills.html')

def recent_jobs(request):
    return render(request, 'main/recent_jobs.html')