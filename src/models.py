import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer,nullable=False)
    hair_color = Column(String(50),nullable=False)
    skin_color = Column(String(50),nullable=False)
    eye_color = Column(String(50),nullable=False)
    birth_year = Column(String(50),nullable=False)
    gender = Column(String(50),nullable=False)
    home_world = Column(String(50),nullable=False)


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    rotationPeriod = Column(Integer, nullable=False)
    orbitalPeriod = Column(Integer, nullable=False)
    diameter = Column(String(250), nullable=False)
    climate = Column(String(50), nullable=False)
    gravity = Column(String(50), nullable=False)
    terrain = Column(String(50), nullable=False)
    surfaceWater = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(50), nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey(User.id))
    character_id = Column(String(50),ForeignKey(Character.id))
    planets_id = Column(String(50),ForeignKey(Planets.id))
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')