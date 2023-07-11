import .database as db


class BalanceRepository():

    def __init__(self, session) -> None:
        self.session = session

    def get_all(self):
        db_balances = self.session.query(db.Balance)
        return [
            Balance(
                id=db_balance.id, value=db_balance.value
            ) for db_balance in db_balances
        ]
