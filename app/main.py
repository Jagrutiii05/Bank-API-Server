print("Starting FastAPI app...")

from fastapi import FastAPI
from app.routers import bank

# Initialize FastAPI app
app = FastAPI(debug=True)

# Include routes
app.include_router(bank.api)