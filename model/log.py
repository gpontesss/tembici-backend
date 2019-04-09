import datetime, jwt
from uuid import uuid4
from sqlalchemy import Column, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship
from model import User
from server import Base

class Log(Base):
    __tablename__ = 'log'

    uuid = Column(String(32), primary_key=True)
    user_uuid = Column(String(32), ForeignKey('users.uuid'))
    date = Column(DateTime)
    token = Column(String)
    
    def __init__(self, user, token):
        self.uuid = uuid4().hex
        self.user_uuid = user.uuid
        self.date = datetime.datetime.today()
        self.token = token
    
    @staticmethod
    def generate_token(payload, secret, algorithm='HS256'):
        return jwt.encode(payload, secret, algorithm=algorithm)

    def verify_token(token, secret, algorithm='HS256'):
        return jwt.decode(token, secret, algorithm=algorithm)


