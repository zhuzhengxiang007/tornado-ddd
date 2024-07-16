from Common.Share.CronTab import CronTab

class RequestUrlInfoTask(CronTab):
    def __init__(self, count=1, time=1) -> None:
        super().__init__(count, time)

    async def run():
        print('run')
        pass