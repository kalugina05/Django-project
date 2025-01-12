from django.db import models


class Salary_years(models.Model):
    year = models.CharField('Год', max_length=4)
    average_salary = models.CharField('Средняя зарплата', max_length=10)

    def __str__(self):
        return self.year
    
    class Meta:
        verbose_name = 'Динамику уровня зарплат по годам'
        verbose_name_plural = 'Динамика уровня зарплат по годам'
