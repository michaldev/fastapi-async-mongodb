from app.db.database_manager import DatabaseManager
from app.db.impl.mongo_manager import MongoManager

db = MongoManager()


async def get_database() -> DatabaseManager:
    return db
