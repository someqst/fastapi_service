import json
from fastapi import APIRouter
from pydantic import BaseModel
from data.loader import mdb, redis


class Message(BaseModel):
    user: int
    message: str


router = APIRouter()


@router.post('/message')
async def post_message(message: Message):
    if await redis.get('all_messages'):
        await redis.delete('all_messages')
    if await mdb.write_message(message.user, message.message):
        return {'status': 'ok'}
    return {'status': 'error'}


@router.get('/messages')
async def get_messages():
    serialized_data = await redis.get('all_messages')
    if serialized_data:
        data = json.loads(serialized_data)
        return data

    all_messages = await mdb.get_all_messages()
    if not all_messages:
        return {'status': 'No Messages'}
    
    serialized_data = json.dumps(all_messages)
    await redis.set('all_messages', serialized_data)
    return all_messages
    
