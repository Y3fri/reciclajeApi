from sqlalchemy import Column, Integer, DECIMAL, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class Producto(Base):
    __tablename__ = "producto"

    pro_id = Column(Integer, primary_key=True, autoincrement=True)
    pro_empresa = Column(Integer, ForeignKey("empresa.inf_id"), nullable=False)
    pro_estado = Column(Integer, ForeignKey("estado.est_id"), nullable=False)
    pro_foto = Column(String(500))
    pro_nombre = Column(String(50))
    pro_puntos = Column(Integer)
    pro_cantidad = Column(Integer)
    
    empresa = relationship("Empresa", back_populates="productos")
    estado = relationship("Estado", back_populates="productos")
    cliente_producto = relationship("Cliente_producto", back_populates="productos")
    
