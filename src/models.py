import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    classification = Column(String(50))
    planet = Column(Integer, ForeignKey('planets.id'))
    character = Column(Integer, ForeignKey('characters.id'))

class Favorite_Characters(Base):
    __tablename__ = 'favorite_characters'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.id'))
    character_id_relationship = relationship('Characters')
    user_id = Column(Integer, ForeignKey('user.id'))
    user_id_relationship = relationship('User')

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    planet = Column(Integer, ForeignKey('planets.id'))
    character = relationship(Species)

class Favorite_Films(Base):
    __tablename__ = 'favorite_films'
    id = Column(Integer, primary_key=True)
    film_id = Column(Integer, ForeignKey('films.id'))
    film_relationship = relationship('Films')
    user_id = Column(Integer, ForeignKey('user.id'))
    user_relationship = relationship('User')

class Films_species(Base):
    __tablename__ = 'films_species'
    id = Column(Integer, primary_key=True)
    film_id = Column(Integer, ForeignKey('films.id'))
    film_relationship = relationship('Films')
    species_id = Column(Integer, ForeignKey('species.id'))
    species_relationship = relationship(Species)

class Films_Characters(Base):
    __tablename__ = 'films_characters'
    id = Column(Integer, primary_key=True)
    film_id = Column(Integer, ForeignKey('films.id'))
    film_relationship = relationship('Films')
    characters_id = Column(Integer, ForeignKey('characters.id'))
    characters_relationship = relationship(Characters)

class Films(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    title = Column(String(120), unique=True)
    episode = Column(Integer, unique=True)
    director = Column(String(50))
    release_date = Column(Date)

class Favorite_Planets(Base):
    __tablename__ = 'favorite_planets'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet_relationship = relationship('Planets')
    user_id = Column(Integer, ForeignKey('user.id'))
    user_relationship = relationship('User')

class Planets_Films(Base):
    __tablename__ = 'planets_films'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet_relationship = relationship('Planets')
    films_id = Column(Integer, ForeignKey('films.id'))
    films_relationship = relationship(Films)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    rotation_period = Column(Integer)
    climate = Column(String(50))
    characters_relationship = relationship(Characters)
    species_relationship = relationship(Species)

class Favorite_Starships(Base):
    __tablename__ = 'favorite_starships'
    id = Column(Integer, primary_key=True)
    starship_id = Column(Integer, ForeignKey('starships.id'))
    starship_relationship = relationship('Starships')
    user_id = Column(Integer, ForeignKey('user.id'))
    user_relationship = relationship('User')


class Starships_Characters(Base):
    __tablename__ = 'starships_characters'
    id = Column(Integer, primary_key=True)
    starship_id = Column(Integer, ForeignKey('starships.id'))
    starship_relationship = relationship('Starships')
    characters_id = Column(Integer, ForeignKey('characters.id'))
    characters_relationship = relationship(Characters)

class Starships_Films(Base):
    __tablename__ = 'starships_films'
    id = Column(Integer, primary_key=True)
    starship_id = Column(Integer, ForeignKey('starships.id'))
    starship_relationship = relationship('Starships')
    films_id = Column(Integer, ForeignKey('films.id'))
    films_relationship = relationship(Films)

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    model = Column(String(100))

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    age = Column(Integer)
    email = Column(String(100), unique=True)
    suscription_date = Column(Date)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
