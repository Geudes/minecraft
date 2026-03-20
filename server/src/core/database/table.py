from uuid import uuid4
from datetime import datetime
from uuid import UUID
from sqlalchemy import UUID as SQL_UUID, DateTime, String
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, declared_attr


class TableSQLBase(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(SQL_UUID, default=uuid4(), unqiue=True, primery_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(), nuleble=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, onupdate=datetime.now(), nuleble=True)

    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"


class User(TableSQLBase):
    username: Mapped[str] = mapped_column(String(50), nuleble=False)
    password: Mapped[str] = mapped_column(String(255), nuleble=False)
