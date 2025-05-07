from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=True)
    password: Mapped[str] = mapped_column(String(16), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    favorites: Mapped[list['PeopleFavorites']] = relationship(back_populates='user', cascade='all, delete-orphan')
    planetfavorites: Mapped[list["PlanetFavorites"]] = relationship(back_populates = "user", cascade='all, delete-orphan')
    starshipsfavorites:Mapped[list ["StarshipsFavorites"]] = relationship(back_populates = "user", cascade='all, delete-orphan')


class People(db.Model):
    __tablename__ = 'people'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25), nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    height: Mapped[int] = mapped_column(Integer, nullable=True)
    favorite_by: Mapped[list['PeopleFavorites']] = relationship(back_populates='people', cascade='all, delete-orphan')

class Planets (db.Model):
    __tablename__= "planets"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25), nullable=False)
    climate: Mapped[str] = mapped_column(String(25), nullable=False)
    orbit: Mapped[str] = mapped_column(String(25), nullable=False)
    favorite_by: Mapped[list['PlanetFavorites']] = relationship(back_populates='planet', cascade='all, delete-orphan')

class Starships (db.Model):
    __tablename__= "starships"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25), nullable=False)
    consumables: Mapped[str] =  mapped_column(String(25), nullable=False)
    color: Mapped[str] =  mapped_column(String(25), nullable=False)
    favorite_by: Mapped[list['StarshipsFavorites']] = relationship(back_populates='starship', cascade='all, delete-orphan')


class PeopleFavorites(db.Model):
    __tablename__ = 'people_favorites'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user: Mapped['User'] = relationship(back_populates='favorites')
    people_id: Mapped[int] = mapped_column(ForeignKey('people.id'))
    people: Mapped['People'] = relationship(back_populates='favorite_by')

class PlanetFavorites(db.Model):
   __tablename__ = 'planet_favorites'
   id: Mapped[int] = mapped_column(primary_key=True)
   user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
   user: Mapped["User"] = relationship(back_populates = "planetfavorites")
   planets_id: Mapped[int] = mapped_column(ForeignKey("planets.id"))
   planet: Mapped[Planets] = relationship(back_populates = "favorite_by")

class StarshipsFavorites(db.Model):
    __tablename__ = "starships_favorites"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates = "starshipsfavorites")
    starships_id: Mapped[int] = mapped_column(ForeignKey("starships.id"))
    starship: Mapped[Starships] = relationship(back_populates = "favorite_by")

   
   

