from sqlalchemy import Column, Integer, Boolean, DECIMAL, DATE, TIME, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class Sso_recogida(Base):
    __tablename__ = "sso_recogida"

    sreg_id = Column(Integer, primary_key=True, autoincrement=True)
    sreg_idcliente = Column(Integer, ForeignKey("sso_cliente.cli_id"), nullable=False)
    sreg_idestado = Column(Integer, ForeignKey("estado.est_id"), nullable=False)
    sreg_idrecogida = Column(Integer, ForeignKey("recogida.reg_id"), nullable=False)
    sreg_idtrabajador = Column(Integer, ForeignKey("sso_usuario.usu_id"), nullable=False)
    sreg_puntos = Column(Integer)
    sreg_peso = Column(DECIMAL(10, 6))
    sreg_fecha = Column(DATE)
    sreg_hora1 = Column(TIME)
    sreg_hora2 = Column(TIME)
    sreg_asignacion = Column(Boolean)


    sso_cliente = relationship("Sso_cliente", back_populates="sso_recogida")
    estado = relationship("Estado", back_populates="sso_recogida")
    recogida = relationship("Recogida", back_populates="sso_recogida")
    sso_usuario = relationship("Sso_usuario", back_populates="sso_recogida")
