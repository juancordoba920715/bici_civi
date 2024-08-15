from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from config.database import Base
from datetime import datetime


class Prestamo(Base):
    __tablename__ = "prestamo"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id"), nullable=False)
    bicicleta_id = Column(Integer, ForeignKey("bicicleta.id"), nullable=False)
    fecha_prestamo = Column(DateTime, default=datetime.now())
    fecha_devolucion = Column(DateTime, nullable=True)

    usuario = relationship("Usuario")
    bicicleta = relationship("Bicicleta")