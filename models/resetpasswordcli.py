from config.database import Base
from sqlalchemy import Column,Integer,String,Float,DateTime
from sqlalchemy.orm import relationship

class Resetpasswordcli(Base):
    __tablename__="resetpasswordcli"

    resp_id = Column(Integer, primary_key = True)
    resp_correo=Column(String(80))
    resp_code=Column(String(6))
    resp_expiration= Column((DateTime))