from abc import abstractmethod
from typing import List

from app.db.models import PostDB, PydanticObjectId


class DatabaseManager(object):
    @property
    def client(self):
        raise NotImplementedError

    @property
    def db(self):
        raise NotImplementedError

    @abstractmethod
    async def connect_to_database(self, path: str):
        pass

    @abstractmethod
    async def close_database_connection(self):
        pass

    @abstractmethod
    async def get_posts(self) -> List[PostDB]:
        pass

    @abstractmethod
    async def get_post(self, post_id: PydanticObjectId) -> PostDB:
        pass

    @abstractmethod
    async def add_post(self, post: PostDB):
        pass

    @abstractmethod
    async def update_post(self, post_id: PydanticObjectId, post: PostDB):
        pass

    @abstractmethod
    async def delete_post(self, post_id: PydanticObjectId):
        pass
