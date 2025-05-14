from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.database.base_class import Base
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Crear motor de base de datos
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)

# Crear sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependencia para obtener sesión en FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

