from sqlalchemy import Column, Integer, String, Boolean, func, Table
from sqlalchemy.sql.sqltypes import Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname  = Column(String(50), nullable=False)
    phone_number = Column(String(12), nullable=False)
    email = Column(String(100), nullable=False)
    birthday = Column(Date, nullable=False)