from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review

def seed_database():
    engine = create_engine('sqlite:///restaurant.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    fake = Faker()

    customers = []
    for _ in range(10):
        customer = Customer(
            name=fake.name() 
        )
        session.add(customer)
        customers.append(customer)    
    
    restaurants = []
    for _ in range(10):
        restaurant = Restaurant(
            name=fake.company(),
            price=random.randint(4000, 10000)
        )
        session.add(restaurant)
        restaurants.append(restaurant)

    for restaurant in restaurants:
        for _ in range(random.randint(1, 10)):
            customer = random.choice(customers)
            review = Review(
                description=fake.sentence(),
                star_rating=random.randint(1, 10)
            )
            restaurant.reviews.append(review)
            customer.reviews.append(review)
    
    session.commit()
    session.close()

if __name__ == '__main__':
    seed_database()
