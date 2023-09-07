# models.py

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)

    # Define the relationship with reviews
    reviews = relationship('Review', back_populates='customer', overlaps="customers")

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    price = Column(Integer, nullable=False)

    # Define the relationship with reviews
    reviews = relationship('Review', back_populates='restaurant', overlaps="restaurants")

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(255), nullable=False)
    star_rating = Column(Integer, nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))

    # Define the relationships with customer and restaurant
    customer = relationship('Customer', back_populates='reviews', overlaps="customers")
    restaurant = relationship('Restaurant', back_populates='reviews', overlaps="restaurants")