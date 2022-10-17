from datetime import date
import time
from models import Payment


def employees_and_payments():
    employee_list = []
    for payment in Payment.query.filter(Payment.payment_date>date(2022,6,11)):
        employee_list.append(f"{payment.employee.companies.name} - {payment.employee.name} - {payment.ammount}")

    return employee_list


if __name__ == "__main__":

    start = time.perf_counter()

    for _ in range(10):
        employees_and_payments()
    print(f"employees_and_payments {time.perf_counter() - start}")