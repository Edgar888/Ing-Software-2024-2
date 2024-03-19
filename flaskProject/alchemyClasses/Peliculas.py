from sqlalchemy import Column, Integer, String

from alchemyClasses import db


class Peliculas (db.Model):

    __tablename__ = 'peliculas'
    id_alumno = Column(Integer, primary_key=True)
    nombre = Column(String(45))
    ap_pat = Column(String(45))
    ap_mat = Column(String(45), nullable=True)
    num_cta = Column(Integer)
    password = Column(String(64), nullable=True)

    def __init__(self, nombre, inventario, genero=None, duracion=None):
        self.nombre = nombre
        self.ap_pat = apPat
        self.ap_mat = apMat
        self.num_cta = numCta
        self.password = password

    def __str__(self):
        return f'Nombre:{self.nombre}'
