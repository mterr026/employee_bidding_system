from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from SQL_app2.database import Base

class Employee(Base):
    __tablename__ = "employee"

    EIN = Column(Integer, primary_key=True, nullable=False, unique=True)
    fname = Column(String, nullable=False)
    lname = Column(String, nullable=False)
    startDate = Column(Date, nullable=False)
    role = Column(String, nullable=False)
    securityQuestion = Column(String, nullable=False)
    securityAnswer = Column(String, nullable=False)
    password = Column(String, nullable=False)