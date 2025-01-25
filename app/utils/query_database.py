from sqlalchemy import create_engine, inspect

from app.database import SessionLocal
from app.model import Bank

# Create an engine to connect to the database
engine = create_engine('sqlite:///./data/new_test.db')

# Inspect the database
inspector = inspect(engine)

# Get the list of tables
tables = inspector.get_table_names()
print("Tables:", tables)

# Get column information for the 'banks' table
columns = inspector.get_columns('banks')
print("Columns in 'banks' table:", columns)

db = SessionLocal()
banks = db.query(Bank).all()
print("Banks:", banks)