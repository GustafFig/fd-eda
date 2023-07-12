from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, HTTPException
from getdb import get_db
from balance.crud import get_by_id
from balance.entity import Balance

router = APIRouter(
    prefix="/balances",
    tags=["balances"],
    # TODO: put responses dict
)


@router.get("/{balance_id}", response_model=Balance)
def get_balances(balance_id: str, db: Session = Depends(get_db)):
    #  TODO: add a container depency injection
    db_balance = get_by_id(db, balance_id)
    if db_balance is None:
        raise HTTPException(status_code=404, detail="Balance not found")
    return db_balance
