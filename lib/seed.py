from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review

def seed_database();
    engine = create_engine('sqlite:///restaurant.db')
    Session = sessionmaker(bind=engine)
    sessiom = Session

    fake = Faker()

    customers = []
    for _ in range(10):
        customer = Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )
        session.add(customer)
        customers.append(customer)    
    