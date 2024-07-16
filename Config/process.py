"""
定义定时任务
name 任务名
handler 定时任务类
count 启动线程个数
time 时间间隔
"""
"""
禁止修改
"""
import importlib
def Crontab():
    for _ in TASK:
        module_name = 'Process.' + _['handler']
        module = importlib.import_module(module_name)
        cron = getattr(module, _['handler'])
        cron(_['count'],_['time'])
    pass
"""
禁止修改
"""

#########配置定时任务开始##############
TASK = [
    {
        'name':'request_url_info_task',
        'handler':'RequestUrlInfoTask',
        'count':4,
        'time':1
    }
]
#########配置定时任务结束##############
