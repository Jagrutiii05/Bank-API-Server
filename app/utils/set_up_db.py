import sys
import os

# Add the parent directory of 'app' to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from app.database import Base, engine
from app.utils.populate_csv import populate_database

# Create database tables
Base.metadata.create_all(bind=engine)

populate_database()

print("DB loaded...")