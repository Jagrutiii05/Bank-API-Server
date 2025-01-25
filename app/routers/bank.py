from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..model import Bank, Branch
from ..database import get_db

api = APIRouter()

@api.get("/banks")
def get_banks(db: Session = Depends(get_db)):
    """
    Fetch a list of all banks.
    """
    banks = db.query(Bank).all()
    return [{"id": bank.id, "name": bank.name} for bank in banks]

@api.get("/branches/{ifsc}")
def get_branch_by_ifsc(ifsc: str, db: Session = Depends(get_db)):
    """
    Fetch branch details by IFSC code.
    """
    branch = db.query(Branch).filter(Branch.ifsc == ifsc).first()
    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")

    return {
        "branch": branch.branch,
        "ifsc": branch.ifsc,
        "bank": {"id": branch.bank.id, "name": branch.bank.name},
        "city": branch.city,
        "district": branch.district,
        "state": branch.state,
    }

@api.get("/")
def read_root():
    return {"message": "Welcome to my app!"}

@api.get("/test")
def test_route():
    return {"message": "test This is a test route!"}