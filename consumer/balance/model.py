from database import Base

import sqlalchemy as sa


class Account(Base):
    __tablename__ = "accounts"

    id = sa.Column(sa.String, primary_key=True)
    value = sa.Column(
        sa.BigInteger,
        nullable=False,
        default=0,
    )
