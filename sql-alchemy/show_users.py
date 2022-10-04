from models import User

for user in User.query.all():
    print(
    f"""    Пользователь: {user.name}
    Зарплата: {user.salary}
    Почта: {user.email}
    """)