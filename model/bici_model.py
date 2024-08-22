from sqlalchemy import Column, Integer, String, Boolean
from config.database import base

class Bicicleta(base):
    __tablename__ = "bicicleta"

    id_bici = Column(Integer, primary_key=True, index=True)
    modelo = Column(String(50), nullable=True)
    disponible = Column(Boolean, default=True)