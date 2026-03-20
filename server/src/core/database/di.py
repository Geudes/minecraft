from src.core.database.utils import Database
from src.core.config import settings, Settings

class DBProvaider:
    serves: Database = Database()
    settings: Settings = settings

    serves.create_engine(
        settings.DATABASE_URL,
    )

    serves.create_session()

    session = serves.session
    async def get_session(self):
        async with self.session as session:
            try:
                yield session
                await session.flush()
            except Exception as e:
                await session.rollback()
                raise e
            finally:
                await session.close()


db = DBProvaider()
