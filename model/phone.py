# Phone Object Relational Mapper

from uuid import uuid4
from sqlalchemy import Column, String, ForeignKey
from server import Base

class Phone(Base):
    __tablename__ = 'phones'

    uuid = Column(String(32), primary_key=True)
    user_uuid = Column(String(32), ForeignKey('users.uuid'))
    phone = Column(String(16))
    ddd = Column(String(2))

    def __init__(self, phone, ddd):
        self.uuid = uuid4().hex
        self.phone = phone
        self.ddd = ddd

    def to_obj(self):
        return {
            'numero': self.phone,
            'ddd': self.ddd
        }