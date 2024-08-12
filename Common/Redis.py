import redis.asyncio as aioredis
import Config.redis as c_redis

#redis://:password@host:port/db 配置密码

# 初始化 Redis 连接池
def init_redis():
    dns = f'redis://{c_redis.REDIS_HOST}:{c_redis.REDIS_PORT}/{c_redis.REDIS_DB}'
    redis = aioredis.from_url(dns)
    return redis

# 心跳检测任务
async def heartbeat(redis):
    try:
        await redis.ping()
        #print("Redis connection is active.")
    except aioredis.RedisError as e:
        print(f"Error: {e}")
        # 可以在这里重新连接 Redis 或者进行其他处理
        await init_redis()

# class RedisService:
#     def __init__(self) -> None:
#         print('redis init')
#         self.redis = aioredis.from_url(f'redis://{c_redis.REDIS_HOST}:{c_redis.REDIS_PORT}/{c_redis.REDIS_DB}')
#         pass

#     def __del__(self) -> None:
#         print('redis close')
#         self.redis.close()
#         pass