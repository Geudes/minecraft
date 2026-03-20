from src.core.database.utils import Database
from src.core.config import settings, Settings

class DBProvaider:
    serves: Database = Database()
    settings: Settings = settings
    
    serves.create_engine(
        settings.DATABASE_URL,
    )
    
    serves.create_session()
    
    serves.get_session()


db = DBProvaider()
