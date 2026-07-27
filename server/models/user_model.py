from sqlalchemy import Boolean, Index, Integer, String, sql
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.database import Base
from models.associations import user_matches
from models.match_model import Match
from models.mixins import Name, TimeStamps


class User(Base, Name, TimeStamps):
    __table_args__ = (
        Index("ix_users_email", "email"),
        Index("ix_users_username", "username"),
    )

    username: Mapped[str] = mapped_column(String(100), nullable=False, unique=False)

    url: Mapped[str] = mapped_column(String(200), nullable=False, unique=False)

    steam_id: Mapped[str] = mapped_column(String(200), nullable=False, unique=True)

    steam_auth_code: Mapped[str] = mapped_column(String(100), nullable=True)

    recent_game_code: Mapped[str] = mapped_column(String(100), nullable=True)

    premier_rating: Mapped[int] = mapped_column(Integer, nullable=False)

    avatar: Mapped[str] = mapped_column(String(100), nullable=True)

    tracking: Mapped[bool] = mapped_column(
        Boolean, nullable=False, server_default=sql.false()
    )

    matches: Mapped[list["Match"]] = relationship(
        secondary=user_matches, back_populates="players"
    )
