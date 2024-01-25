from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///my_db.sql", echo=True)
Session = sessionmaker(engine,)

from .models import (Base)

def create_all(engine=engine):
    Base.metadata.create_all(engine)