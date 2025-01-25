# all commands combined
import os
import subprocess
from app.main import app

if __name__ == "__main__":
    try:
        # Step 1: Install required dependencies
        print("Installing dependencies from requirements.txt...")
        subprocess.check_call(["pip", "install", "-r", "requirements.txt"])

        # Step 2: Load the database
        print("Setting up the database by running set_up_db.py...")
        subprocess.check_call(["python", "app/utils/set_up_db.py"])

        # Step 3: Run the server
        print("Starting the server...")
        import uvicorn
        uvicorn.run(app, host="127.0.0.1", port=8000)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running a command: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")