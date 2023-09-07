from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review

def main():
    engine = create_engine('sqlite:///restaurant.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    print("All Restaurants:")
    restaurants = session.query(Restaurant).all()
    for restaurant in restaurants:
        print(f"{restaurant.name} - ${restaurant.price:.2f}")

    print("\nAll Customers:")
    customers = session.query(Customer).all()
    for customer in customers:
        print(f"{customer.first_name} {customer.last_name}")

    session.close()

if __name__ == '__main__':
    main()
