from config.database import base
from sqlalchemy import Column, Integer, String 
from sqlalchemy.ext.declarative import declarative_base


base=declarative_base()

class Usuario(base):
        __tablename__ = "usuarios"

        id=Column(Integer,primary_key=True, index=True)
        nombre=Column(String(50), index=True,nullable=True)
        email=Column(String(50), index=True, nullable=True)
        telefono=Column(int, index=True, nullable=True)
        direccion=Column(String(70),index=True,nullable=True)