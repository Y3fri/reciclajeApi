from config.database import Base
from sqlalchemy import Column,Integer,String,Float
from sqlalchemy.orm import relationship

class Sso_rol(Base):
    __tablename__ = "sso_rol"

    rol_id = Column(Integer, primary_key=True)
    rol_nombre = Column(String(50))

    sso_usuario = relationship("Sso_usuario", back_populates="sso_rol")
