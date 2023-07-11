import sqlalchemy as sa


class Balance(sa.Table):
    id = sa.Column(sa.UUID, primary_key=True)
    value = sa.Column(sa.BigInteger, nullable=False, default=0, description="The account value in cents.")
