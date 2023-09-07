# create_tables.py

from sqlalchemy import create_engine
from models import Base

def create_database():
    engine = create_engine('sqlite:///restaurant.db')
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    create_database()
