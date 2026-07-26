from sqlalchemy import DECIMAL, ForeignKey, Index, Integer
from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base
from models.mixins import Name, TimeStamps


class PlayerMatch(Base, Name, TimeStamps):
    __table_args__ = (
        Index("ix_playermatch_user_id", "user_id"),
        Index("ix_playermatch_match_id", "match_id"),
    )

    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False
    )

    match_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("match.id", ondelete="CASCADE"), nullable=False
    )

    rounds_won: Mapped[int] = mapped_column(Integer, nullable=False)

    rounds_lost: Mapped[int] = mapped_column(Integer, nullable=False)

    kills: Mapped[int] = mapped_column(Integer, nullable=False)

    deaths: Mapped[int] = mapped_column(Integer, nullable=False)

    assists: Mapped[int] = mapped_column(Integer, nullable=False)

    adr: Mapped[float] = mapped_column(DECIMAL(5, 1), nullable=False)

    kast: Mapped[float] = mapped_column(DECIMAL(5, 1), nullable=False)

    hs: Mapped[float] = mapped_column(DECIMAL(5, 1), nullable=False)

    ping: Mapped[int] = mapped_column(Integer, nullable=False)

    enemies_flashed: Mapped[int] = mapped_column(Integer, nullable=False)

    # opens relationship

    # clutches relationship

    # weapons relationship
