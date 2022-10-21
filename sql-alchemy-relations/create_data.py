import csv
import random
from datetime import  date, datetime, timedelta
from faker import Faker

from models import Company


fake = Faker('ru_RU')
#print(fake.name(), fake.city_name(), fake.large_company())

def fake_companies(num_rows=10):
    companies = []
    for _ in range(num_rows):
        companies.append(
            [fake.large_company(), fake.city_name(),
            fake.street_address(), fake.phone_number()]
        )
    return companies


def fake_employees(companies, num_rows=10):
    employees = []
    for company in companies:
        for _ in range(num_rows):
            employee = [fake.name(), fake.job(), fake.phone_number(),
                fake.free_email(), fake.date_of_birth(minimum_age=18, maximum_age=70)]
            employees.append(company + employee)
    return employees

def fake_payments(employees):
    payments = []
    for employee in employees:
        for month in range(1, 13):
            payment_date = date(2022, month, random.randint(1, 28))
            ammount = random.randint(20000, 200000)
            payment = [payment_date, ammount]
            payments.append(employee + payment)
    return payments


def get_project_name():
    projects = ['Ребрендинг', 'Разработка CRM', 'Обслуживание 1С', 'Разработка сайта',
                'Опрос покупателей', 'Запуск колцентра', 'Модернизация wifi-сети',
                'Проведение исследований', 'Дизайн сайта', 'Разработка моб. приложения',
                'Дизайн буклетов', 'Аудит информационной безопасности',
                'Обучение сотрудников']

    return random.choice(projects)


def projects_for_employee(company_id, employee_id):
    projects = []
    for month in range(1, 13):
        date_start = date(2022, month, random.randint(1, 10))
        date_and = date_start + timedelta(days=random.randint(5, 20))
        project = [get_project_name(), company_id, employee_id, date_start, date_and]
        projects.append(project)
    return projects


def fake_project_list():
    data= []
    companies = Company.query.all()
    for company in companies:
        for employee in company.employees:
            data += projects_for_employee(company.id, employee.id)

    return data


"""def generate_data(payments):
    with open("salary.csv", "w", encoding="utf-8", newline='')as file:
        writer = csv.writer(file, delimiter=";")
        for payment in payments:
            writer.writerow(payment)"""

def generate_data(data, filename):
    with open(filename, "w", encoding="utf-8", newline='')as file:
        writer = csv.writer(file, delimiter=";")
        for row in data:
            writer.writerow(row)


if __name__ == "__main__":
    generate_data(fake_project_list(), 'projects.csv')
    """companies = fake_companies()
    employees = fake_employees(companies)
    payments = fake_payments(employees)
    generate_data(payments)"""
