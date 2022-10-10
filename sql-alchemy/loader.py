import csv
from datetime import datetime
import time
from db import db_session
from models import Salary


def read_csv1(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        fields = ["name", "city", "address", 
                "company", "job", "phone_number", 
                "email", "date_of_birth", "salary"]

        reader = csv.DictReader(file, fields, delimiter=";")
        for row in reader:
            save_salary_data1(row)

        
def save_salary_data1(row):
    salary = Salary(name=row["name"], city=row["city"], address=row["address"], 
                company=row["company"], job=row["job"], phone_number=row["phone_number"], 
                email=row["email"], date_of_birth=datetime.strptime(row["date_of_birth"], "%Y-%m-%d"), salary=int(row["salary"]))
                #email=row["email"], date_of_birth=row["date_of_birth"], salary=row["salary"])

    db_session.add(salary)
    db_session.commit()


def read_csv2(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        fields = ["name", "city", "address", 
                "company", "job", "phone_number", 
                "email", "date_of_birth", "salary"]

        reader = csv.DictReader(file, fields, delimiter=";")
        salary_data = []
        for row in reader:
            row["date_of_birth"]=datetime.strptime(row["date_of_birth"], "%Y-%m-%d")
            row["salary"]=int(row["salary"])
            salary_data.append(row)
        
        save_salary_data2(salary_data)

        
def save_salary_data2(data: list):
    
    db_session.bulk_insert_mappings(Salary, data)
    db_session.commit()


if __name__ == "__main__":
    start = time.time()
    #read_csv1("salary.csv")
    read_csv2("salary.csv")
    print(f"Загрузка заняла {time.time() - start}")