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
    skill = models.CharField('Навык', max_length=50)
    count = models.CharField('Количество упоминаний', max_length=10)

    def __str__(self):
        return self.skill
    
    class Meta:
        verbose_name = 'ТОП-20 навыков'
        verbose_name_plural = 'ТОП-20 навыков'

class Salary_years_developer(models.Model):
    year = models.CharField('Год', max_length=4)
    average_salary = models.CharField('Средняя зарплата', max_length=10)

    def __str__(self):
        return self.year
    
    class Meta:
        verbose_name = 'Динамику уровня зарплат по годам для 1С разработчика'
        verbose_name_plural = 'Динамика уровня зарплат по годам для 1С разработчика'

class Salary_years_developer_img(models.Model):
    img1 = models.ImageField(null=True, upload_to="images/")
    
    class Meta:
        verbose_name = 'Картинка уровня зарплат по годам для 1С разработчика'


class Number_vacancies_developer(models.Model):
    year = models.CharField('Год', max_length=4)
    count = models.CharField('Количество вакансий', max_length=10)

    def __str__(self):
        return self.year
    
    class Meta:
        verbose_name = 'Динамику количества вакансий по годам для 1С разработчика'
        verbose_name_plural = 'Динамика количества вакансий по годам для 1С разработчика'

class Number_vacancies_developer_img(models.Model):
    img2 = models.ImageField(null=True, upload_to="images/")
    
    class Meta:
        verbose_name = 'Картинка динамики количества вакансий по годам для 1С разработчика'
    
class Salary_city_developer(models.Model):
    city = models.CharField('Город', max_length=20)
    average_salary = models.CharField('Средняя зарплата', max_length=10)

    def __str__(self):
        return self.city
    
    class Meta:
        verbose_name = 'Уровень зарплат по городам для 1С разработчика'
        verbose_name_plural = 'Уровень зарплат по городам для 1С разработчика'

class Salary_city_developer_img(models.Model):
    img3 = models.ImageField(null=True, upload_to="images/")
    
    class Meta:
        verbose_name = 'Картинка уровня зарплат по городам для 1С разработчика'

class Vacancy_rate_city_developer(models.Model):
    city = models.CharField('Город', max_length=20)
    rate_vacancy = models.CharField('Доля вакансий', max_length=10)

    def __str__(self):
        return self.city
    
    class Meta:
        verbose_name = 'Доля вакансий по городам для 1С разработчика'
        verbose_name_plural = 'Доля вакансий по городам для 1С разработчика'

class Vacancy_rate_city_developer_img(models.Model):
    img4 = models.ImageField(null=True, upload_to="images/")
    
    class Meta:
        verbose_name = 'Картинка доли вакансий по городам для 1С разработчика'

class Skills_developer(models.Model):
    skill = models.CharField('Навык', max_length=50)
    count = models.CharField('Количество упоминаний', max_length=10)

    def __str__(self):
        return self.skill
    
    class Meta:
        verbose_name = 'ТОП-20 навыков для 1С разработчика'
        verbose_name_plural = 'ТОП-20 навыков для 1С разработчика'

class Skills_developer_img(models.Model):
    img5 = models.ImageField(null=True, upload_to="images/")
    
    class Meta:
        verbose_name = 'Картинка топа навыков для 1С разработчика'