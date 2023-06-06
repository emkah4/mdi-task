from sqlalchemy import Column, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Weather(Base):
    __tablename__ = 'weather'

    city = Column(String, primary_key=True)
    date = Column(Date, primary_key=True)
    min_temp = Column(Float)
    max_temp = Column(Float)
    conditions = Column(String)
