# -*- coding: utf-8 -*-
"""
    model.user
    ----
    User ORM for registering users.
"""
import datetime

from uuid import uuid4
from passlib.hash import pbkdf2_sha256 as sha256

from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship

from model import Phone
from server import Base

class User(Base):
    __tablename__ = 'users'

    uuid = Column(String(32), primary_key=True)
    name = Column(String)
    email = Column(String)
    creation_date = Column(DateTime)
    update_date = Column(DateTime)
    phones = relationship("Phone")
    password = Column(String)

    def __init__(self, name, email, password):
        self.uuid = uuid4().hex
        self.name = name
        self.email = email
        self.creation_date = datetime.datetime.today()
        self.update_date = self.creation_date
        self.password = password

    """ Returns User as JSON serializable.
    """
    def to_obj(self):
        import util.db
        return {
            'nome': self.name,
            'email': self.email,
            'senha': self.password,
            'data_criacao': self.creation_date.isoformat(),
            'data_atualizacao': self.update_date.isoformat(),
            'ultimo_login': util.db.user_last_login(self.email).date.isoformat(),
            'telefones': [p.to_obj() for p in self.phones]
        }

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)