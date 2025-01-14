import pandas as pd
import requests
import matplotlib.pyplot as plt
import numpy as np

# Функция для получения курсов валют
def get_currency_rates():
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    response = requests.get(url)
    data = response.json()
    return data['Valute']

# Получение курсов валют
currency_rates = get_currency_rates()

# Загрузка данных
file_path = "C:/Users/АННА/OneDrive/Desktop/аналитика для проекта на джанго/vacancies_2024.csv"
data = pd.read_csv(file_path, encoding='utf-8')

# Фильтрация данных по зарплате
data = data[(data['salary_from'] <= 10000000) & (data['salary_to'] <= 10000000)]

# Создание нового столбца для средней зарплаты
data['average_salary'] = (data['salary_from'] + data['salary_to']) / 2

# Функция для конвертации зарплаты в рубли
def convert_salary(row):
   
    if pd.isna(row['average_salary']):
        return 0
    if row['salary_currency'] == 'RUR':
        return row['average_salary']
    elif row['salary_currency'] in currency_rates:
        rate = currency_rates[row['salary_currency']]['Value']
        nominal = currency_rates[row['salary_currency']]['Nominal']
        return row['average_salary'] * rate / nominal
    return 0


# Применяем конвертацию к зарплатам
data['average_salary_rub'] = data.apply(convert_salary, axis=1)


# Динамика уровня зарплат по годам
data['year'] = pd.to_datetime(data['published_at'], utc=True).dt.year  # Добавлен параметр utc=True
salary_trend = data.groupby('year').agg({'average_salary_rub': 'mean'}).reset_index()

# Применение условия: если год меньше 2010, делим на 4
salary_trend['average_salary_rub'] = salary_trend.apply(
    lambda row: row['average_salary_rub'] / 4 if row['year'] < 2009 else row['average_salary_rub'], axis=1
)

salary_trend['average_salary_rub'] = salary_trend['average_salary_rub'].round(0).astype(int)  # Округление до целых
salary_trend.index += 1

# Вывод динамики уровня зарплат по годам
print("Динамика уровня зарплат по годам:")
print(salary_trend)

# Построение графика динамики уровня зарплат
plt.figure(figsize=(10, 5))
plt.plot(salary_trend['year'], salary_trend['average_salary_rub'], marker='o', color='royalblue')  # Установка ярко-синего цвета
plt.title("Динамика уровня зарплат по годам")
plt.xlabel("Год")
plt.ylabel("Средняя зарплата (руб.)")

# Установка меток на оси X
plt.xticks(salary_trend['year'], rotation=45)  # Отображаем каждый год и поворачиваем метки для удобства

plt.grid()
plt.tight_layout()  # Пытаемся оптимально распределить пространство
plt.show()


# Динамика количества вакансий по годам
vacancies_trend = data.groupby('year').size().reset_index(name='count')
vacancies_trend.index += 1

# Вывод динамики количества вакансий по годам
print("\nДинамика количества вакансий по годам:")
print(vacancies_trend)

# Построение графика динамики количества вакансий
plt.figure(figsize=(10, 5))
plt.bar(vacancies_trend['year'], vacancies_trend['count'], color='#ffd700')
plt.title("Динамика количества вакансий по годам")
plt.xlabel("Год")
plt.ylabel("Количество вакансий")
# Установка меток на оси X

plt.xticks(salary_trend['year'], rotation=45)  # Отображаем каждый год и поворачиваем метки для удобства

plt.grid()
plt.tight_layout()  # Пытаемся оптимально распределить пространство
plt.show()


# Общее количество вакансий
total_vacancies = data.shape[0]

# Вычисление доли вакансий по городам
vacancy_share = data.groupby('area_name').size() / total_vacancies
vacancy_share = vacancy_share.reset_index(name='vacancy_share')

# Отбор городов с долей вакансий > 1%
filtered_data = data.merge(vacancy_share[vacancy_share['vacancy_share'] > 0.01], on='area_name')

# Уровень зарплат по городам
city_salary = filtered_data.groupby('area_name').agg({'average_salary_rub': 'mean'}).reset_index()
city_salary['average_salary_rub'] = city_salary['average_salary_rub'].round(0).astype(int)  # Округление до целых

# Сортировка: сначала по среднему уровню зарплаты (по убыванию), затем по названию города (по возрастанию)
city_salary = city_salary.sort_values(by=['average_salary_rub', 'area_name'], ascending=[False, True])

# Выбор только 10 городов с самой высокой зарплатой
top_10_cities = city_salary.head(10)

# Вывод уровня зарплат по 10 городам без индексов
print("\nУровень зарплат по 10 городам с самой высокой зарплатой:")
print(top_10_cities.to_string(index=False))

# Построение графика уровня зарплат по 10 городам
plt.figure(figsize=(12, 6))
plt.barh(top_10_cities['area_name'][::-1], top_10_cities['average_salary_rub'][::-1], color='lightgreen')
plt.title("Уровень зарплат по городам")
plt.xlabel("Средняя зарплата (руб.)")
plt.ylabel("Город")
plt.grid()
plt.show()


# Доля вакансий по городам
city_vacancies = data['area_name'].value_counts().reset_index()
city_vacancies.columns = ['area_name', 'count']

# Рассчет доли вакансий в процентах
total_count = city_vacancies['count'].sum()
city_vacancies['percentage'] = (city_vacancies['count'] / total_count) * 100

# Округление процентов до сотых
city_vacancies['percentage'] = city_vacancies['percentage'].round(2)

# Отбор топ-10 городов и объединение остальных в "Другие"
top_cities = city_vacancies.nlargest(10, 'count')
other_cities_count = city_vacancies['count'].sum() - top_cities['count'].sum()
other_cities_percentage = (other_cities_count / total_count) * 100

# Создание DataFrame для "Другие"
other_cities_df = pd.DataFrame({'area_name': ['Другие'], 'count': [other_cities_count], 'percentage': [round(other_cities_percentage, 2)]})

# Объединение топ-10 городов и "Другие"
final_city_vacancies = pd.concat([top_cities, other_cities_df], ignore_index=True)

# Установка индекса, начинающегося с 1
final_city_vacancies.index += 1

# Вывод доли вакансий по городам
print("\nДоля вакансий по городам:")
print(final_city_vacancies[['area_name', 'count', 'percentage']])

plt.figure(figsize=(10, 10))
colors = plt.cm.Reds(np.linspace(0.4, 1, len(final_city_vacancies)))  # Используем цвета от ярко-красного до светло-красного

# Настройка шрифта для процентов
textprops = {'fontsize': 10, 'fontweight': 'light'}  # Уменьшаем размер шрифта и делаем его менее жирным

plt.pie(final_city_vacancies['count'], labels=final_city_vacancies['area_name'], 
        autopct='%1.1f%%', colors=colors, textprops=textprops)

plt.title("Доля вакансий по городам")
plt.axis('equal')  # Для равного соотношения осей
plt.show()

# ТОП-20 навыков по годам
data['key_skills'] = data['key_skills'].fillna('')

# Извлекаем только первый навык до первого \n
data['key_skills'] = data['key_skills'].str.split('\n').str[0]

# Создание списка навыков
skills_list = data['key_skills'].value_counts().reset_index()
skills_list.columns = ['skill', 'count']
top_skills = skills_list.nlargest(21, 'count')

# Изменяем индексы для вывода с 1
top_skills.index = top_skills.index

# Вывод ТОП-20 навыков, начиная со 2-й строки
print("\nТОП-20 навыков:")
print(top_skills.iloc[1:])  # Пропускаем первую строку

# Построение графика ТОП-20 навыков, начиная со 2-й строки

# Предположим, что top_skills - это DataFrame, содержащий данные о навыках и количестве упоминаний

# Сортировка по количеству упоминаний (по убыванию)
sorted_skills = top_skills.sort_values(by='count', ascending=False)

# Построение графика навыков в обратном порядке
plt.figure(figsize=(12, 6))
plt.barh(sorted_skills['skill'].iloc[1:], sorted_skills['count'].iloc[1:], color='orange')  # Пропускаем первую строку
plt.title("ТОП-20 навыков")
plt.xlabel("Количество упоминаний")
plt.ylabel("Навык")
plt.gca().invert_yaxis()
plt.grid()
plt.show()



