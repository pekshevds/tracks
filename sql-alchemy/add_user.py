from db import db_session
from models import User


first_user = User(name='Григорий Дрозд', salary=1500, email='drozd@example.com')
db_session.add(first_user)
db_session.commit()