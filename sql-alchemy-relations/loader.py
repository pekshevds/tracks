import csv
from db import db_session
from datetime import datetime
from models import Company, Employee, Payment


def read_csv(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        fields = ["company", "city", "address", "phone_company", "name", "job",
                "phone_person", "email", "date_of_birth", "payment_date", "ammount"]

        reader = csv.DictReader(file, fields, delimiter=";")
        payments_data = []
        for row in reader:
            payments_data.append(row)
        return payments_data


def save_companies(data):
    processed = []
    unique_companies = []
    for row in data:
        if row['company'] not in processed:
            company = {
                'name': row['company'],
                'city': row['city'],
                'address': row['address'],
                'phone': row['phone_company']
            }
            unique_companies.append(company)
            processed.append(company['name'])
    
    db_session.bulk_insert_mappings(Company, unique_companies, return_defaults=True)
    db_session.commit()
    return unique_companies


def get_company_by_name(companies, company_name):
    for company in companies:
        if company['name'] == company_name:
            return company['id']


def save_employees(data, companies):
    processed = []
    unique_employees = []
    for row in data:
        if row['phone_person'] not in processed:
            employee = {
                'name': row['name'],
                'job': row['job'],
                'email': row['email'],
                'phone': row['phone_person'],
                'date_of_birth': datetime.strptime(row['date_of_birth'], "%Y-%m-%d"),
                'company_id': get_company_by_name(companies, row['company'])
            }
            unique_employees.append(employee)
            processed.append(employee['phone'])
    
    db_session.bulk_insert_mappings(Employee, unique_employees, return_defaults=True)
    db_session.commit()
    return unique_employees
            

def get_employee_by_name(employees, employee_phone):
    for employee in employees:
        if employee['phone'] == employee_phone:
            return employee['id']


def save_payments(data, employees):
    payments = []
    for row in data:
        payment = {
            'payment_date': datetime.strptime(row['payment_date'], "%Y-%m-%d"),
            'ammount': row['ammount'],
            'employee_id': get_employee_by_name(employees, row['phone_person'])
        }
        payments.append(payment)
    db_session.bulk_insert_mappings(Payment, payments)
    db_session.commit()    


if __name__ == "__main__":
    all_data = read_csv("salary.csv")
    companies = save_companies(all_data)
    employees = save_employees(all_data, companies)
    save_payments(all_data, employees)
    