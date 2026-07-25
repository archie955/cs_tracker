from sqlalchemy import Column, ForeignKey, Table

from database.database import Base

user_match = Table(
    "user_match",
    Base.metadata,
    Column("user_id", ForeignKey("user.id"), primary_key=True),
    Column("match_id", ForeignKey("match.id"), primary_key=True),
)
