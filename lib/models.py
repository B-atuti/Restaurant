# models.py

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_keys=True)
    name = Column(String, nullable=False)
    price = Column(Integer)

    reviews = relationship('Review', back_populates='restaurant')
    customer = relationship('Customer', secondary='reviews')

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer)

    reviews = relationship('Review', back_populates='restaurant')
    customer = relationship('Customer', secondary='reviews')
    