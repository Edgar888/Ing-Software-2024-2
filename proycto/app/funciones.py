from datetime import datetime, timedelta
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    idUsuario = Column(Integer, primary_key=True)
    nombre = Column(String(200), nullable=False)
    apPat = Column(String(200), nullable=False)
    apMat = Column(String(200))
    password = Column(String(64), nullable=False)
    email = Column(String(500))
    profilePicture = Column(String)
    superUser = Column(Integer)

class Pelicula(Base):
    __tablename__ = 'peliculas'
    idPelicula = Column(Integer, primary_key=True)
    nombre = Column(String(200), nullable=False)
    genero = Column(String(45))
    duracion = Column(Integer)
    inventario = Column(Integer, nullable=False, default=1)

class Rentar(Base):
    __tablename__ = 'rentar'
    idRentar = Column(Integer, primary_key=True)
    idUsuario = Column(Integer, ForeignKey('usuarios.idUsuario'))
    idPelicula = Column(Integer, ForeignKey('peliculas.idPelicula'))
    fecha_renta = Column(DateTime, nullable=False)
    dias_de_renta = Column(Integer, default=5)
    estatus = Column(Integer, default=0)

engine = create_engine('mysql+pymysql://username:password@localhost/lab_ing_software')
Session = sessionmaker(bind=engine)
session = Session()

def insertar_registros():
    # Insertar usuarios
    nuevo_usuario = Usuario(nombre='Nombre1', apPat='Apellido1', password='123456', email='usuario1@example.com')
    session.add(nuevo_usuario)

    # Insertar películas
    nueva_pelicula = Pelicula(nombre='Pelicula1', genero='Drama', duracion=120, inventario=10)
    session.add(nueva_pelicula)

    # Insertar renta
    usuario_existente = session.query(Usuario).filter_by(idUsuario=1).first()
    pelicula_existente = session.query(Pelicula).filter_by(idPelicula=1).first()
    nueva_renta = Rentar(idUsuario=usuario_existente.idUsuario, idPelicula=pelicula_existente.idPelicula, fecha_renta=datetime.now())
    session.add(nueva_renta)

    session.commit()

def filtrar_usuarios_por_apellido(apellido):
    usuarios = session.query(Usuario).filter(Usuario.apMat.like(f'%{apellido}') | Usuario.apPat.like(f'%{apellido}')).all()
    return usuarios

def cambiar_genero_pelicula(nombre_pelicula, nuevo_genero):
    pelicula = session.query(Pelicula).filter_by(nombre=nombre_pelicula).first()
    if pelicula:
        pelicula.genero = nuevo_genero
        session.commit()
    else:
        print("La película especificada no existe.")

def eliminar_rentas_antiguas():
    fecha_limite = datetime.now() - timedelta(days=3)
    rentas = session.query(Rentar).filter(Rentar.fecha_renta <= fecha_limite).all()
    for renta in rentas:
        session.delete(renta)
    session.commit()


