from sqlalchemy import create_engine, Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class City(Base):
    __tablename__ = 'cities'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    
    weather = relationship('Weather', back_populates='city', cascade="all, delete-orphan")
    forecasts = relationship('Forecast', back_populates='city', cascade="all, delete-orphan")

class Weather(Base):
    __tablename__ = 'weather'
     
    city_id = Column(Integer, ForeignKey('cities.id'), primary_key=True)
    date = Column(Date, primary_key=True)
    temperature = Column(Float, nullable=False)
    description = Column(String, nullable=False)
    
    city = relationship('City', back_populates='weather')

class Forecast(Base):
    __tablename__ = 'forecasts'
    
    id = Column(Integer, primary_key=True)
    city_id = Column(Integer, ForeignKey('cities.id'), nullable=False)
    date = Column(Date, nullable=False)
    forecast = Column(String, nullable=False)
    
    city = relationship('City', back_populates='forecasts')

DATABASE_URL = 'sqlite:///weather.db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
