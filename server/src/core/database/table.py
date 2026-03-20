from uuid import uuid4, UUID
from datetime import datetime
from sqlalchemy import UUID as SQL_UUID, DateTime, String, Integer, Enum as SQLEnum
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, declared_attr
from enum import Enum

class ServerStatus(str, Enum):
    ONLINE = "online"
    OFFLINE = "offline"
    ACTIVE = "active"

class UserRole(str, Enum):
    ADMIN = "Admin"
    USER = "User"
    CREATOR = "Creator"

class TableSQLBase(DeclarativeBase):
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id: Mapped[UUID] = mapped_column(SQL_UUID, default=uuid4, unique=True, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, onupdate=datetime.utcnow, nullable=True)

class User(TableSQLBase):
    username: Mapped[str] = mapped_column(String(50), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    role: Mapped[UserRole] = mapped_column(SQLEnum(UserRole), default=UserRole.USER)

class Server(TableSQLBase):
    img_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    domain: Mapped[str | None] = mapped_column(String(255), nullable=True)
    ip_address: Mapped[str] = mapped_column(String(45), nullable=False)
    port: Mapped[int] = mapped_column(Integer, default=25565)
    version: Mapped[str] = mapped_column(String(20))
    max_players: Mapped[int] = mapped_column(Integer, default=20)
    online_players: Mapped[int] = mapped_column(Integer, default=0)
    status: Mapped[ServerStatus] = mapped_column(
        SQLEnum(ServerStatus), default=ServerStatus.OFFLINE
    )
    type: Mapped[str] = mapped_column(String(50), nullable=False)
