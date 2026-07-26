from sqlalchemy import Column, ForeignKey, Table

from database.database import Base

user_wins = Table(
    "user_wins",
    Base.metadata,
    Column("user_id", ForeignKey("user.id"), primary_key=True),
    Column("match_id", ForeignKey("match.id"), primary_key=True),
)

user_losses = Table(
    "user_losses",
    Base.metadata,
    Column("user_id", ForeignKey("user.id"), primary_key=True),
    Column("match_id", ForeignKey("match.id"), primary_key=True),
)
