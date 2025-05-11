from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.database.base_class import Base
from dotenv import load_dotenv
import os

load_dotenv()  # Cargar variables del .env

DATABASE_URL = os.getenv("DATABASE_URL")

# Puedes agregar connect_args si usas SQLite
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
