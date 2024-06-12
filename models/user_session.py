from sqlalchemy import Column, Integer,Boolean, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from config.database import Base
from datetime import datetime

class UserSession(Base):
    __tablename__ = "usersession"

    uses_id = Column(Integer, primary_key=True, autoincrement=True)
    uses_iduser = Column(Integer, ForeignKey("sso_usuario.usu_id"), nullable=False)    
    uses_token = Column(String(255))
    uses_expiration_timestamp = Column(DateTime)
    uses_created_at = Column(DateTime, default=datetime.utcnow)
    uses_active = Column(Boolean)

    sso_usuario = relationship("Sso_usuario", back_populates="usersession")
