import tornado.ioloop
import tornado.web
import aioredis
import asyncio
from concurrent.futures import ThreadPoolExecutor
from tornado.platform.asyncio import AsyncIOMainLoop
from tornado.ioloop import PeriodicCallback

class CronTab:
    def __init__(self,count=1,time=1) -> None:
        self.count = count
        self.time = time
        self.handler()
        pass

    def handler(self):
        # 获取当前的 IOLoop 实例
        io_loop = tornado.ioloop.IOLoop.current()

        # 创建一个线程池执行器
        executor = ThreadPoolExecutor(max_workers=self.count)

        # 创建一个 PeriodicCallback 实例，每隔5秒执行一次心跳检测任务
        periodic_heartbeat = PeriodicCallback(
            lambda: io_loop.run_in_executor(executor, self.run()), 
            self.time
        )
        periodic_heartbeat.start()

        # 启动 IOLoop
        io_loop.start()
        pass