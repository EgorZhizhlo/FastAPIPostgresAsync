from sqlalchemy.orm import Mapped
from app.db import (
    Base, str_not_none, str_not_none_uniq
)


class Users(Base):
    __tablename__ = "users"

    username: Mapped[str_not_none]
    email: Mapped[str_not_none_uniq]
    password: Mapped[str_not_none]
