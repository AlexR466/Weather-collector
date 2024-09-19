import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, JSON, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class City(Base):
    """Модель города"""
    __tablename__ = 'cities'
    city_id = Column(Integer, primary_key=True)
    city_name = Column(String(50), unique=True)


class Weather(Base):
    """Модель погоды"""
    __tablename__ = 'weather_data'
    id = Column(Integer, primary_key=True)
    weather_in_city = Column(JSON)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    city_id = Column(Integer, ForeignKey(City.city_id))
