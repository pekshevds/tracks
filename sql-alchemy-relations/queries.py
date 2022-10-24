from importlib import import_module
import time

from db import db_session
from models import Company, Employee, Project


def emplyees_by_company(company_name):
    company = Company.query.filter(Company.name==company_name).first()
    employee_list = []
    if company:
        for employee in Employee.query.filter(Employee.company_id==company.id):
            employee_list.append(f"{company.name} - {employee.name}")
    return employee_list


def emplyees_by_company_joined(company_name):
    query = db_session.query(Employee, Company).join(
        Company, Employee.company_id==Company.id
    ).filter(Company.name==company_name)
    
    employee_list = []
    for employee,company in query:
            employee_list.append(f"{company.name} - {employee.name}")
    return employee_list


def emplyees_by_company_relation(company_name):
    company = Company.query.filter(Company.name==company_name).first()
    employee_list = []
    if company:
        for employee in company.employees:
            employee_list.append(f"{company.name} - {employee.name}")
    return employee_list


def company_projects_employees(company_name):
    query = Project.query.join(Project.id, Project.employees).filter(Company.name == company_name)
    for project in query:

        print('-' * 20)
        print(project.name)
        for project_employee in project.employees:
            delta = (project_employee.date_end - project_employee.date_start).days
            print(f"{project_employee.employee.name} -- {delta}")



if __name__ == "__main__":
    """start = time.perf_counter()

    for _ in range(10000):
        emplyees_by_company(company_name="ТЭК Мосэнерго")
    print(f"emplyees_by_company {time.perf_counter() - start}")

   start = time.perf_counter()

    for _ in range(10000):
        emplyees_by_company_joined(company_name="ТЭК Мосэнерго")
    print(f"emplyees_by_company_joined {time.perf_counter() - start}")"""    

    """start = time.perf_counter()

    for _ in range(10000):
        emplyees_by_company_relation(company_name="ТЭК Мосэнерго")
    print(f"emplyees_by_company_relation {time.perf_counter() - start}")"""

    company_projects_employees("ГК Ташир")