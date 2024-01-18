from config.database import Base
from sqlalchemy import Column,Integer,String,Float
from sqlalchemy.orm import relationship

class Estado(Base):
    __tablename__="estado"

    est_id = Column(Integer, primary_key = True)
    est_nombre=Column(String(30))

    sso_cliente = relationship("Sso_cliente", back_populates="estado")
    sso_usuario = relationship("Sso_usuario", back_populates="estado")
    sso_recogida = relationship("Sso_recogida", back_populates="estado")