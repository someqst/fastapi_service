from motor.motor_asyncio import AsyncIOMotorClient
from data.config import settings


class MongoDB():
    def __init__(self) -> None:
        client = AsyncIOMotorClient(host=settings.MONGO_TOKEN.get_secret_value())
        self.collection = client.work.messages
    
    async def write_message(self, user, message):
        try:
            query = {"_id": user}
            update = {"$push": {'message': message}}
            user_message = await self.collection.find_one(query)
            if user_message:
                await self.collection.update_one(query, update)
            else:
                await self.collection.insert_one({'_id': user, 'message': [message]})
            return True
        except:
            return False


    async def get_all_messages(self):
        messages = await self.collection.find().to_list(None)
        if messages:
            return [{'user': message['_id'], 'messages': message['message']} for message in messages]
        else:
            return False