from sqlalchemy import Column, Integer, Boolean, DECIMAL, DATE, TIME, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class Sso_cliente(Base):
    __tablename__ = "sso_cliente"

    cli_id = Column(Integer, primary_key=True, autoincrement=True)
    cli_estado = Column(Integer, ForeignKey("estado.est_id"), nullable=False)    
    cli_correo = Column(String(50))
    cli_documento = Column(String(20))
    cli_nombres = Column(String(50))
    cli_apellidos = Column(String(50))
    cli_nickname = Column(String(50))
    cli_clave = Column(String(255))
    cli_telefono = Column(String(50)) 
    cli_totalpuntos= Column(Integer) 

    estado = relationship("Estado", back_populates="sso_cliente")
    sso_recogida = relationship("Sso_recogida", back_populates="sso_cliente")
    cliente_producto = relationship("Cliente_producto", back_populates="sso_cliente")
    userclisession = relationship("UserCliSession", back_populates="sso_cliente")
    