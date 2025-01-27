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
        port = int(os.getenv("PORT", 8000))
        uvicorn.run(app, host="0.0.0.0", port=port)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running a command: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")