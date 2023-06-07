from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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

class DatabaseWriter:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def write_data(self, weather_data):
        for city, records in weather_data.items():
            for record in records:
                weather_record = Weather(
                    city=city,
                    date=record['date'],
                    min_temp=record['min'],
                    max_temp=record['max'],
                    conditions=record['condition']
                )
                self.session.add(weather_record)
        self.session.commit()
        self.session.close()
