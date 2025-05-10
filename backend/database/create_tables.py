
from backend.database.connection import engine
from backend.database.base_class import Base
from backend.models import *  # importa todo para que Base los registre

def create_all_tables():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_all_tables()
    print("✅ Tablas creadas exitosamente.")
