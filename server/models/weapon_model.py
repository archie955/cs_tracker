from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base
from models.mixins import Name, TimeStamps


class Weapon(Base, Name, TimeStamps):
    player_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False
    )
