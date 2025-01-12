from django.db import models


class Salary_years(models.Model):
    year = models.CharField('Год', max_length=4)
    average_salary = models.CharField('Средняя зарплата', max_length=10)

    def __str__(self):
        return self.year
    
    class Meta:
        verbose_name = 'Динамику уровня зарплат по годам'
        verbose_name_plural = 'Динамика уровня зарплат по годам'

class Number_vacancies(models.Model):
    year = models.CharField('Год', max_length=4)
    count = models.CharField('Количество вакансий', max_length=10)

    def __str__(self):
        return self.year
    class Meta:
        verbose_name = 'Динамику количества вакансий по годам'
        verbose_name_plural = 'Динамика количества вакансий по годам'

class Salary_city(models.Model):
    city = models.CharField('Город', max_length=20)
    average_salary = models.CharField('Средняя зарплата', max_length=10)

    def __str__(self):
        return self.city
    
    class Meta:
        verbose_name = 'Уровень зарплат по городам'
        verbose_name_plural = 'Уровень зарплат по городам'

class Vacancy_rate_city(models.Model):
    city = models.CharField('Город', max_length=20)
    rate_vacancy = models.CharField('Доля вакансий', max_length=10)

    def __str__(self):
        return self.city
    
    class Meta:
        verbose_name = 'Доля вакансий по городам'
        verbose_name_plural = 'Доля вакансий по городам'

class Skills(models.Model):
    skill = models.CharField('Навык', max_length=20)
    count = models.CharField('Количество упоминаний', max_length=10)

    def __str__(self):
        return self.skill
    
    class Meta:
        verbose_name = 'ТОП-20 навыков'
        verbose_name_plural = 'ТОП-20 навыков'