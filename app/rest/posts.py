from fastapi import APIRouter, Depends

from app.db import DatabaseManager, get_database
from app.db.models import PostDB, OID

router = APIRouter()


@router.get('/')
async def all_posts(db: DatabaseManager = Depends(get_database)):
    posts = await db.get_posts()
    return posts


@router.get('/{post_id}')
async def one_post(post_id: OID, db: DatabaseManager = Depends(get_database)):
    post = await db.get_post(post_id=post_id)
    return post


@router.put('/{post_id}')
async def update_post(post_id: OID, post: PostDB, db: DatabaseManager = Depends(get_database)):
    post = await db.update_post(post=post, post_id=post_id)
    return post


@router.post('/', status_code=201)
async def add_post(post_response: PostDB, db: DatabaseManager = Depends(get_database)):
    post = await db.add_post(post_response)
    return post


@router.delete('/{post_id}')
async def delete_post(post_id: OID, db: DatabaseManager = Depends(get_database)):
    await db.delete_post(post_id=post_id)
