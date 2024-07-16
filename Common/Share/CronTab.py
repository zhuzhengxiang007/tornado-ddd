import tornado.ioloop
import tornado.web
import multiprocessing
import time
from abc import ABC, abstractmethod

class CronTab(ABC):
    def __init__(self,count=1,time=1) -> None:
        self.count = count
        self.time = time
        self.handler()
        pass

    def start_periodic_task(self):
        # 创建一个 IOLoop 实例
        io_loop = tornado.ioloop.IOLoop.current()

        # 创建一个 PeriodicCallback 实例，每隔self.time秒执行一次 run 函数
        callback = tornado.ioloop.PeriodicCallback(self.run, self.time*1000)

        # 启动定时任务
        callback.start()

        # 启动 IOLoop 事件循环
        io_loop.start()

    def handler(self):
        # 创建多个进程
        processes = []
        for i in range(self.count):  # 创建self.count个进程
            process = multiprocessing.Process(target=self.start_periodic_task)
            processes.append(process)
            process.start()

        # 等待所有进程结束
        for process in processes:
            process.join()   

    @abstractmethod
    def run(self):
        pass