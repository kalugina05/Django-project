from django.shortcuts import render
from .models import Salary_years, Number_vacancies, Salary_city, Vacancy_rate_city, Skills, Salary_years_developer, Salary_years_developer_img, Number_vacancies_developer, Number_vacancies_developer_img, Salary_city_developer, Salary_city_developer_img, Vacancy_rate_city_developer, Vacancy_rate_city_developer_img, Skills_developer, Skills_developer_img


def index(request):
    return render(request, 'main/index.html')

def general_statistics(request):
    dynamics = Salary_years.objects.all()
    dynamics_count = Number_vacancies.objects.all()
    salary_city_level = Salary_city.objects.all()
    rate_vacancy = Vacancy_rate_city.objects.all()
    skills = Skills.objects.all()
    return render(request, 'main/statistics.html', {'dynamics': dynamics, 'dynamics_count': dynamics_count, 'salary_city_level': salary_city_level, 'rate_vacancy': rate_vacancy, 'skills': skills})

def relevance(request):
    dynamics = Salary_years_developer.objects.all()
    image1 = Salary_years_developer_img.objects.all()
    dynamics_count = Number_vacancies_developer.objects.all()
    image2 = Number_vacancies_developer_img.objects.all()
    return render(request, 'main/relevance.html', {'dynamics': dynamics, 'image1': image1, 'dynamics_count':dynamics_count, 'image2':image2})

def geography(request):
    salary_city_level = Salary_city_developer.objects.all()
    image3 = Salary_city_developer_img.objects.all()
    rate_vacancy = Vacancy_rate_city_developer.objects.all()
    image4 = Vacancy_rate_city_developer_img.objects.all()
    return render(request, 'main/geography.html', {'salary_city_level': salary_city_level, 'image3':image3, 'rate_vacancy':rate_vacancy, 'image4':image4})

def skills(request):
    skills = Skills_developer.objects.all()
    image5 = Skills_developer_img.objects.all()
    return render(request, 'main/skills.html', {'skills': skills, 'image5':image5})

def recent_jobs(request):
    return render(request, 'main/recent_jobs.html')