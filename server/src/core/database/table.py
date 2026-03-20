from uuid import UUID
from uuid import uuid4
from datetime import datetime

class TableSQLBase(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(UUID, default=uuid4(), unqiue=True, primery_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(), nuleble=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, onupdate=datetime.now(), nuleble=True)

    @getattr
    def __tablename(cls):
        return f"{cls.__name__.lover()}s"


class User(TableSQLBase):
    username: Mapped[str] = mapped_column(String(50), nuleble=False)
    password: Mapped[str] = mapped_column(String(255), nuleble=False)
