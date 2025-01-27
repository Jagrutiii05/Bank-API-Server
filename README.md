# FastAPI Bank & Branch API
This is a simple FastAPI-based application that provides an API to fetch bank details and branch information using IFSC codes. The application is connected to a SQLite database, which is populated from a CSV file containing bank and branch details.

## Overview
This project provides a RESTful API to access data about banks and branches in India. The database is populated from a CSV file, and the API provides endpoints to get:
- A list of all banks.
- Branch details using an IFSC code.
The app uses the FastAPI framework for the backend and SQLAlchemy for database management.

## Features
  - **GET /banks**: Fetches a list of all banks.
  - **GET /branches/{ifsc}**: Fetches branch details using the IFSC code.

### Run the Application

To start the FastAPI app, run the `run.py` script:

```bash
python run.py
```

Time taken to complete this assignment: 3 hours
