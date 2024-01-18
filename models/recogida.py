from sqlalchemy import Column, Integer, Boolean, DECIMAL, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class Recogida(Base):
    __tablename__ = "recogida"

    reg_id = Column(Integer, primary_key=True, autoincrement=True)
    reg_idcomuna = Column(Integer, ForeignKey("comuna.com_id"), nullable=False)
    reg_plastico = Column(Boolean)
    reg_papel = Column(Boolean)
    reg_carton = Column(Boolean)
    reg_metal = Column(Boolean)
    reg_vidrio = Column(Boolean)
    reg_ubicacion_lag = Column(DECIMAL(10, 6))
    reg_ubicacion_log = Column(DECIMAL(10, 6))
    reg_numero = Column(String(30))

    comuna = relationship("Comuna", back_populates="recogida")
    sso_recogida = relationship("Sso_recogida", back_populates="recogida")
