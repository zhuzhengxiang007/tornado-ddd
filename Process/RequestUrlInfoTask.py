from Common.Share.CronTab import CronTab
from Common.Redis import init_redis
import Config.queue as queue_map
import json

class RequestUrlInfoTask(CronTab):
    def __init__(self, count=1, time=1) -> None:
        super().__init__(count, time)

    async def run(self):
        redis = init_redis()
        content = await redis.lpop(queue_map.SYSTEM_LOG_REDIS_QUEUE_KEY)
        if content == None:
            return None
        content = json.loads(content)
        print(content)

    def callback(self):
        pass