from sqlalchemy import Column, Integer, String, Boolean
from config.database import Base

class Bicicleta(Base):
    __tablename__ = "bicicleta"

    id = Column(Integer, primary_key=True, index=True)
    modelo = Column(String, nullable=True)
    disponible = Column(Boolean, default=True)