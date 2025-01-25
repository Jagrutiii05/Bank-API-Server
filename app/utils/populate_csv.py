import os
import pandas as pd
from app.model import Base, Bank, Branch
from app.database import engine, SessionLocal
from dotenv import load_dotenv

def populate_database():
    # Load the CSV file
    csv_file = os.getenv('CSV_FILE_PATH')
    if not csv_file:
        raise ValueError("CSV_FILE_PATH environment variable is not set")

    df = pd.read_csv(csv_file)

    # Create a session to interact with the database
    session = SessionLocal()

    # Iterate over the dataframe to insert data into the Bank and Branch tables
    for _, row in df.iterrows():
        try:
            # Check if the bank already exists in the database
            bank = session.query(Bank).filter(Bank.name == row['bank_name']).first()

            if not bank:
                # Create a new bank if it doesn't exist
                bank = Bank(name=row['bank_name'])
                session.add(bank)
                session.commit()

            # Check if the branch already exists by its IFSC code
            branch = session.query(Branch).filter(Branch.ifsc == row['ifsc']).first()

            if not branch:
                # Create a new branch and associate it with the bank if it doesn't exist
                branch = Branch(
                    branch=row['branch'],
                    ifsc=row['ifsc'],
                    bank_id=bank.id,
                    city=row['city'],
                    district=row['district'],
                    state=row['state']
                )
                session.add(branch)
            else:
                print(f"Branch with IFSC {row['ifsc']} already exists. Skipping.")

        except Exception as e:
            # Rollback the transaction in case of an error
            session.rollback()
            print(f"Error processing row: {row.to_dict()} - {e}")

    # Commit the transaction for all branches
    try:
        session.commit()
        print("Data loaded successfully!")
    except Exception as e:
        session.rollback()
        print(f"Error during final commit: {e}")

    # Close the session
    session.close()

if __name__ == "__main__":
    # Ensure the schema exists
    Base.metadata.create_all(bind=engine)

    # Populate the database
    populate_database()