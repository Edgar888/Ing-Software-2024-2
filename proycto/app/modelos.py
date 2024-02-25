from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    idUsuario = Column(Integer, primary_key=True)
    nombre = Column(String(200), nullable=False)
    apellido = Column(String(200), nullable=False)
    email = Column(String(500), nullable=True)

class Pelicula(Base):
    __tablename__ = 'peliculas'
    
    idPelicula = Column(Integer, primary_key=True)
    nombre = Column(String(200), nullable=False)
    genero = Column(String(45), nullable=True)
    duracion = Column(Integer, nullable=True)

class Rentar(Base):
    __tablename__ = 'rentar'
    
    idRentar = Column(Integer, primary_key=True)
    idUsuario = Column(Integer, nullable=False)
    idPelicula = Column(Integer, nullable=False)
    fecha_renta = Column(Date, nullable=False)
    dias_de_renta = Column(Integer, nullable=True)
    estatus = Column(Integer, nullable=True)

