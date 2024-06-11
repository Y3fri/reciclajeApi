from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from config.database import Base
from datetime import datetime

class UserCliSession(Base):
    __tablename__ = "userclisession"

    ses_id = Column(Integer, primary_key=True, autoincrement=True)
    ses_idcliente = Column(Integer, ForeignKey("sso_cliente.cli_id"), nullable=False)    
    ses_token = Column(String(255))
    ses_expiration_timestamp = Column(DateTime)
    ses_created_at = Column(DateTime, default=datetime.utcnow)

    sso_cliente = relationship("Sso_cliente", back_populates="userclisession")
