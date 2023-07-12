from database import Base

import sqlalchemy as sa


class Balance(Base):
    __tablename__ = "balances"

    id = sa.Column(sa.String, primary_key=True)
    value = sa.Column(
        sa.BigInteger,
        nullable=False,
        default=0,
    )
