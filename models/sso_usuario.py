from sqlalchemy import Column, Integer, Boolean, DECIMAL, DATETIME, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class Sso_usuario(Base):
    __tablename__ = "sso_usuario"

    usu_id = Column(Integer, primary_key=True, autoincrement=True)
    usu_estado = Column(Integer, ForeignKey("estado.est_id"), nullable=False)    
    usu_rol = Column(Integer, ForeignKey("sso_rol.rol_id"), nullable=False) 
    usu_correo = Column(String(50))
    usu_documento = Column(String(20))
    usu_nombres = Column(String(50))
    usu_apellidos = Column(String(50))
    usu_nickname = Column(String(50),unique=True, index=True)
    usu_clave = Column(String(255))    
    usu_latitud = Column(DECIMAL(10, 6))
    usu_longitud = Column(DECIMAL(10, 6))
    usu_fechahora = Column(DATETIME)
    
    estado = relationship("Estado", back_populates="sso_usuario")
    sso_rol = relationship("Sso_rol", back_populates="sso_usuario")
    sso_recogida = relationship("Sso_recogida", back_populates="sso_usuario")
    usersession = relationship("UserSession", back_populates="sso_usuario")
    