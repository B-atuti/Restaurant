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

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    star_rating = Column(Integer)
    
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))

    customer = relationship('Customer', back_populates='reviews')
    restaurant = relationship('Restaurant', back_populates='reviews')