from sqlalchemy import Column, Integer, Boolean, DECIMAL, DATE, TIME, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class Cliente_producto(Base):
    __tablename__ = "cliente_producto"

    clip_id = Column(Integer, primary_key=True, autoincrement=True)
    clip_idcliente = Column(Integer, ForeignKey("sso_cliente.cli_id"), nullable=False)
    clip_idproducto = Column(Integer, ForeignKey("producto.pro_id"), nullable=False)        
    clip_latitud = Column(DECIMAL(10, 6))
    clip_longitud = Column(DECIMAL(10, 6))
    clip_cantidad = Column(Integer)

    sso_cliente = relationship("Sso_cliente", back_populates="cliente_producto")
    productos = relationship("Producto", back_populates="cliente_producto")   
