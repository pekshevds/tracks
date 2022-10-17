import csv
import random
from datetime import  date
from faker import Faker


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


def generate_data(payments):
    with open("salary.csv", "w", encoding="utf-8", newline='')as file:
        writer = csv.writer(file, delimiter=";")
        for payment in payments:
            writer.writerow(payment)

if __name__ == "__main__":    
    companies = fake_companies()
    employees = fake_employees(companies)
    payments = fake_payments(employees)
    generate_data(payments)
