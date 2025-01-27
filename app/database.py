from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# DATABASE_URL = "sqlite:///./data/new_test.db"

# os.makedirs(os.path.dirname(DATABASE_URL.split("///")[1]), exist_ok=True)

# Get the absolute path of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construct the SQLite database path relative to the project directory
DATABASE_PATH = os.path.join(BASE_DIR, "../data/new_test.db")

# Define the database URL
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"


engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
