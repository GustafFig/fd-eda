from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, HTTPException
from getdb import get_db
from balance.crud import get_by_id
from balance.schemas import Account


router = APIRouter(
    prefix="/balances",
    tags=["balances"],
    # TODO: put responses dict
)


@router.get("/{account_id}", response_model=Account)
def get_balances(account_id: str, db: Session = Depends(get_db)):
    #  TODO: add a container depency injection
    db_balance = get_by_id(db, account_id)
    if db_balance is None:
        raise HTTPException(status_code=404, detail="Balance not found")
    return db_balance
