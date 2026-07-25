from sqlalchemy import Index, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.database import Base
from models.associations import user_match
from models.match_models import Match
from models.mixins import Name, TimeStamps


class User(Base, Name, TimeStamps):
    __table_args__ = (
        Index("ix_users_email", "email"),
        Index("ix_users_username", "username"),
    )

    username: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    steam_id: Mapped[str] = mapped_column(String(200), nullable=False, unique=True)

    matches: Mapped[list["Match"]] = relationship(
        secondary=user_match, back_populates="players"
    )
