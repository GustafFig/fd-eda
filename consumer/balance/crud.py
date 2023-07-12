from balance.model import Balance as db_Balance
from .entity import Balance
from sqlalchemy.orm import Session


def get_by_id(db: Session, id) -> Balance:
    return db.query(db_Balance).filter(db_Balance.id == id).first()

    # save db_balance
def save(db: Session, balance: Balance) -> None:
    db_balance = db_Balance(
        id=balance.id,
        value=balance.value
    )
    db.add(db_balance)
    db.commit()
    db.refresh(db_balance)

