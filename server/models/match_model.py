from datetime import datetime

from sqlalchemy import DateTime, Index, Integer
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.database import Base
from models.associations import user_matches
from models.enums import Maps, MatchTypes
from models.mixins import Name, TimeStamps
from models.user_model import User

maps = SQLEnum(Maps, name="maps")
types = SQLEnum(MatchTypes, name="types")


class Match(Base, Name, TimeStamps):
    __table_args__ = Index("ix_match_maps", "map")

    map: Mapped[Maps] = mapped_column(maps, nullable=False)

    tickrate: Mapped[int] = mapped_column(Integer, nullable=False)

    type: Mapped[MatchTypes] = mapped_column(types, nullable=False)

    time: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    players: Mapped[list["User"]] = relationship(
        secondary=user_matches, back_populates="players"
    )
