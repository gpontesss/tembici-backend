# User Object Relational Mapper

from datetime import date
from uuid import uuid4
from sqlalchemy import Column, String, Date
from sqlalchemy.orm import relationship
from .phone import Phone
from server import Base

class User(Base):
    __tablename__ = 'users'

    uuid = Column(String(32), primary_key=True)
    name = Column(String)
    email = Column(String)
    creation_date = Column(Date)
    update_date = Column(Date)
    phones = relationship("Phone")

    def __init__(self, name, email):
        self.uuid = uuid4().hex
        self.name = name
        self.email = email
        self.creation_date = date.today()
        self.update_date = date.today()