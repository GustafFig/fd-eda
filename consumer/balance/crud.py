from balance.model import Account as db_Account
from .schemas import Account
from sqlalchemy.orm import Session


def get_by_id(db: Session, id) -> Account:
    return db.query(db_Account).filter(db_Account.id == id).first()


def update_or_save(db: Session, account: Account) -> None:
    db_account = get_by_id(db, account.id)
    if db_account is None:
        db_account = db_Account(id=account.id, value=account.value)
        db.add(db_account)
    else:
        db_account.value = account.value

    db.commit()
    db.refresh(db_account)
