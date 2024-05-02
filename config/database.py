# En el archivo config/database.py


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote
from sqlalchemy.ext.declarative import declarative_base

#password = quote("Y3f3r#@+")
#mysql_file_name = f"mysql+mysqlconnector://root:{password}@localhost:3306/reciclarDB"

password = quote("OSxJdcDDSoiukXLnuF4k")
mysql_file_name = f"mysql+mysqlconnector://uy5eflvvfga7xrsj:{password}@bas7ovxw2tksfkjqhjum-mysql.services.clever-cloud.com:3306/bas7ovxw2tksfkjqhjum"

engine = create_engine(mysql_file_name, echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

