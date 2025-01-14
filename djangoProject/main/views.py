from django.shortcuts import render
from .models import Salary_years, Number_vacancies, Salary_city, Vacancy_rate_city, Skills, Salary_years_developer, Salary_years_developer_img, Number_vacancies_developer, Number_vacancies_developer_img, Salary_city_developer, Salary_city_developer_img, Vacancy_rate_city_developer, Vacancy_rate_city_developer_img, Skills_developer, Skills_developer_img
import requests
from datetime import datetime, timedelta
from django.shortcuts import render

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
    now = datetime.now()
    two_days_ago = now - timedelta(days=2)

    url = "https://api.hh.ru/vacancies"
    params = {
        "text": "1С-разработчик OR 1c разработчик OR 1с OR 1c OR 1 c OR 1 с",
        "search_field": "name",
        "per_page": 10,
        "order_by": "publication_time",
        "date_from": two_days_ago.isoformat() + "Z", 
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(f"Ошибка при запросе: {response.status_code}")
        vacancies = []
    else:
        print(response.json())  
        vacancies = response.json().get('items', [])

        vacancy_details = []

        for vacancy in vacancies:
            vacancy_id = vacancy['id']
            details_url = f'https://api.hh.ru/vacancies/{vacancy_id}'
            details_response = requests.get(details_url)

            if details_response.status_code != 200:
                continue
            
            details_data = details_response.json()
            published_at = datetime.fromisoformat(details_data['published_at'].replace('Z', '+00:00'))
            formatted_datetime = published_at.strftime("%d:%m:%Y %H:%M")

            vacancy_info = {
                'title': details_data['name'],
                'description': details_data['description'],
                'skills': ', '.join([skill['name'] for skill in details_data.get('key_skills', [])]),
                'company': details_data['employer']['name'],
                'salary': details_data['salary']['from'] if details_data.get('salary') and details_data['salary']['from'] is not None else 'Не указано',
                'region': details_data['area']['name'],
                'published_at': formatted_datetime
            }
            
            vacancy_details.append(vacancy_info)
    return render(request, 'main/recent_jobs.html', {'vacancies': vacancy_details})
