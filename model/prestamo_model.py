from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from config.database import base
from datetime import datetime


class Prestamo(base):
    __tablename__ = "prestamo"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id_documento"), nullable=False)
    bicicleta_id = Column(Integer, ForeignKey("bicicleta.id_bici"), nullable=False)
    fecha_prestamo = Column(DateTime, default=datetime.now())
    fecha_devolucion = Column(DateTime, nullable=True)

    usuario = relationship("Usuario_model")
    bicicleta = relationship("Bicicleta")