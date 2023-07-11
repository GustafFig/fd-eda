from src.main import app
from sqlalchemy import Session
from fastapi import Depends
from src.__seedwork__.getdb import get_db


@app.get("/balances")
def get_balances(db: Session = Depends(get_db)):
    return