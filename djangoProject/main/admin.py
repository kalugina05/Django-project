from django.contrib import admin
from .models import Salary_years, Number_vacancies, Salary_city, Vacancy_rate_city, Skills


admin.site.register(Salary_years)
admin.site.register(Number_vacancies)
admin.site.register(Salary_city)
admin.site.register(Vacancy_rate_city)
admin.site.register(Skills)
# Register your models here.
