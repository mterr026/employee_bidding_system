from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from SQL_app2.database import Base
from auth.model import Employee

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)

class Bid(Base):
    __tablename__ = "bid"

    bidNum = Column(Integer, primary_key=True, nullable=False, unique=True) 
    status = Column(String, nullable=False)
    description = Column(String, nullable=False)
    postDate = Column(Date, nullable=False)
    closeDate = Column(Date, nullable=False)
    awarded = Column(String, nullable=True, unique=True)
    daysOff = Column(String, nullable=False)
    hours = Column(String, nullable=False)



class Postings(Base):
    __tablename__ = "postings"

    postID = Column(Integer, primary_key=True)
    EIN = Column(Integer, ForeignKey(Employee.EIN))
    bidNum = Column(Integer, ForeignKey(Bid.bidNum))
    requestDate = Column(Date, nullable=False)
    awardDate = Column(Date, nullable=True)
    awarded = Column(Date)


employee = relationship("Employee", back_populates="postings")