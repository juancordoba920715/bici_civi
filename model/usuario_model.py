from config.database import base
from sqlalchemy import Column, Integer, String 

class Usuario_model(base):
        __tablename__ = "usuario"

        id_documento=Column(Integer,primary_key=True, index=True)
        nombre=Column(String(50), index=True,nullable=True)
        email=Column(String(50), index=True, unique=True, nullable=True)
        contrasena=Column(String(50), index=True, nullable=True)
        telefono=Column(Integer, index=True, nullable=True)
        direccion=Column(String(70),index=True,nullable=True)