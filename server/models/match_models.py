from datetime import datetime

from sqlalchemy import DateTime, Index, Integer
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.database import Base
from models.associations import user_losses, user_wins
from models.enums import Maps
from models.mixins import Name, TimeStamps
from models.user_models import User

maps = SQLEnum(Maps, name="maps")


class Match(Base, Name, TimeStamps):
    __table_args__ = Index("ix_match_maps", "map")

    won_rounds: Mapped[int] = mapped_column(Integer, nullable=False)

    lost_rounds: Mapped[int] = mapped_column(Integer, nullable=False)

    map: Mapped[Maps] = mapped_column(maps, nullable=False)

    date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    winners: Mapped[list["User"]] = relationship(
        secondary=user_wins, back_populates="wins"
    )

    losers: Mapped[list["User"]] = relationship(
        secondary=user_losses, back_populates="losses"
    )
