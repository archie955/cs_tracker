from sqlalchemy.orm import Mapped, relationship

from database.database import Base
from models.associations import user_match
from models.mixins import Name, TimeStamps
from models.user_models import User


class Match(Base, Name, TimeStamps):
    players: Mapped[list["User"]] = relationship(
        secondary=user_match, back_populates="matches"
    )
