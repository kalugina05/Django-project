from django.shortcuts import render
from .models import Salary_years


def index(request):
    return render(request, 'main/index.html')

def general_statistics(request):
    dynamics = Salary_years.objects.all()
    return render(request, 'main/statistics.html', {'dynamics': dynamics })

def geography(request):
    return render(request, 'main/geography.html')

def relevance(request):
    return render(request, 'main/relevance.html')

def skills(request):
    return render(request, 'main/skills.html')

def recent_jobs(request):
    return render(request, 'main/recent_jobs.html')