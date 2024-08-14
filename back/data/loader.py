from database.mongodb import MongoDB
from redis.asyncio import StrictRedis


mdb = MongoDB()
redis = StrictRedis(host='redis', port=6379)
