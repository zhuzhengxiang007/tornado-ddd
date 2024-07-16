"""
定义定时任务
handler 定时任务类
count 启动线程个数
time 时间间隔
"""
import Common.Redis


TASK = [
    'request_url_info_task' = {
        'handler':Common.Redis.aioredis,
        'count':4,
        'time':1
    }
]