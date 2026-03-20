from uuid import uuid4
from datetime import datetime
from uuid import UUID
from sqlalchemy import UUID as SQL_UUID, DateTime, String, Integer, Enum
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, declared_attr

from server.src.application.rest.v1.schemas.server import ServerStatus


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


class Server(TableSQLBase):
    class Server(TableSQLBase):
        img_url: Mapped[str | None] = mapped_column(String(500))
        name: Mapped[str] = mapped_column(String(100))
        ip_address: Mapped[str] = mapped_column(String(45))
        port: Mapped[int] = mapped_column(Integer, default=25565)
        version: Mapped[str] = mapped_column(String(20))
        max_players: Mapped[int] = mapped_column(Integer, default=20)
        online_players: Mapped[int] = mapped_column(Integer, default=0)
        status: Mapped[ServerStatus] = mapped_column(
            Enum(ServerStatus), default=ServerStatus.OFFLINE
        )
        type: Mapped[str] = mapped_column(String(50), nullable=False)
