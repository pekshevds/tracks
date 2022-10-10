import csv
from datetime import datetime
from db import db_session
from models import Salary


def read_csv(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        fields = ["name", "city", "address", 
                "company", "job", "phone_number", 
                "email", "date_of_birth", "salary"]

        reader = csv.DictReader(file, fields, delimiter=";")
        for row in reader:
            save_salary_data(row)

        
def save_salary_data(row):
    salary = Salary(name=row["name"], city=row["city"], address=row["address"], 
                company=row["company"], job=row["job"], phone_number=row["phone_number"], 
                email=row["email"], date_of_birth=datetime.strptime(row["date_of_birth"], "%Y-%m-%d"), salary=int(row["salary"]))

    db_session.add(salary)
    db_session.commit()

if __name__ == "__main__":
    read_csv("salary.csv")