from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from model import Phone, User

engine = create_engine('sqlite:///tembici-test.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()

Base.metadata.create_all(engine)

session = Session()

users = []

users.append(User("Guilherme Pontes", "guilherme.pontes@gmail.com"))
users.append(User("Juca Pereira", "juca.pereira@gmail.com"))
users[0].phones = [Phone('992139309', '11')]
users[1].phones = [Phone('56146882', '11')]

for user in users:
    session.add(user)

session.commit()
session.close()
